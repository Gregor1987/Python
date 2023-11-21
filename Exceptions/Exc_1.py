def get_number():
    while True:
        try:
            number = float(input('input number: '))
            break
        except ValueError as err:
            print(f'{err}, try again: ')
    return number


print(get_number())
