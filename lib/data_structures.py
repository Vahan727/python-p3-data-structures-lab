spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_foods_names = []
    for index in range(3):
        spicy_foods_names.append(spicy_foods[index]["name"])
    return spicy_foods_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spicy_foods[index] for index in range(3) if spicy_foods[index]["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods: 
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
        elif food["cuisine"] == cuisine:
            return food
        elif food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    [print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}') for food in spicy_foods if food["heat_level"] > 5]
    

def get_average_heat_level(spicy_foods):
    average_heat_level = (spicy_foods[0]["heat_level"] + spicy_foods[1]["heat_level"] + spicy_foods[2]["heat_level"]) / 3
    return average_heat_level
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
