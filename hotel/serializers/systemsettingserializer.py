from rest_framework import serializers
from hotel.models.systemsettingmodel import SystemSetting

class SystemSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SystemSetting
        fields = ('meta_key', 'meta_value')