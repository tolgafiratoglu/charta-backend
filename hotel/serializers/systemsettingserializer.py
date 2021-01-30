from rest_framework import serializers
from hotel.models.systemsettingmodel import SystemSetting

class SystemSettingRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = SystemSetting
        fields = ('meta_key', 'meta_value')