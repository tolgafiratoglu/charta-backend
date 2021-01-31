from django.test import TestCase

from hotel.serializers.systemsettingserializer import SystemSettingSerializer

class BookingSaveSerializerTestCase(TestCase):

    def test_booking_save_serializer(self):
        serializer = SystemSettingSerializer(data={'meta_key': 'test_setting_key', 'meta_value': True})
        is_serializer_validated = serializer.is_valid()
        self.assertEqual(is_serializer_validated, True)