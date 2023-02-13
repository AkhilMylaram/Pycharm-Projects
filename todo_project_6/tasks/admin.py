from django.contrib import admin
from . import  models
# Register your models here.
#to work on Actions
#query set contains the list of the contents we have
def mark_complete(model_admin, request, queryset):
    from django.utils import timezone
    queryset.update(
        status=models.TaskStatus.COMPLETED,
        completed_at=timezone.now()
    )
mark_complete.short_description="mark thease tasks as completed right now"

def mark_pending(model_admin, request, queryset):
    from django.utils import timezone
    queryset.update(
        status=models.TaskStatus.PENDING,
        completed_at=None
    )
mark_pending.short_description="mark thease tasks as pending"

class TaskAdmin(admin.ModelAdmin):
    fields=['content','deadline','tags']
    list_display = ['content','status','deadline','get_all_tags']

    list_editable = ['status']
    list_filter = ['status','deadline','tags']
    search_fields = ['content','tags__name']

    actions = [mark_complete,mark_pending]

    ordering = ['status','deadline']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']



admin.site.register(models.Task,TaskAdmin)
admin.site.register(models.Tag,TagAdmin)


