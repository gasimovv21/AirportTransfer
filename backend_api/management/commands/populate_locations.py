from django.core.management.base import BaseCommand
from cars.models import Location

class Command(BaseCommand):
    help = 'Populate locations in the database'

    def handle(self, *args, **options):
        locations = [
        'Kemer',
        'Tekirova',
        'Çamyuva',
        'Kiriş',
        'Göynük',
        'Beldibi',
        'City Center',
        'Belek',
        'Kundu',
        'Side',
        'Manavgat',
        'Avsallar',
        'Alanya',
        'Kas',
        'Fethiye',
        'Marmaris',
        'Bodrum',
        'Didim',
        'Kuşadası',
        'Cesme',
    ]

        for location_name in locations:
            Location.objects.create(name=location_name)

        self.stdout.write(self.style.SUCCESS('Successfully populated locations'))
