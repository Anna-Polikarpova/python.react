from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('main:detail', args=[self.id])


