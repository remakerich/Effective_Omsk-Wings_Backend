from django.db import models


class Rule(models.Model):
    icon = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title
