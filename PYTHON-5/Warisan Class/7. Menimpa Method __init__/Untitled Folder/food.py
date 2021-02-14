from menu_item import MenuItem

class Food(MenuItem):
    # Definisikan method __init__ 
    
    
    
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kkal)'
    
    def calorie_info(self):
        print('kkal: ' + str(self.calorie_count))
