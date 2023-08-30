import pytest

from utils_draft import load_operations, filter_sort_operations


def test_load_operations():
    assert isinstance(load_operations('operations.json'), list)
    with pytest.raises(FileNotFoundError):
        load_operations('sadsad')


def test_filter_sort_operations(valid_data, one_executed_op):
    assert len(filter_sort_operations(valid_data)) == 4
    assert filter_sort_operations(one_executed_op) == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]

