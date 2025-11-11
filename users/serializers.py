from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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


class CustomObtainTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['full_name'] = user.full_name
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = {
            'id' : self.user.id,
            'email': self.user.id,
            'full_name': self.user.full_name,
        }

        return data
            