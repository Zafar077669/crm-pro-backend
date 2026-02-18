from rest_framework import serializers
from .models import Deal


class DealSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Deal
        fields = [
            'id',
            'lead',
            'amount',
            'currency',
            'stage',
            'owner',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')
