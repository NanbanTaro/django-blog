from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    posted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.text
