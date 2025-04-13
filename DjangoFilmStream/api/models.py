import uuid
from django.db import models

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    video_url = models.URLField(blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)
    cover_image_url = models.URLField(blank=True, null=True)

    is_public = models.BooleanField(default=True)
    duration = models.PositiveIntegerField(help_text="Duration in seconds", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title