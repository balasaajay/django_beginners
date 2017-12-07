from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, unique=True)
    emailid = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.emailid

    class Meta:
        ordering = ['last_name']
