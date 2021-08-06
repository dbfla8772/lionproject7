from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    senderID = models.CharField(max_length=100)
    receiverID = models.CharField(max_length=100)
    send_date = models.DateTimeField(auto_now = True)
    content = models.TextField()

    def summary(self):
        return self.content[:50]  