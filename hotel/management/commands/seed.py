from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from hotel.models.systemsettingmodel import SystemSetting
from hotel.serializers.systemsettingserializer import SystemSettingSerializer

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding started'))
        initial_settings = settings.INITIAL_SETTINGS
        for key, value in initial_settings.items():
            if SystemSetting.objects.filter(meta_key=key).count() == 0:
                serializer = SystemSettingSerializer(data={"meta_key": key, "meta_value": value})
                if serializer.is_valid():
                    serializer.save()

        self.stdout.write(self.style.SUCCESS('Seeding ended'))