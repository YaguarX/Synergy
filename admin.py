from django.contrib import admin
from ckeditor.widgets import CKEditorUploadingWidget
from django.forms import TextInput, Textarea
from .models import Human

class HumanAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'description')
    search_fields = ('name', 'bio', 'description')

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'bio': CKEditorUploadingWidget(),
            'description': CKEditorUploadingWidget(config_name='custom'),
        }
        return super().get_form(request, obj, **kwargs)

admin.site.register(Human, HumanAdmin)
