from django.db import models

# Create your models here.
class Pet(models.Model):
    name=models.CharField(max_length=150 , default = "")
    age=models.IntegerField(default = 0)
    available=models.BooleanField(default = True)
    image=models.ImageField(upload_to='images/')
    price=models.DecimalField(max_digits = 5 , decimal_places = 2)

    def __str__(self):
        return self.name
