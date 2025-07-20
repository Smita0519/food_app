from django.shortcuts import render,redirect
import requests
from .models import Ingredient
# Create your views here.
def viewIngredients(req):
    ingredient=Ingredient.objects.all()
    return render(req,'fridge/fridge.html',{'ingredient':ingredient})

def addIngredients(requests):
    recipes=[]
    if requests.method=='POST':
        print("post")
        name = requests.POST.get('name')
        Ingredient.objects.create(name=name)
        return redirect('viewIngredients')
    return render(requests,'add/add.html')

def recipes(request) :
    recipes=[]
    for ingredient in Ingredient.objects.values_list('name', flat=True):
        
        result = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={ingredient}')
        if result.status_code==200:
            meals = result.json().get('meals')
            if meals:
                recipes.append(meals)
        
        # print(recipes)
    return render(request, 'recipe/recipe.html', {'recipes': recipes})