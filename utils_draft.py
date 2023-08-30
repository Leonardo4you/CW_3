import json

#функция чтения файла
def load_operations(path_to_file):
    with open(path_to_file, "r", encoding='utf8') as file:
        return json.load(file)

# print(load_operations("operations.json"))



#функция преобразования даты
def transform_data(date):
    date = date.split("T")[0].split("-")
    return f"{date[2]}.{date[1]}.{date[0]}"

# print(transform_data('2019-08-26T10:50:58.294041'))



#функция маскировки счета
def mask_check(check):
    check = check.split()
    return f"{check[0]} **{check[-1][-4:]}"

# print(mask_check("Счет 64686473678894779589"))



#функция маскировки карты
def card(card):
    card = card.split()
    return f"{card[0]} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}"

# print(card('Visa Classic 6831982476737658'))

#сортировка по executed и вывод 5 последних
def filter_sort_operations(operations):
    executed_operations = [operation for operation in operations if operation.get("state") == "EXECUTED"]
    sorted_operations = sorted(executed_operations, key=lambda operation: operation['date'], reverse=True)
    return sorted_operations

