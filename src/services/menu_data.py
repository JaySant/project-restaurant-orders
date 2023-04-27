import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path) as csvfile:
            reader = csv.DictReader(csvfile)
            data = {}
            for row in reader:
                dish_name = row['dish']
                price = float(row['price'])
                quantity = int(row['recipe_amount'])
                ingredient = Ingredient(row['ingredient'])
                dish = next(
                    (dish for dish in self.dishes
                        if dish.name == dish_name),
                    None
                    )
                if dish is None:
                    dish = Dish(dish_name, price)
                    data[dish_name] = dish
                dish.add_ingredient_dependency(ingredient, quantity)
                self.dishes = data.values()
