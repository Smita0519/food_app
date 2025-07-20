from django.urls import path,include
from . import views

app_name = 'fridge'

urlpatterns = [

    path('view/',views.viewIngredients,name="viewIngredients"),
    path('add/',views.addIngredients,name="AddIngredients"),
    path('recipe/',views.recipes,name="recipeIngredients"),


]