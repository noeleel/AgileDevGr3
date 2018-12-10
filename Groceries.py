class Grocery():
    def __init__(self, name, calories, weight, nutritional_values):
        super().__init__()
        self.Name = name
        self.calories = calories
        self.weight = weight
        self.nutritional_values = nutritional_values # List of dictionnary
        
    def show(self):
        print('Grocery Name : ' + str(self.Name))
        print('Calories : ' + str(self.calories))
        print('Weight : ' + str(self.weight))
        print('Nutritional values : ')
        print('Proteins : ' + str(self.nutritional_values['Protein']))
        print('Carbohydrate : ' + str(self.nutritional_values['Carbohydrate']))
        print('Fat : '+ str(self.nutritional_values['Fat']))