from django.contrib import admin

from .models import Feature, Car


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'id',
        'name',
    )
    list_filter = (
        'id',
        'name',
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
    
    display_features.short_description = 'Features'