from django.utils.timezone import now
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'name',
            'email',
            'password',
            'access_type',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'modified_at': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        # ya no popeamos modified_at aquí
        user = User(**validated_data)
        user.set_password(password)
        user.modified_at = now()   # 🔥 Aquí le das un valor válido
        user.save()
        return user



        
        
        
        