from django.db import models


class Song(models.Model):

    name = models.CharField(null=False, max_length = 100)
    duration = models.PositiveIntegerField(null=False)
    uploaded_time = models.DateTimeField(null=False, auto_now_add=True)



class Podcast(models.Model):

    name = models.CharField(null=False, max_length = 100)
    duration = models.PositiveIntegerField(null=False)
    uploaded_time = models.DateTimeField(null=False, auto_now_add=True)
    host = models.CharField(null=False, max_length = 100)
    participants = models.TextField(null=True)


class Audiobook(models.Model):

    title = models.CharField(null=False, max_length = 100)
    author = models.CharField(null=False, max_length = 100)
    narrator = models.CharField(null=False, max_length = 100)
    duration = models.PositiveIntegerField(null=False)
    uploaded_time = models.DateTimeField(null=False, auto_now_add=True)
