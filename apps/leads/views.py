from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Lead
from .serializers import LeadSerializer
from .permissions import IsOwnerOrAssigned


class LeadViewSet(ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAssigned]

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(
            models.Q(owner=user) | models.Q(assigned_to=user)
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
