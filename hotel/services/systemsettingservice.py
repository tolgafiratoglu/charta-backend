from hotel.models.systemsettingmodel import SystemSetting

class SystemSettingService():

    @classmethod
    def get_setting_value(self, meta_key):
        if SystemSetting.objects.filter(meta_key=meta_key).count() > 0:
            return SystemSetting.objects.filter(meta_key=meta_key).first().meta_value
        else:
            return False