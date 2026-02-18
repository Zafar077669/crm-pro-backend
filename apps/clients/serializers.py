from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'website',
            'status',
            'owner',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')
