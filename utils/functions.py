import json
from datetime import datetime

def load_operations():

    """ Функция, которая читает файл operations.json """

    with open("operations.json", "rt", encoding="utf-8") as operations_file:

        all_operations = json.load(operations_file)

    return all_operations


def sorting_operations(operations):

    """ Функция, которая сортирует операции по дате """

    valid_operations = []

    for operation in operations:
        if not operation:
            continue
        elif not "date" in operation:
            continue
        elif not operation.get("date"):
            continue
        valid_operations.append(operation)

    sorted_list_of_operations = sorted(valid_operations, key=lambda operation:operation["date"], reverse=True)

    return sorted_list_of_operations


def filtering_operations(operations):

    """ Функция, которая добавляет в список только выполненные операции и выводит сразу 5 последних операций """

    operations_performed = []

    for one_operation in operations:
        if one_operation.get("state") == "EXECUTED":
            operations_performed.append(one_operation)

    return operations_performed[:5]


def masking_the_card_number(bill_info):

    """ Функция, которая маскирует номер карты или счета """

    # разделяем название карты и номер карты
    card_info = bill_info.split()
    # берем только номер карты
    number = card_info[-1]

    if bill_info.lower().startswith("счет"):
        masked_number = f"**{number[-4:]}"
    else:
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[12:]}"

    card_info[-1] = masked_number
    hidden_bill_info = " ".join(card_info)

    return hidden_bill_info


def output_of_operations(operation):

    """ Функция, которая выводит операции по требованиям """

    line_1 = ""
    line_2 = ""
    line_3 = ""

    date = datetime.strptime(operation.get("date"), "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    description = operation.get("description")
    from_account = operation.get("from")
    to_account = operation.get("to")
    amount = operation.get("operationAmount", {}).get("amount")
    currency = operation.get("operationAmount", {}).get("currency", {}).get("name")

    line_1 += date + " " + description

    if from_account is None:
        from_account = ""
    else:
        from_hidden_info = masking_the_card_number(from_account)
        line_2 += from_hidden_info

    if to_account is None:
        to_account = ""
    else:
        to_hidden_info = masking_the_card_number(to_account)
        line_2 += " -> " + to_hidden_info

    line_3 += amount + " " + currency

    print(f"""{line_1}.
{line_2}.
{line_3}\n""")


def main():

    operations = load_operations()
    sorted_operations = sorting_operations(operations)
    executed_operations = filtering_operations(sorted_operations)
    for operation in executed_operations:
        output_of_operations(operation)


if __name__ == '__main__':
    main()