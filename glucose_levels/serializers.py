from rest_framework import serializers

from glucose_levels.models import GlucoseLevel


class GlucoseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseLevel
        fields = [
            "id",
            "user",
            "device_timestamp",
            "glucose_value_trend",
            "glucose_scan",
        ]
