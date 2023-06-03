from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'favorite_poems', 'image', 'is_owner'
        ]
