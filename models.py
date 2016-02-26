from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    last_login = models.DateTimeField()
    place = models.CharField(max_length=50)
    dob = models.DateField()
    job = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Connection(models.Model):
    user_id1 = models.CharField(max_length=30)
    user_id2 = models.CharField(max_length=30)

    def __str__(self):
        return (self.user_id1,self.user_id2)


class request(models.Model):
    request_from = models.CharField(max_length=30)
    request_to = models.CharField(max_length=30)

    def __str__(self):
        return (self.request_from, self.request_to)

    def accept_request(self,username):
        conn = Connection(self.username, username)
        conn.save()

    def decline_request(self,username):
        return 