from django.db import models
from users.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    description = models.TextField()
    publish_date = models.DateTimeField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.title
