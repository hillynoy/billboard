from __future__ import unicode_literals
from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now= False, auto_now_add=True)
    published_time = models.DateTimeField(auto_now= True, auto_now_add=False)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title +self.content + str(self.timestamp) + self.author




