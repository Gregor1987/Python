import random


def random_names(file_name: str, names_count: int):
    file_name = file_name + '.txt'
    letters = {1: 'a', 2: 'e', 3: 'u', 4: 'i', 5: 'o'}
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(names_count):
            name_length = random.randint(4, 7)
            name = ''
            for j in range(name_length):
                name += chr(random.randint(97, 122))
            if 'a' not in name or 'e' not in name or 'u' not in name or i not in name or 'o' not in name:
                name = list(name)
                name[random.randint(0, name_length - 1)] = letters.get(random.randint(1, 5))
                name = ''.join(name)
            print(name. capitalize(), end='\n', file=f)


random_names('new_names', 10)
