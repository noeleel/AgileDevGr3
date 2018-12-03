                    
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