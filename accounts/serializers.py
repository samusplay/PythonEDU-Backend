from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            'user_id',
            'name',
            'email',
            'password',
            'created_at',
            'access_type',
        )
        extra_kwargs={
            'password':{'write_only':True} #para no exponer la contraseña
        }

        def create(self,validated_data):
            password=validated_data.pop('password')
            user=User(**validated_data)
            user.set_password(password)
            user.save()
            return user
        
        
        
        