def cook_book_mader(file_name, second_file):
    cook_book_dictionary = {}
    name_of_dish = []
    i = -1
    ingredients = []
    a = -1
    for line in open(file_name):
        if line.strip().replace(" ", "a").isalpha():
            cook_book_dictionary[line.strip()] = []
            name_of_dish.append(line.strip())
            i += 1
        elif "|" in line:
            a += 1
            dict_of_ingredient = {'ingredient_name': line.split('|')[0], 'quantity': line.split('|')[1], 'measure': line.split('|')[2]}
            ingredients.append(dict_of_ingredient)
            cook_book_dictionary[name_of_dish[i]].append(ingredients[a])
    with open(second_file, 'w') as file:
        file.write(str(cook_book_dictionary))

    return cook_book_dictionary

#cook_book_mader('Coook_Book.txt')
cook_book_mader('Coook_Book.txt', 'Cook_book_dict.txt')















