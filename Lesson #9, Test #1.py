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
        print(cook_book)
        with open('Cook_Book_dict.txt', 'w') as Cook_Book_dict:
            cook_book_str = str(cook_book)
            Cook_Book_dict.write(cook_book_str)

        return




cook_book_mader('Coook_Book.txt')















