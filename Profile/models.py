from django.db import models


# Create your models here.
class Contact(models.Model):
    Contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name + "(" + self.email + ") on subject: " + self.subject
