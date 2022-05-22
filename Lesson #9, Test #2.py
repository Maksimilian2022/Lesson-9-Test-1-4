documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def people():
    number_document = input('Введите номер документа ')
    for number in documents:
        if number.get("number") == number_document:
            return number.get("name")


def shelf():
    number_directories = input('Введите номер документа ')
    for number in directories:
        for numbers in directories.get(number):
            if numbers == number_directories:
                print('Номер полки:', number)

    else:
        print('Нет такого номера', number)

    return ' '

def list_documents():
    for conclusion in documents:
        for printed_list in conclusion:
            print (conclusion.get(printed_list), end =' ')
        print(';')
    return ' '


if "1" in directories:
    directories.get("1").append("1414"), directories
    #print(directories)



def add():
    type, number, name, number_directories = map(str, input('Введите тип, номер, имя,  полку: ').split(","))
    new_dict = {"type": type, "number": number, "name": name}
    documents.append(new_dict)
    if number_directories in directories.keys():
        directories.get(number_directories).append(number)
        print('Такая полка есть')
    else:
        directories[number_directories] = [number]
        print("Такой полки не было, но мы её успешно создали")
    print(directories.keys())
    return directories, documents



def function_call():
    command_name = input('Введите команду ')
    if command_name == 'p':
        print(people())
    elif command_name == 's':
        print(shelf())
    elif command_name == 'l':
        print(list_documents())
    elif command_name == 'a':
        print(add())
function_call()