from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Deal
from .serializers import DealSerializer


class DealViewSet(ModelViewSet):
    serializer_class = DealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Deal.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def revenue(self, request):
        total = Deal.objects.filter(
            owner=request.user,
            stage='won'
        ).aggregate(total=Sum('amount'))['total'] or 0

        return Response({
            'total_revenue': total
        })
