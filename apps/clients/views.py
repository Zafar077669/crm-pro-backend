from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .serializers import ClientSerializer
from .permissions import IsOwner


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        # user faqat o‘z clientlarini ko‘radi
        return Client.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # owner avtomatik belgilanadi
        serializer.save(owner=self.request.user)
