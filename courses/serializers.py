from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['admin']
        read_only_fields = ['admin']  # Ensure `admin` is read-only
