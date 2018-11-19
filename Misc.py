from Groceries import *
from Recipes import *
import pandas as pd


List_days      =  ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
List_meals     =  ["Breakfast","Lunch","Dinner"]

vals = ['1.25', '1.5', '1.75','2.1']
etiqs = ['daily activities and 30 min walk / day ', 
            '~60 min of small activities',
            '>60 min of small activities, or 30-60 min intensive activities',
            '>60min of intensive activities']



def str_to_float(string):
    try:
        return float(string)
    except:
        return 0

def max_lenght(l):
    m = 0
    for i in range (len(l)):
        for j in range(len(l[i])):
            if l[i,j].NumberIngredients>m:
                m = l[i,j].NumberIngredients
    return m



def recipes_parser(lines):
    Recipes = []
    Recipe = []
    for x in lines:
        if not x.isspace():
            if '#' in x:
                if len(Recipe) > 0 :
                    Recipes += [Recipe]
                    Recipe = []
                name = x.split('###')[1]
                Recipe += [name]
            else :
                Recipe += [x]
    return Recipes

def read_recipes():
    """
    Ingredients.csv : a csv file containing five columns : Aliment	QTT	Prot	Glu	Lip	cal
    recettes.txt : a txt file containing the name of the recipes between three ### and
    below each recipes, the ingredients with their factors
    Later, it has to be replace by the SQL database
    """
    f_ingredients = "Ingredients.csv"
    f_recipes = open("recettes.txt","r")
    lines_recipes = f_recipes.readlines()
    lines_ingredients = pd.read_csv(f_ingredients)
    ingredients_size = len(lines_ingredients)
    Ingredients = []
    for i in range(ingredients_size):
        name = lines_ingredients['Aliment'][i]
        calories = lines_ingredients['cal'][i]
        weight = lines_ingredients['QTT'][i]
        nutritional_values = [{'Protein' : lines_ingredients['Prot'][i]},
                              {'Carbohydrate' : lines_ingredients['Glu'][i]},
                                {'Fat' : lines_ingredients['Lip'][i]}] 
        # In the nutriotinal_values List, everything related to vitamins will be added here
        Ingredient = Grocery(name, calories, weight, nutritional_values)
        Ingredients += [Ingredient]
    Recipes = recipes_parser(lines_recipes)
    return Recipes
    
def optimisation_lineaire(recipes, calories_per_day, basal_metabolism):
    """
        Input : recipes, a list-typed object containing all the recipes known by the program
        Principle : Compute the number of calories per recipes until this number gets
        between basal_metabolism and calories_per_day.
        Output : List, a list-typed object containing the list of groceries for the week.
    """
    sum_calories = 0
    Calories_for_day = []
    calories_per_recipe = 800
    i = 0
    while sum_calories < calories_per_day:
        for i in  range(len(recipes)):
            if sum_calories + calories_per_recipe < calories_per_day:
                sum_calories += calories_per_recipe
                Calories_for_day = Calories_for_day + [recipes[i]]
    List = [Calories_for_day,
            Calories_for_day,
            Calories_for_day,
            Calories_for_day,
            Calories_for_day,
            Calories_for_day,
            Calories_for_day]
    return List
    
    
    [["a","aa","ab","ac"],["b","ba","bb"],["c","ca","cb","cc","cd"],["d","da","db"],["e","ea"],["f","fa"],["g","ga","gb"]]
    