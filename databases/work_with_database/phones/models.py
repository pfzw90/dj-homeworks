from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.TextField(null=False)
    price = models.IntegerField(null=False)
    release_date = models.DateField(null=False)
    image = models.URLField(null=False)
    lte_exists = models.BooleanField(null=False, default=False)
    slug = models.SlugField(null=False)
