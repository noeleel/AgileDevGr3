from Groceries import *
from Recipes import *

def str_to_float(string):
    try:
        return float(string)
    except:
        return -1

List_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def read_recipes(file):
    f_ingredients = open("ingredients.txt", "r")
    f_recipes = open("recettes.txt","r")
    lines_recipes = f_recipes.readlines()
    lines_ingredients = f_ingredients.readlines()
    for x in lines_recipes:
        for y in lines_ingredients:
            a = 0
        
    return 1
    
def optimisation_lineaire(recipes, calories_per_day, basal_metabolism):
    """
        Input : recipes, a list-typed object containing all the recipes known by the program
        Principle : Compute the number of calories per recipes until this number gets
        between basal_metabolism and calories_per_day.
        Output : List, a list-typed object containing the list of groceries for the week.
    """
    sum_calories = 0
    Calories_for_day = []
    i = 0
    while sum_calories < calories_per_day:
        for i in  range(len(recipes)):
            if sum_calories + recipes[i].calories < calories_per_day:
                sum_calories += recipes[i].calories
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
    