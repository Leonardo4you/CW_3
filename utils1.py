import datetime
import json

from settings import PATH_WITH_FIXTURES


def get_all_operations(path: str) -> list[dict]:
    with open(path, 'r', encoding='utf8') as file:
        return json.load(file)


"""Отсортировали по выполненым (executed) операциям """


def get_executed_operations(operations: list[dict]) -> list[dict]:
    executed_operations = list()
    for operation in operations:
        if operation.get('state') == "Executed":
            executed_operations.append(operation)
    return executed_operations


"""Сортировка по дате и выделение 5ти транзакций"""


def get_newer_five_operations(executed_operations: list[dict]) -> list[dict]:
    return list(sorted(executed_operations, key=lambda operation: operation['date'], reverse=True))[:5]


"""Приведение даты к виду dd.mm.yyyy"""


def convert_date(date: str) -> str:
    date_ = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.datetime.strftime(date_, '%d.%m.%Y')


"""Обработка строчки счета и карты"""


def convert_payment_info(info: str) -> str:
    if info.startswith('Счет'):
        return f"{info.split()[0]} **{info.split()[-1][-4:]}"
    return f'{info.split()[0]} {info.split()[-1][:4]} {info.split()[-1][4:6]}** **** {info.split()[-1][-4:]}'


"""Валидация вывода"""


def get_validate_data(operation: dict) -> str:
    date = convert_date(operation['date'])
    from_ = convert_payment_info(operation['from']) if operation.get('from') else ''
    to_ = convert_payment_info(operation['to'])
    amount = operation["operationAmount"]["amount"]
    currency = operation["operationAmount"]["currency"]["name"]
    return f'{date} {operation["description"]}' \
           f'{from_} -> {to_}' \
           f'{amount} {currency}'


operations = get_all_operations(PATH_WITH_FIXTURES)
ex_operations = get_executed_operations(operations)
five_operations = get_newer_five_operations(ex_operations)
print(json.dumps(five_operations, indent=2, ensure_ascii=False))
for operation in five_operations:
    if operation:
        print(get_validate_data(operation))
