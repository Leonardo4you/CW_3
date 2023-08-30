from utils_draft import load_operations, filter_sort_operations, transform_data, card, mask_check


def main():
    operations = load_operations('operations.json')
    # print(operations)
    sorted = filter_sort_operations(operations)[:5]
    # print(sorted)
    for operation in sorted:
        print(f'{transform_data(operation.get("date"))} {operation.get("description")}')
        print(f'{card(operation.get("from")) if operation.get("from") else None} -> {mask_check(operation.get("to"))}')
        print(f'{operation.get("operationAmount").get("amount")} {operation.get("operationAmount").get("currency").get("name")}')


main()

