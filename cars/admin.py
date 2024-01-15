from django.contrib import admin

from .models import Feature, Photo, Car


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'icon',
    )
    search_fields = (
        'id',
        'name',
        'icon',
    )
    list_filter = (
        'id',
        'name',
        'icon',
    )
    empty_value_display = '-empty-'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
    )
    search_fields = (
        'id',
        'image',
    )
    list_filter = (
        'id',
        'image',
    )
    empty_value_display = '-empty-'


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'price',
        'availability_date',
        'display_features',
    )
    search_fields = (
        'id',
        'name',
        'category',
        'price',
        'availability_date',
        'features__name',
    )
    list_filter = (
        'id',
        'name',
        'category',
        'price',
        'availability_date',
        'features',
    )
    empty_value_display = '-empty-'

    def display_features(self, obj):
        return ", ".join([feature.name for feature in obj.features.all()])
    
    display_features.short_description = 'Arabanin ozel hizmetleri'