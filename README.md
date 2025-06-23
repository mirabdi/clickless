# Clickless API Documentation

## Overview

Clickless is a Django REST API project designed for pain management and wellness tracking. The project uses a sophisticated abstraction layer in the `core` app that provides reusable components for rapid API development across multiple domains.

## Core Architecture

The `core` app provides three fundamental abstractions that eliminate boilerplate code and ensure consistency across all apps:

### 1. CustomModel

**Location**: `core/models.py`

**Purpose**: Base model class that provides soft deletion, metadata generation, and URL generation capabilities.

**Key Features**:
- **Soft Deletion**: `deleted` and `deleted_at` fields with automatic filtering
- **Metadata Generation**: `meta()` method for consistent object representation
- **URL Generation**: Automatic RESTful URL generation from class names
- **Custom Manager**: Enhanced manager with serialization capabilities

**Usage Example**:
```python
from core.models import CustomModel

class Exercise(CustomModel):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'v2_exercise'
```

**Benefits**:
- Automatic soft deletion support
- Consistent metadata across all models
- Built-in URL generation
- Enhanced query manager with serialization

### 2. CustomRepresentor

**Location**: `core/representors.py`

**Purpose**: Handles output serialization with automatic metadata inclusion and flexible detail levels.

**Key Features**:
- **Automatic Metadata**: Includes `meta` field with object information
- **Detail Control**: `detailed` context parameter controls response depth
- **List Support**: Handles both single objects and querysets
- **Field Mapping**: Automatic mapping from model fields to serializer fields
- **Method Fields**: Support for custom `get_*` methods

**Usage Example**:
```python
from core.representors import CustomRepresentor

class ExerciseRepresentor(CustomRepresentor):
    class Meta:
        model = Exercise
        fields = ['id', 'title', 'type', 'histories']
    
    def get_custom_field(self, obj):
        return f"Custom: {obj.title}"
```

**Response Format**:
```json
{
  "meta": {
    "id": 1,
    "name": "Exercise Title",
    "type": "exercise",
    "href": "/exercises/1"
  },
  "id": 1,
  "title": "Exercise Title",
  "type": "strength",
  "custom_field": "Custom: Exercise Title"
}
```

### 3. CustomViewSet

**Location**: `core/views.py`

**Purpose**: Complete CRUD ViewSet with built-in pagination, filtering, searching, and export capabilities.

**Key Features**:
- **Automatic CRUD**: Complete create, read, update, delete operations
- **Pagination**: Built-in limit/offset pagination
- **Search**: Multi-field search with configurable search fields
- **Filtering**: Advanced filtering with operators (`=`, `!=`, `>`, `<`, `>=`, `<=`)
- **Ordering**: Multi-field ordering with aggregation support
- **Export**: Excel export functionality
- **Related Fields**: Built-in support for managing related objects
- **Consistent Responses**: Standardized response format

**Usage Example**:
```python
from core.views import CustomViewSet

class ExerciseViewSet(CustomViewSet):
    model_manager = Exercise.objects
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    representor_class = ExerciseRepresentor
    search_fields = ['title', 'type']
    limit = 20
```

**Required Configuration**:
- `model_manager`: Model's manager instance
- `queryset`: Base queryset
- `serializer_class`: Serializer for input validation
- `representor_class`: Representor for output formatting

**Optional Configuration**:
- `search_fields`: Fields to search in
- `limit`: Default pagination limit
- `offset`: Default pagination offset

## API Features

### Standard Response Format

All API responses follow a consistent format:

```json
{
  "status": 0,
  "message": "success",
  "response": {
    "meta": {
      "type": "exercise-list",
      "href": "/exercises/",
      "size": 100,
      "limit": 10,
      "offset": 0
    },
    "rows": [...]
  }
}
```

### Pagination

**Query Parameters**:
- `limit`: Number of items per page (default: 10)
- `offset`: Starting position (default: 0)

**Example**: `GET /exercises/?limit=20&offset=40`

### Search

**Query Parameter**: `search`

**Example**: `GET /exercises/?search=strength`

Searches across all fields specified in `search_fields`.

### Filtering

**Query Parameter**: `filter`

**Operators**: `=`, `!=`, `>`, `<`, `>=`, `<=`

**Examples**:
- `GET /exercises/?filter=type=strength`
- `GET /exercises/?filter=created_at__gte=2024-01-01`
- `GET /exercises/?filter=type__in=[strength,cardio]`

### Ordering

**Query Parameter**: `order`

**Format**: `field,direction` or `field__aggregation,direction`

**Examples**:
- `GET /exercises/?order=title,asc`
- `GET /exercises/?order=histories__count,desc`

### Export

**Endpoint**: `GET /exercises/export/`

Exports data to Excel format with all current filters applied.

## App Structure

Each app follows a consistent structure:

```
app_name/
├── models.py          # CustomModel subclasses
├── representors.py    # CustomRepresentor subclasses
├── serializers.py     # CustomSerializer subclasses
├── views.py          # CustomViewSet subclasses
├── urls.py           # URL routing
└── admin.py          # Django admin configuration
```

## Advanced Features

### Custom Methods in Representors

Add custom computed fields using `get_*` methods:

```python
class UserRepresentor(CustomRepresentor):
    class Meta:
        model = User
        fields = ['id', 'email', 'stats']
    
    def get_stats(self, obj):
        return {
            'total_exercises': obj.exercise_histories.count(),
            'recent_activity': obj.exercise_histories.filter(
                created_at__gte=timezone.now() - timedelta(days=7)
            ).count()
        }
```

### Related Field Management

CustomViewSet provides built-in support for managing related objects:

```python
# GET /exercises/1/histories/ - List related objects
# PUT /exercises/1/histories/ - Replace all related objects
# PATCH /exercises/1/histories/ - Add related object
# DELETE /exercises/1/histories/ - Remove related object
```

### Soft Deletion

All models support soft deletion:

```python
# Soft delete
instance.delete()  # Sets deleted=True

# Restore
instance.restore()  # Sets deleted=False

# Hard delete
instance.hard_delete()  # Actually removes from database

# Query with deleted items
Model.objects.with_deleted().all()
```

## Best Practices

1. **Always inherit from core classes**: Use `CustomModel`, `CustomRepresentor`, `CustomSerializer`, and `CustomViewSet`
2. **Define search fields**: Configure `search_fields` in ViewSets for better UX
3. **Use method fields**: Add computed fields using `get_*` methods in representors
4. **Leverage soft deletion**: Use soft deletion for data integrity
5. **Consistent naming**: Follow the naming convention for representors (`ModelNameRepresentor`)

## Error Handling

The API uses standardized error responses:

```json
{
  "status": 1,
  "message": "Error description",
  "response": []
}
```

Common status codes:
- `0`: Success
- `1`: Not found
- `2`: Validation error

This architecture provides a robust foundation for building consistent, maintainable APIs with minimal boilerplate code. 