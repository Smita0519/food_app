from django.urls import path,include
from . import views

urlpatterns = [

    path('view/',views.viewIngredients,name="viewIngredients"),
    # path('add/',views.addIngredients,name="addIngredients"),
    path('recipe/',views.recipes,name="recipeIngredients"),


]