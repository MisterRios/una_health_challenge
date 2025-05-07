from django.contrib.auth import get_user_model
from django.db import models


class GlucoseLevel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    device = models.CharField(max_length=255, null=False, blank=False)
    serial_number = models.UUIDField(editable=False)
    device_timestamp = models.DateTimeField()
    record_type = models.IntegerField()

    # optional in import
    glucose_value_trend = models.IntegerField(null=True, blank=True, db_comment="mg/dL")
    glucose_scan = models.IntegerField(null=True, blank=True, db_comment="mg/dL")

    # not imported intitially
    nonnumeric_rapid_acting_insulin = models.CharField(null=True, blank=True)
    rapid_acting_insulin = models.IntegerField(
        null=True, blank=True, db_comment="units"
    )
    nonnumeric_food_data = models.CharField(null=True, blank=True)
    carbohydrates = models.IntegerField(null=True, blank=True, db_comment="grams")
    carbohydrate_servings = models.IntegerField(null=True, blank=True)
    nonnumeric_slow_release_insulin = models.CharField(null=True, blank=True)
    slow_release_insulin = models.IntegerField(
        null=True, blank=True, db_comment="units"
    )
    notes = models.TextField(null=True, blank=True)
    glucose_test_strip = models.IntegerField(null=True, blank=True, db_comment="mg/dL ")
    ketone = models.IntegerField(null=True, blank=True, db_comment="mmol/L")
    mealtime_insulin = models.IntegerField(null=True, blank=True, db_comment="units")
    correction_insulin = models.IntegerField(null=True, blank=True, db_comment="units")
    user_changed_insulin = models.IntegerField(
        null=True, blank=True, db_comment="units"
    )

    def __str__(self):
        """
        Representational string for object (for example for Admin)
        """
        return f"{self.device} {self.serial_number} {self.timestamp}"
