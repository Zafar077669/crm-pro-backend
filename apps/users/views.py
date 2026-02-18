from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class MeView(APIView):
    def get(self, request):
        return Response({
            "id": request.user.id,
            "email": request.user.email,
            "full_name": request.user.full_name,
        })
