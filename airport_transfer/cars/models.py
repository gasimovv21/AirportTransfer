from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

class Car(models.Model):
    CATEGORY_CHOICES = [
        ('Luxury', 'Luxury'),
        ('Econom', 'Econom'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_date = models.DateField()
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
