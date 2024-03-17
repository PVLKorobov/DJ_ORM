from django.db import models
from django.conf import settings

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50)