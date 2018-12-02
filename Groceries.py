class Grocery():
    def __init__(self, name, calories, weight, nutritional_values):
        super().__init__()
        self.Name = name
        self.calories = calories
        self.weight = weight
        self.nutritional_values = nutritional_values # List of dictionnary