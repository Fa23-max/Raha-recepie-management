from django.urls import path
from . import views


urlpatterns = [
    path('recipes/',views.ListRecipe.as_view(),name='recipe'),
    # path('recipes/<category_slug>/',views.ListRecipe.as_view(),name='recipe'),
    path('recipes/<int:pk>/',views.DetailRecipe.as_view(),name='DetailRecipe'),

        
        
       



]   
