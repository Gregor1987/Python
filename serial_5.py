import json
import pickle
import os


def json_to_pickle(folder):
    for _, _, files in os.walk(folder):
        for file in files:
            if file.split('.')[-1] == 'json':
                with open(file, 'r', encoding='utf-8') as f_1, \
                      open(f'{file.rsplit(".", 1)[0]}.pickle', 'wb') as f_2:
                    data = json.load(f_1)
                    pickle.dump(data, f_2)


json_to_pickle('C:/Users/aborisov6/PycharmProjects/HW_1')
