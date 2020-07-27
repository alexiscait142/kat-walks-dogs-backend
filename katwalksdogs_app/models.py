from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=30)
    review = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)