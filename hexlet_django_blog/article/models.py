from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
