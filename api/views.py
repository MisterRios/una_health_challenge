from rest_framework.generics import ListAPIView, RetrieveAPIView

from glucose_levels.models import GlucoseLevel
from glucose_levels.serializers import GlucoseLevelSerializer


class LevelsListView(ListAPIView):
    model = GlucoseLevel
    serializer_class = GlucoseLevel
    queryset = GlucoseLevel.objects.all()


# class LevelsItemView(RetrieveAPIView):
#     model = GlucoseLevel
#     serializer_class = GlucoseLevel
#     queryset = GlucoseLevel.objects.all()
