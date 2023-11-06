import json
import csv


def json_to_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_1,\
          open(f'{file_name.split(".")[0]}.csv', 'w', encoding='utf-8') as f_2:
        data = json.load(f_1)
        result = ['level', 'id', 'name']
        for k, v in data.items():
            for a, b in v.items():
                result.append([k, a, b])
        csv_write = csv.DictWriter(f_2, dialect='excel')
        csv_write.writerows(result)


json_to_csv('users.json')