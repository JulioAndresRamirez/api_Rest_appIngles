from rest_framework import viewsets
from .serializers import DataSerializer, StarRatingSerializer
from .models import Data, StarRating


# Create your views here.
class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all().order_by('-fecha')
    serializer_class = DataSerializer


class StarRatingViewSet(viewsets.ModelViewSet):
    queryset = StarRating.objects.all()
    serializer_class = StarRatingSerializer
