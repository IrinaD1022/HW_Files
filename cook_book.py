import os
file_path = os.path.join(os.getcwd(), 'recipes.txt')
cook_book = {}

with open(file_path,'r',encoding='utf-8') as f:
    for line in f:
        dish_name = line.strip()
        ingridients_count = int(f.readline().strip())
        ingridients = []
        for idx in range(ingridients_count):
            ingridient = f.readline().strip().split(' | ')
            ingridients.append({
                'ingredient_name': ingridient[0],
                'quantity': int(ingridient[1]),
                'measure': ingridient[2]
            })
        cook_book[dish_name] = ingridients
        f.readline()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in cook_book:
        if dish in dishes:
            for  item in cook_book[dish]:
                #print(item)
                if item['ingredient_name'] in shop_list.keys():
                    shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count
                else:
                    shop_list[item['ingredient_name']] = {
                       'measure': item['measure'],
                       'quantity': item['quantity'] * person_count
                    }
    return shop_list
    
shop = get_shop_list_by_dishes(['Омлет','Фахитос'], 3)
print('Список покупок:')
for item in shop:
    print(f'{item} - {shop[item]["quantity"]} {shop[item]["measure"]}')