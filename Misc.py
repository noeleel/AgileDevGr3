from Groceries import *
from Recipes import *
import numpy as np
import pandas as pd
from scipy.optimize import minimize

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


def parse_recipes():
    """
    recettes.txt : a txt file containing the name of the recipes between three ### and
    below each recipes, the ingredients with their factors
    Later, it has to be replace by the SQL database
    """
    f_recipes = open("recettes.txt","r")
    lines_recipes = f_recipes.readlines()    
    Recipes = []
    Recipe = []
    for x in lines_recipes:
        if not x.isspace():
            if '#' in x:
                if len(Recipe) > 0 :
                    Recipes += [Recipe]
                    Recipe = []
                name = x.split('###')[1]
                Recipe += [name.strip()]
            else :
                Recipe += [x.lower().strip()]
    Recipes.pop(0)
    return Recipes

def read_ingredients():
    """
    Ingredients.csv : a csv file containing five columns : Aliment	QTT	Prot	Glu	Lip	cal
    """
    f_ingredients = "Ingredients.csv"
    lines_ingredients = pd.read_csv(f_ingredients)
    ingredients_size = len(lines_ingredients)
    Ingredients = []
    for i in range(ingredients_size):
        name = lines_ingredients['Aliment'][i].lower()
        calories = float(lines_ingredients['cal'][i])
        weight = lines_ingredients['QTT'][i]
        nutritional_values = {'Protein' : float(lines_ingredients['Prot'][i]),
                              'Carbohydrate' : float(lines_ingredients['Glu'][i]),
                                'Fat' : float(lines_ingredients['Lip'][i])}
        # In the nutriotinal_values List, everything related to vitamins will be added here
        Ingredient = Grocery(name, calories, weight, nutritional_values)
        Ingredients += [Ingredient]
    return Ingredients

def read_recipes():
    Recipes_parsed = parse_recipes()
    Recipes = []
    Ingredients = read_ingredients()
    for x in Recipes_parsed:
        Len_recipe = len(x)
        name = x[0].strip()
        calories = 0.0
        nutritional_values = {'Protein' : 0.0,
                              'Carbohydrate' : 0.0,
                                'Fat' : 0.0}
        List = []
        QTT = []
        for i in range(1,Len_recipe):
            for y in Ingredients:
                if x[i].split(' ')[1].strip().lower() == y.Name.strip().lower():
                    calories += float(y.calories)
                    nutritional_values['Protein'] +=  float(y.nutritional_values['Protein'])
                    nutritional_values['Carbohydrate'] +=  float(y.nutritional_values['Carbohydrate'])
                    nutritional_values['Fat'] +=  float(y.nutritional_values['Fat'])
                    if len(x[i].split(' '))>1: 
                        List+= [y]
                        QTT += [str(x[i].split(' ')[0].strip().lower())]
                    else: 
                        List+= [y]
                        QTT += ['1u']
        Recipe_o = Recipe(name, len(List), calories, nutritional_values, List, QTT)
        Recipes += [Recipe_o]
    return Recipes
    

def optimisation_lineaire_past(recipes, kg_per_day, basal_metabolism = 1500):
    """
        Input : recipes, a list-typed object containing all the recipes known by the program
        Principle : Compute the number of calories per recipes until this number gets
        between basal_metabolism and calories_per_day.
        Output : List, a list-typed object containing the list of groceries for the week.
    """
    sum_calories = 0
    Calories_for_day = []
    counter = 0
    calories_per_day = ((13.7516 + 9.5634)/2) * kg_per_day + basal_metabolism + 300
    while sum_calories < calories_per_day and counter < 3:
        for i in range(len(recipes)):
            if sum_calories < calories_per_day \
            and counter < 3 and len(recipes[i].Ingredients) == recipes[i].NumberIngredients \
            and recipes[i].NumberIngredients > 0:
                sum_calories += recipes[i].calories
                Calories_for_day = Calories_for_day + [recipes[i]]
                counter+=1
    List = [Calories_for_day,
            Calories_for_day,
            Calories_for_day,
            Calories_for_day,
            Calories_for_day,
            Calories_for_day,
            Calories_for_day]
    return np.array(List)

def function_to_minimize(X, P,L, C, G):
    f = (X[0] + X[4] - P)**2 + (X[1] + X[5] - G)**2 + (X[2] + X[6] - L)**2 + (X[3] + X[7] - P)**2
    return f

def Array_to_list(Array):
    List = []
    Array = Array.flatten()
    for x in Array:
        List +=[x]
    return List
    
def minimizing(X, P,L, C, G):
    X = np.array(X)
    res = minimize(function_to_minimize, X, (P, L, C, G))
    minimum = res.x
    L_minimum = Array_to_list(minimum)
    return L_minimum

def check_is_not_in_list(List, obj):
    if len(List) < 1:
        return -1
    else:
        for x in List:
            if x==obj:
                return 0
            else:
                return -1
    return -1

def optimisation_lineaire(recipes, kg_per_day, basal_metabolism = 1500):
    List = []
    calories_per_day = ((13.7516 + 9.5634)/2) * kg_per_day + basal_metabolism + 300
    carbohydrates = (50/100) * calories_per_day
    fat = (35/100) * calories_per_day
    proteins = (15/100) * calories_per_day
    X = []
    # Creation of the pairs of recipes
    for i in range(len(recipes)):
        for j in range(len(recipes)):
            if i!=j:
                X += [[recipes[i].nutritional_values['Protein'], recipes[i].nutritional_values['Carbohydrate'],recipes[i].nutritional_values['Fat'], recipes[i].calories,recipes[j].nutritional_values['Protein'], recipes[j].nutritional_values['Carbohydrate'],recipes[j].nutritional_values['Fat'], recipes[j].calories, (i,j)]]
    # Running the minization function on the pairs
    Minimized = []
    for i in range(len(X)):
        Val = X[i][0:8]
        Minimized +=[minimizing(Val, proteins, fat, calories_per_day, carbohydrates)]
    # Making the recipes for each day
    while len(List) < 7:
        Recipes_for_day = []
        while len(Recipes_for_day)<3:
            mini = min(Minimized)
            idx = Minimized.index(mini)
            Minimized.pop(idx)
            idx_recipe1 = X[idx][8][0]
            idx_recipe2 = X[idx][8][1]
            recipe1 = recipes[idx_recipe1]
            recipe2 = recipes[idx_recipe2]
            # Check any if the recipes is not redundant
            flag1 = check_is_not_in_list(Recipes_for_day,recipe1)
            if flag1 == -1 and len(Recipes_for_day) < 3:
                Recipes_for_day +=[recipe1]
            else:
                flag2 = check_is_not_in_list(Recipes_for_day,recipe2)
                if flag2 == -1 and len(Recipes_for_day) < 3:
                    Recipes_for_day +=[recipe2]
                elif flag1 == 0 and flag2 == 0:
                    Recipes_for_day+=[recipe1]
        List +=[Recipes_for_day]
    return np.array(List)
    
def print_List(Array):
    Array = Array.flatten()
    Array = Array[0:10]
    for x in Array:
        print('\n')
        print(x.show())
        print('\n')