from django.db import models


# Модель Mobile с полем slug
class Mobile(models.Model):
    id_phone = models.IntegerField()
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    image = models.CharField(max_length=250)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=250)
