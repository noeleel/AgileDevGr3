                    
class Recipe():
    def __init__(self, name, NumberIngredients, calories, nutritional_values, List, QTT):
        super().__init__()
        self.Name = name
        self.NumberIngredients = NumberIngredients
        self.calories = calories
        self.nutritional_values = nutritional_values
        self.Ingredients = List # List of dictionaries values with the 
        # name of the ingredients and the factor for this
        # ingredients
        self.QTT = QTT # How much for each ingredients
        
    def show(self):
        print('\n Recipe Name : ' + str(self.Name))
        print('Calories : ' + str(self.calories))
        print('Number of Ingredients : ' + str(self.NumberIngredients))
        print('Nutritional values : ')
        print('Proteins : ' + str(self.nutritional_values['Protein']))
        print('Carbohydrate : ' + str(self.nutritional_values['Carbohydrate']))
        print('Fat : '+ str(self.nutritional_values['Fat']))
        print('Which Ingredients? ')
        for i in range(len(self.Ingredients)):
            print('\nIngredient ' + str(i) + ' : ' + str(self.QTT[i]))
            print(self.Ingredients[i].show())