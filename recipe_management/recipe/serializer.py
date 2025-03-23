from .models import Recipe
from rest_framework import serializers
from django.contrib.auth.models import User

class Recipeserializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
