import json


def to_json(file):
    some_dict = {}
    with open(file, 'r', encoding='utf-8') as f_1, \
            open(f'{file.split(".")[0]}.json', 'w', encoding='utf-8') as f_2:
        for line in f_1:
            some_dict[(line.strip().capitalize().split(' '))[0]] = (line.strip().split(' '))[1]
        json.dump(some_dict, f_2, indent=0)


to_json('result_file.txt')
