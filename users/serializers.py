from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
User=get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','email','password','confirm_password','role','is_active']
        read_only_fields=['role']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"message":"Password's didn't match"})
        return attrs
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        username=validated_data['email']
        user = User.objects.create_user(
            username=username,
            email=validated_data['email'],
            password=validated_data['password']
        )

        user.role = 'viewer'  # 🔥 force role
        user.save()

        return user
    

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)

    def validate(self, attrs):
        user=authenticate(
            username=attrs['email'],
            password=attrs['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")
        attrs['user']=user
        return attrs

class RoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['role']