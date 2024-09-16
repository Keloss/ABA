from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    image = models.ImageField(upload_to = '', blank=True)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        pass