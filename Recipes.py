                    
class Recipe():
    def __init__(self, NumberIngredients, calories, Dictionary):
        super().__init__()
        self.NumberIngredients = NumberIngredients
        self.calories = calories
        self.Ingredients = Dictionary # List of dictionaries values with the 
        # name of the ingredients and the factor for this
        # ingredients