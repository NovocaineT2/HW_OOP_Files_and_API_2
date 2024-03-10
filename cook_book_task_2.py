def create_cook_book(file_name):
    cook_book = {}
    with open (file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    i = 0
    while i < len(lines):
        dish_name = lines[i].strip()
        ingredient_count = int(lines[i+1].strip())
        i += 2
        
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_info = lines[i].strip().split(' | ')
            ingredient = {
                'ingredient_name': ingredient_info[0],
                'quantity': int(ingredient_info[1]),
                'measure': ingredient_info[2]
            }
            ingredients.append(ingredient)
            i += 1
        
        cook_book[dish_name] = ingredients
        i += 1
    
    return cook_book

file_name = 'recipes.txt'
cook_book = create_cook_book(file_name)
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'quantity' : quantity, 'measure' : measure}
            else:
                shop_list[ingredient_name]['quantity'] += quantity
    return shop_list
grossery = get_shop_list_by_dishes(['Фахитос'], 10)
print(grossery)
