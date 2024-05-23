from django.db import models

# Create your models here.
class Proizvod(models.Model):
    ime = models.CharField(max_length=100)
    deskripcija = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    kolicina = models.IntegerField()
    napravljen = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='product_images/', blank=True, null=True)