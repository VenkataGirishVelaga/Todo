from django.contrib import admin

from .models import Person, Todo

admin.site.register(Person)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'deadline', 'done')
    list_filter = ( 'priority', 'deadline')
    search_fields = ('title', 'description')




