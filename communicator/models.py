from django.db import models


class Device(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
