from django.contrib import admin
from .models import Data, StarRating
# Import export
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
class StarRatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(StarRating)


class DataResource(resources.ModelResource):
    class Meta:
        model = Data
        fields = ('run', 'nombre', 'exam', 'fecha', 'hora_inicio', 'hora_fin', 'sala', 'proctor', 'sede')
        import_id_fields = ('run',)
        export_order = ('exam', 'sala', 'proctor',)
        readonly_fields = ('created', 'updated',)


@admin.register(Data)
class DataAdmin(ImportExportActionModelAdmin):
    list_display = ('run', 'exam', 'fecha', 'hora_inicio', 'hora_fin', 'sala', 'proctor', 'sede')
    search_fields = ('run', 'nombre', 'exam', 'fecha', 'sala', 'proctor')
    exclude = ('created', 'updated')
    list_filter = ['exam', 'sede']
    empty_value_display = '-vacío-'
    resource_class = DataResource
