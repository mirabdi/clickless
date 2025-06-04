from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import APIException
from django.db.models import Count, Sum, Avg, Min, Max
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
# from authentication.token_auth import UserTokenActiveAuth
from django.db import transaction
from rest_framework.decorators import action
from openpyxl import Workbook
from django.http import HttpResponse

class CustomAPIException(APIException):
    """Customizable API exception for structured error responses."""
    
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, message="An error occurred", response=None):
        self.status_code = status_code
        self.detail = {
            "status": 1 if status_code == status.HTTP_404_NOT_FOUND else 2,
            "message": message,
            "response": response if response else []
        }

class CustomViewSet(ViewSet):
    # !required
    model_manager = None 
    queryset = None  
    serializer_class = None 
    representor_class = None 
    
    # optional
    authentication_classes = []
    permission_classes = []
    limit = 10
    offset = 0
    search_fields = ['username', 'name', 'title', 'content', 'description', 'phone']

    def get_queryset(self):
        return self.queryset.filter(deleted=False)

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except self.model_manager.model.DoesNotExist:
            raise CustomAPIException(status_code=status.HTTP_404_NOT_FOUND, message=f"{self.model_manager.model.__name__} not found")

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return self.serializer_class
        return self.representor_class

    def list(self, request):
        print(request.user, '*********')
        queryset = self.get_queryset()
        queryset = self._prepare_qs(request, queryset)
        limit = int(request.GET.get('limit', self.limit))
        offset = int(request.GET.get('offset', self.offset))
        result = self.representor_class(queryset, context={'detailed': True, 'limit': limit, 'offset': offset}).data
        return self._respond(result)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        return self._respond(self.representor_class(instance, context={'detailed': True}).data)
    
    @transaction.atomic
    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return self._respond(
                    serializer.errors,
                    status.HTTP_400_BAD_REQUEST,
                    message='Invalid data'
                )
            instance = serializer.save()
            response_serializer = self.representor_class(instance, context={'detailed': True})
            return self._respond(
                response_serializer.data,
                status.HTTP_201_CREATED,
                f"{self.model_manager.model.__name__} successfully created",
                status_id=0
            )
        except Exception as e:
            return self._respond({}, status.HTTP_400_BAD_REQUEST, str(e), status_id=1)

    @transaction.atomic
    def update(self, request, pk=None):
        try:
            instance = self.model_manager.get(pk=pk)
            if not instance:
                return self._respond({}, f"{self.model_manager.model.__name__} not found", status.HTTP_404_NOT_FOUND)

            serializer = self.serializer_class(
                instance,
                data=request.data,
                partial=True
            )
            if not serializer.is_valid():
                return self._respond(
                    serializer.errors,
                    status.HTTP_400_BAD_REQUEST,
                    message='Invalid data'
                )

            updated_instance = serializer.save()
            response_serializer = self.representor_class(updated_instance, context={'detailed': True})
            return self._respond(
                response_serializer.data,
                message=f"{self.model_manager.model.__name__} successfully updated"
            )
        except Exception as e:
            return self._respond({}, status.HTTP_400_BAD_REQUEST, str(e))

    def destroy(self, request, pk=None):
        try:
            instance = self.model_manager.get(pk=pk)
            if not instance:
                return self._respond({}, status.HTTP_400_BAD_REQUEST, f"{self.model_manager.model.__name__} not found", status.HTTP_404_NOT_FOUND)

            instance.deleted = True
            instance.save()
            return self._respond(
                None,
                message=f"{self.model_manager.model.__name__} successfully deleted"
            )
        except Exception as e:
            return self._respond({}, status.HTTP_400_BAD_REQUEST, str(e))

    @action(methods=['get'], detail=False, url_path='export')
    def export(self, request):
        self.limit = 10000
        self.offset = 0
        queryset = self._prepare_qs(request)
        if queryset.count() > 10000:
            return self._respond({}, status.HTTP_400_BAD_REQUEST, message='Too much data to process, please filter the request')
        column_names = [field.name for field in self.get_queryset().model._meta.fields]
        data = [column_names] + list(self.get_queryset().values_list())
        return self._export_excel(data)
    
    @action(detail=True, methods=['get'], url_path='members')
    def members(self, request, pk=None):
        instance = self.model_manager.get(pk=pk)
        return self._related_field_action(request, instance, 'members')
    
    def _related_field_action(self, request, instance, field_name):
        related_manager = getattr(instance, field_name, None)

        if not related_manager: 
            return Response(
                {'status': 1, 'message': f'Field {field_name} is invalid for this ViewSet'},
                status=400
            )

        queryset = related_manager.all()
        queryset = self._prepare_qs(request, queryset)
        
        if request.method == 'GET':
            result = related_manager.serialize(queryset, self.limit, self.offset, {'detailed': True})
            return self._respond(result)

        elif request.method == 'PUT':
            data = request.data
            item_ids = [item.get('id') for item in data]
            items = related_manager.model.objects.filter(id__in=item_ids)
            related_manager.set(items)
            return self._respond(
                self.representor_class(instance, context={'detailed': True}).data
            )

        elif request.method == 'PATCH':
            item_id = request.data.get('id')
            if not item_id:
                return self._respond(
                    {}, 
                    status.HTTP_400_BAD_REQUEST,
                    message='ID is required'
                )
            
            try:
                item = related_manager.model.objects.get(id=item_id)
                related_manager.add(item)
                return self._respond(
                    self.representor_class(instance, context={'detailed': True}).data
                )
            except related_manager.model.DoesNotExist:
                return self._respond(
                    {},
                    status.HTTP_400_BAD_REQUEST,
                    message=f'{related_manager.model.__name__} not found'
                )

        elif request.method == 'DELETE':
            item_id = request.data.get('id')
            if not item_id:
                return self._respond(
                    {},
                    status.HTTP_400_BAD_REQUEST,
                    message='ID is required'
                )
            
            try:
                item = related_manager.model.objects.get(id=item_id)
                related_manager.remove(item)
                return self._respond(
                    self.representor_class(instance, context={'detailed': True}).data
                )
            except related_manager.model.DoesNotExist:
                return self._respond(
                    {},
                    status.HTTP_400_BAD_REQUEST,
                    message=f'{related_manager.model.__name__} not found'
                )

    def _prepare_qs(self, request, queryset = None):
        order = request.GET.get('order', None)
        filter = request.GET.get('filter', None)
        search = request.GET.get('search', None)
        
        if queryset is None:
            queryset = self.get_queryset()

        if search:
            search_fields = self.search_fields
            q_objects = Q()
            for field in search_fields:
                if hasattr(queryset.model, field):
                    q_objects |= Q(**{f'{field}__icontains': search})
            queryset = queryset.filter(q_objects)
        
        if filter:
            queryset = self._apply_filter(queryset, filter)
        if order:
            queryset = self._apply_order(queryset, order)
        return queryset

    def _apply_order(self, queryset, order):
        order_conditions = []
        for order_exp in order.split(';'):
            order_exp = order_exp.strip()
            if ',' in order_exp:
                field, direction = order_exp.split(',', 1)
                field = field.strip()
                direction = direction.strip().lower()

                aggregation_functions = {
                    'count': Count,
                    'sum': Sum,
                    'avg': Avg,
                    'min': Min,
                    'max': Max,
                }

                if '__' in field:
                    model_field, func_name = field.rsplit('__', 1)
                    if func_name in ['count', 'sum', 'avg', 'min', 'max']:
                        annotation_name = f'{model_field}_{func_name}'
                        queryset = queryset.annotate(
                            **{annotation_name: aggregation_functions[func_name](model_field)}
                        )
                        field = annotation_name

                if direction == 'desc':
                    order_conditions.append(f'-{field}')
                elif direction == 'asc':
                    order_conditions.append(field)
                else:
                    raise ValueError(f"Invalid order direction: {direction}")
            else:
                order_conditions.append(order_exp)
        return queryset.order_by(*order_conditions)
    
    def _apply_filter(self, queryset, filter):
        operator_map = {
            '!=': '',
            '>': '__gt',
            '<': '__lt',
            '>=': '__gte',
            '<=': '__lte',
            '=': '',
        }

        conditions = []
        for filter_exp in filter.split(';'):
            for op, django_lookup in operator_map.items():
                if op in filter_exp:
                    field, value = filter_exp.split(op, 1)
                    field = field.strip()
                    value = value.strip()

                    if value.startswith('[') and value.endswith(']'):
                        value_list = value[1:-1].split(',')
                        value_list = [v.strip() for v in value_list]
                        conditions.append((field, '__in', value_list, op == '!='))
                    else:
                        conditions.append((field.strip(), django_lookup, value.strip(), op == '!='))
                    break

        q_objects = Q()
        exclude_objects = Q()

        for field, lookup, value, is_exclude in conditions:
            if is_exclude:
                exclude_objects |= Q(**{f"{field}{lookup}": value})
            else:
                q_objects &= Q(**{f"{field}{lookup}": value})

        if exclude_objects:
            queryset = queryset.exclude(exclude_objects)
        if q_objects:
            queryset = queryset.filter(q_objects)

        return queryset

    def _export_excel(self, data):
        wb = Workbook()
        ws = wb.active
        ws.title = 'Sheet1'
        for row in data:
            ws.append(row)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="export.xlsx"'
        wb.save(response)
        return response

    def _respond(self, data, status_code=status.HTTP_200_OK, message='success', status_id=0):
        return Response({
            'status': status_id,
            'message': message,
            'response': data
        }, status=status_code)
