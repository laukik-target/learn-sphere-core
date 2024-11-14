from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer
from django.utils import timezone

class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the `admin` field to the authenticated user
        serializer.save(admin=self.request.user)


class ScheduledCourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Course.objects.filter(publish_date__lte=timezone.now())
