from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=20)
    rating=models.DecimalField(max_digits=5,decimal_places=1)


    def __str__(self):
        return self.name
