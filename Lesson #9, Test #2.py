def cook_book_mader(file_name):
    with open(file_name) as cook_book_mader_file:
        cook_book = {}
        for line in cook_book_mader_file:
            ingredients_for_book = []
            name_dish = line.strip()
            for ingredients in range(int(cook_book_mader_file.readline())):
                ingredient = cook_book_mader_file.readline()

                ingredients_for_book.append({'ingredient_name': ingredient.split('|')[0], 'quantity': ingredient.split('|')[1], 'measure': ingredient.split('|')[2].strip()})
            cook_book[name_dish] = ingredients_for_book
            cook_book_mader_file.readline()

        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_book_mader('Coook_Book.txt')
    menu = {}
    for cook_book_ingredients in dishes:
        cook_book.get(cook_book_ingredients)
        for cook_book_ingredient in cook_book.get(cook_book_ingredients):
            menu[cook_book_ingredient.get('ingredient_name')] = {'measure': cook_book_ingredient['measure']  , 'quantity': int(cook_book_ingredient['quantity']) * person_count }

    return menu


print(get_shop_list_by_dishes(['Omelette'], 2))