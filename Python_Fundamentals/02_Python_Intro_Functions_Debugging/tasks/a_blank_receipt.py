def header_print():
    print('CASH RECEIPT')
    dash_print()


def dash_print():
    print('------------------------------')


def body_print():
    print('Charged to____________________')
    print('Received by___________________')


def footer_print():
    dash_print()
    print('© SoftUni')


def print_controller():
    header_print()
    body_print()
    footer_print()


print_controller()
