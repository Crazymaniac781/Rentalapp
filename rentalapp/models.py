from django.db import models

class RentalHome(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.location}"
