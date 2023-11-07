import csv
import json


def csv_to_json(init_name, final_name):
    with open(init_name, 'r', encoding='utf-8') as f_1, \
            open(final_name, 'w', encoding='utf-8') as f_2:
        data = csv.reader(f_1)
        raw_data = []
        new_data = []
        for row in data:
            raw_data.append(row)
        for i in range(1, len(raw_data)):
            new_data.append(
                {raw_data[0][0]: raw_data[i][0], raw_data[0][1]: f'{int(raw_data[i][1]):010}',
                 raw_data[0][2]: raw_data[i][2].capitalize(), 'hash': hash(raw_data[i][2] + raw_data[i][1])})
        json.dump(new_data, f_2, indent=2)


csv_to_json('users.csv', 'users_new.json')
