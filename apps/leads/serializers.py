from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    assigned_to = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Lead
        fields = [
            'id',
            'title',
            'description',
            'status',
            'client',
            'owner',
            'assigned_to',
            'created_at',
            'updated_at',
        ]
        read_only_fields = (
            'id',
            'owner',
            'created_at',
            'updated_at',
        )
