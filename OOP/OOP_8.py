class Archive:
    list_str = []
    list_int = []

    def __init__(self, number, string):
        self.number = number
        self.string = string
        self.list_int.append(number)
        self.list_str.append(string)


a = Archive(123, 'sadf')
b = Archive(789, 'asdfgfds')

print(f'{a = }')
