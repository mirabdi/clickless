from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    def handle(self, *args, **options):
        fields_file = open('fields.txt', 'w')
        apps_list = [
        "users",
        "pain_management",
        "exercises",
        "surveys",
        "content",
        "habits",
        "medications",
        "notifications",
        ]

        for app_name in apps_list:
            app = apps.get_app_config(app_name)
            models_list = app.get_models()
            fields_file.write(f"- {app_name}\n")
            for counter, model in enumerate(models_list, start=1):
                fields = model._meta.get_fields()
                model_name = model.__name__
                app_name = app.verbose_name

                fields_file.write(f"    {counter}) {model_name}\n")

                for field in fields:
                    field_name = field.name
                    field_type = field.get_internal_type()
                    fields_file.write(f"        -  {field_name} " +"-"*(30 - len(field_name)) +  f" {field_type}\n")

                fields_file.write("\n")

        fields_file.close()
