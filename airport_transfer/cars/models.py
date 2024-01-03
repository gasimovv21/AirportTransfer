from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

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
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    
    def clean_availability_date(self):
        """
        Checking data in future not in past.
        """
        if self.availability_date < timezone.now().date():
            raise ValidationError("Kullanılabilirlik tarihi gelecekte olmalıdır.")
    
    def clean(self):
        super().clean()
        self.clean_availability_date()