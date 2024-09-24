from django.db import models
from django.core.validators import RegexValidator
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Название')
    description = models.TextField(blank=True, verbose_name = 'Описание блюда')
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Цена(в рублях)')
    image = models.ImageField(upload_to = '', blank=True, verbose_name = 'Картинка')
    is_available = models.BooleanField(default=True, verbose_name = 'В наличии')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name
    
