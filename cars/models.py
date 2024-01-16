import os


from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Feature(models.Model):
    name = models.CharField(
        verbose_name='Araç hizmetinin ismi',
        max_length=255,
        unique=True
    )
    icon = models.FileField(
        verbose_name='Icon',
        upload_to='icons/',  # Папка для сохранения загруженных файлов
        blank=True,
        null=True,
    )


    def save(self, *args, **kwargs):
        # Если поле icon не было явно установлено, устанавливаем его равным значению поля name
        if not self.icon:
            self.icon = f'icons/{self.name}.png'
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Araç hizmeti'
        verbose_name_plural = 'Araç hizmetleri'


class Photo(models.Model):
    image = models.ImageField(
        upload_to='car_images_album/', 
        verbose_name='Araç resmi',
        null=True, 
        blank=False
    )


    def __str__(self):
        return os.path.basename(str(self.image))


    class Meta:
        ordering = ['id']
        verbose_name = 'Araçlarin albüm resimi'
        verbose_name_plural = 'Araçin albüm resimleri'


    # def clean_existing_feature(self):
    #   """
    #   Checking the existing feature.
    #   """
    #     existing_feature = Feature.objects.filter(name=self.name).first()
    #     if existing_feature:
    #         raise ValidationError('Böyle bir hizmet sistemde zaten mevcut!')
        
    
    # def clean(self):
    #     super().clean()
    #     self.clean_existing_feature()

    

class Car(models.Model):
    CATEGORY_CHOICES = [
        ('Luxury', 'Luxury'),
        ('Econom', 'Econom'),
    ]

    name = models.CharField(
        verbose_name='Araçin Ismi',
        max_length=255,
        blank=False
    )
    category = models.CharField(
        verbose_name='Araçin kategorisi',
        max_length=100,
        choices=CATEGORY_CHOICES,
        blank=False
    )
    price = models.DecimalField(
        verbose_name='Araçin fiyati',
        max_digits=10,
        decimal_places=2,
        blank=False
    )
    availability_date = models.DateField(
        verbose_name='Araçin mevcut tarihi',
        blank=False
    )
    features = models.ManyToManyField(
        Feature,
        verbose_name='Araçin ozel hizmeti',
        blank=False
    )
    image = models.ImageField(
        upload_to='car_images/', 
        verbose_name='Araçin resmi',
        null=True, 
        blank=False
    )
    photo_album = models.ManyToManyField(
        'Photo',
        verbose_name='Araçin foto albümü',
        blank=True
    )


    def __str__(self):
        return self.name


    class Meta:
        ordering = ['id']
        verbose_name = 'Araç'
        verbose_name_plural = 'Araçlar'


    def clean_availability_date(self):
        """
        Checking data in future not in past.
        """
        if self.availability_date < timezone.now().date():
            raise ValidationError("Kullanılabilirlik tarihi gelecekte olmalıdır.")


    # FOR FUTURE EACH CAR MUST HAVE UNIQE CAR_NUMBER Ex: 90-EQ-200, 10-AB-123 and etc.
    # def clean_existing_car(self):
    #     existing_cars = Car.objects.filter(name=self.name, category=self.category)
        
    #     for car in existing_cars:
    #         if car.price == self.price:
    #             raise ValidationError(f"Böyle bir fiyata artik araba var. {self.price}")


    def clean(self):
        super().clean()
        self.clean_availability_date()