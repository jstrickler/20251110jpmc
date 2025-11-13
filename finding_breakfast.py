
valid_foods = ['eggs', 'waffles', 'idli', 'roast beef', 'sweet-and-sour tofu']

food_list = open('DATA/breakfast.txt').read().splitlines()

print(f"{valid_foods = }")
print(f"{food_list = }")

valid_set = set(valid_foods)
food_set = set(food_list)
print(f"{food_set = }")


common_food = valid_set & food_set
print(f"{common_food = }")

