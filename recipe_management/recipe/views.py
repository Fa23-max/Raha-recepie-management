from rest_framework.generics import ListAPIView ,RetrieveAPIView
from .models import Recipe 
from .serializer import Recipeserializer

class ListRecipe(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer

class DetailRecipe(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer


    

