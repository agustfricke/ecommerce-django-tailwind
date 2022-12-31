from django.db import models

class Newsletter(models.Model):
    email = models.EmailField(unique=True, max_length=100)

    def __str__(self):
        return self.email

class ContentNewsLetter(models.Model):
    content = models.CharField(max_length=100)
