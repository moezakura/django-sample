from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=40)
    text = models.CharField(max_length=65535)
    post_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text