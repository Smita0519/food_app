from django.shortcuts import render,redirect
import requests as http_request
from .models import Ingredient
# Create your views here.
def viewIngredients(request):
    if request.method == 'POST':
        action_type = request.POST.get('action_type')

        if action_type == 'add':
            name = request.POST.get('name')
            if name and not Ingredient.objects.filter(name__iexact=name).exists():

                Ingredient.objects.create(name=name.lower())
            return redirect('viewIngredients')  # reload page

        elif action_type == 'search':
            button_clicked=request.POST.get('action')
            if button_clicked== 'find_recipe':
                return specificRecipe(request)
            else:
                return removeIngredients(request)

    # GET request: show ingredients
    ingredient = Ingredient.objects.all()
    return render(request, 'fridge/fridge.html', {'ingredient': ingredient})




def specificRecipe(requests):
    recipes=[]
    if requests.method=='POST':
        nameOfIngredients = requests.POST.getlist('fridge_item')
        # print(nameOfIngredients)
        for ingredient in nameOfIngredients:
            # print(ingredient)
            #Ingredient.objects.get(name=ingredient)
            #ingredient.delete()
            result = http_request.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={ingredient}')
            # print(result)
            if result.status_code==200:
                    meals = result.json().get('meals')
                    if meals:
                        recipes.append(meals)
    return render(requests, 'recipe/recipe.html', {'recipes': recipes})

def removeIngredients(request):
    remove_list=request.POST.getlist('fridge_item')
    for remove_ingredient in remove_list:
        print("start:==",Ingredient.objects.all())
        print(remove_ingredient)
        Ingredient.objects.filter(name=remove_ingredient).delete()
        print("end:==",Ingredient.objects.all())

    ingredient=Ingredient.objects.all()
    return render(request,'fridge/fridge.html', {'ingredient': ingredient})

def addIngredients(requests):
    recipes=[]
    if requests.method=='POST':
        
        # print("post")
        name = requests.POST.get('name')
        present_in_db=False
        all_Ingredients=list(Ingredient.objects.all())
        # print(all_Ingredients)
        for ingredient in all_Ingredients:
            if name in ingredient.name:
                present_in_db=True
        
        if present_in_db==False:
            Ingredient.objects.create(name=name)

        return redirect('viewIngredients')
    return render(requests,'add/add.html')

def recipes(request) :
    recipes=[]
    for ingredient in Ingredient.objects.values_list('name', flat=True):
        
        result = http_request.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={ingredient}')
        if result.status_code==200:
            meals = result.json().get('meals')
            if meals:
                recipes.append(meals)
        
        # print(recipes)
    return render(request, 'recipe/recipe.html', {'recipes': recipes})