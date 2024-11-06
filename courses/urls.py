from django.urls import path
from .views import CourseCreateView, ScheduledCourseListView

urlpatterns = [
    path('add/', CourseCreateView.as_view(), name='add-course'),
    path('view/', ScheduledCourseListView.as_view(), name='view-scheduled-courses'),
]
