from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'admin', 'publish_date')
    
    # Fields to filter by in the admin list view
    list_filter = ('publish_date',)
    
    # Fields to search by in the admin list view
    search_fields = ('title', 'description')
    
    # Fields to display on the course detail page
    fieldsets = (
        (None, {'fields': ('title', 'video_url', 'description', 'publish_date', 'admin')}),
    )

admin.site.register(Course, CourseAdmin)
