from rest_framework.generics import ListAPIView, RetrieveAPIView

from glucose_levels.models import GlucoseLevel
from glucose_levels.serializers import GlucoseLevelSerializer


class LevelsListView(ListAPIView):
    model = GlucoseLevel
    serializer_class = GlucoseLevelSerializer
    filterset_fields = ["user", "device_timestamp"]
    ordering_fields = [
        "device_timestamp",
        "glucose_value_trend",
        "glucose_scan",
    ]
    queryset = GlucoseLevel.objects.all()


# class LevelsItemView(RetrieveAPIView):
#     model = GlucoseLevel
#     serializer_class = GlucoseLevelSerializer
