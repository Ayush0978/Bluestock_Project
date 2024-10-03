from rest_framework import viewsets
from .models import IPO
from .serializers import IPOSerializer

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
