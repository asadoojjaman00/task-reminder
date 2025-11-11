from rest_framework import serializers

from .models import User



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password']
    
    def create(self, validated_data):
        return User.objects.create_user(
            full_name = validated_data['full_name'],
            email = validated_data['email'],
            password = validated_data['password'],
            is_active = True
        )
    
from rest_framework import serializers

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

            