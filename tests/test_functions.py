from utils.functions import load_operations, sorting_operations, filtering_operations, masking_the_card_number, output_of_operations, main


#def test_load_operations():

    #assert load_operations([{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}]) == [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}]


def test_sorting_operations():

    assert sorting_operations([{"id": 441945886, "date": "2019-08-26T10:50:58.294041"}, {"id": 939719570, "date": "2018-06-30T02:08:58.425572"}, {"id": 41428829, "date": "2019-07-03T18:35:29.512364"}]) == [{"id": 441945886, "date": "2019-08-26T10:50:58.294041"}, {"id": 41428829, "date": "2019-07-03T18:35:29.512364"}, {"id": 939719570,"date": "2018-06-30T02:08:58.425572"}]
    assert sorting_operations([{"id": 441945886}]) == []
    assert sorting_operations([{"id": 441945886, "date": ""}]) == []
    assert sorting_operations([]) == []


def test_filtering_operations():

    assert filtering_operations([{"id": 441945886, "state": "EXECUTED"}, {"id": 939719570, "state": "EXECUTED"}, {"id": 41428829, "state": "EXECUTED"}, {"id": 27192367, "state":"CANCELED"}]) == [{"id": 441945886, "state": "EXECUTED"}, {"id": 939719570, "state": "EXECUTED"}, {"id": 41428829, "state": "EXECUTED"}]


def test_masking_the_card_number():

    assert masking_the_card_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert masking_the_card_number("Счет 58518872592028002662") == "Счет **2662"


def test_output_of_operations():

    assert output_of_operations({"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}) == None
