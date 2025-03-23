from rest_framework.generics import ListAPIView ,RetrieveAPIView ,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .models import Recipe 
from .serializer import Recipeserializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required,name='dispatch')
class ListRecipe(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer
    lookup_field = 'category'

 

@method_decorator(login_required,name='dispatch') 
class DetailRecipe(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer

