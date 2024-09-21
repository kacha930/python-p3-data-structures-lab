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
    return[food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_level_str = '🌶' * heat_level  
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_str}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    matching_cuisine = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return matching_cuisine[0] if matching_cuisine else None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_level_str = '🌶' * heat_level
        if food["heat_level"] > 5:
             print(f"{name} ({cuisine}) | Heat Level: {heat_level_str}")

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    
    number_of_spfoods = len(spicy_foods)
    
    average_heat = total_heat_level // number_of_spfoods
    return average_heat
    
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods






    