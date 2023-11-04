def func(file_1, file_2, file_3):
    with open(file_1, 'r', encoding='utf-8') as f_1, \
            open(file_2, 'r', encoding='utf-8') as f_2, \
            open(file_3, 'w', encoding='utf-8') as f_3:
        list_numbers = f_1.readlines()
        list_words = f_2.readlines()
        result_length = max(len(list_numbers), len(list_words))
        counter_1 = 0
        counter_2 = 0
        for _ in range(result_length):
            a, b = list_numbers[counter_1].split(sep='|')
            result = int(a) * float(b)
            if result < 0:
                print(f'{list_words[counter_2].lower().strip()} {abs(result)}', file=f_3)
            else:
                print(f'{list_words[counter_2].upper().strip()} {round(result)}', file=f_3)
            counter_1 += 1
            counter_2 += 1
            if counter_1 == len(list_numbers):
                counter_1 = 0
            if counter_2 == len(list_words):
                counter_2 = 0


func('new_file.txt', 'new_names.txt', 'result_file.txt')