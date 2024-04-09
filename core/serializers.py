from rest_framework import serializers
from .models import Activity
# accounts/serializers.py (If you have a separate accounts app)
from django.contrib.auth.models import User
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password'] 

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
