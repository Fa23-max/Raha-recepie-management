from .models import Recipe
from rest_framework import serializers

class Recipeserializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


