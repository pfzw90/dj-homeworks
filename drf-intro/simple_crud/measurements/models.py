from django.db import models


class Common(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Project(Common):

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Measurement(Common):

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='uploaded_images/')
