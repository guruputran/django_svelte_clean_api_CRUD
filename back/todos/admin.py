from django.contrib import admin
from .models import Todo

#admin.site.register(Todo)

#https://stackoverflow.com/questions/10543032/how-to-show-all-fields-of-model-in-admin-page
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Todo._meta.fields if field.name not in ('id', 'qual_key', 'qual_desc')]
    list_display.insert(0, '__str__')