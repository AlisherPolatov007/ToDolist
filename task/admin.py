from django.contrib import admin

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created_at', 'update_at')  # Admin panelda ko'rinadigan ustunlar
    search_fields = ('title',)  # Qidirish imkoniyati
    list_filter = ('completed', 'created_at')  # Filtrlash opsiyalari
