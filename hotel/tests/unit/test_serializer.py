from django.test import TestCase

from hotel.serializers.systemsettingserializer import SystemSettingSerializer
from hotel.serializers.visitorserializer import VisitorSaveSerializer

class BookingSaveSerializerTestCase(TestCase):

    def test_booking_save_serializer(self):
        serializer = SystemSettingSerializer(data={'meta_key': 'test_setting_key', 'meta_value': True})
        is_serializer_validated = serializer.is_valid()
        self.assertEqual(is_serializer_validated, True)


class VisitorSaveSerializerTestCase(TestCase):

    def test_visitor_save_serializer(self):
        serializer = VisitorSaveSerializer(data={'gsm':'5554443322', 'email': 'test@test.com', 'firstname': 'John', 'lastname': 'Doe'})
        is_serializer_validated = serializer.is_valid()
        self.assertEqual(is_serializer_validated, True)        