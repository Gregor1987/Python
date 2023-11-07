import json
import csv


def json_to_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_1,\
          open(f'{file_name.split(".")[0]}.csv', 'w', newline='', encoding='utf-8') as f_2:
        data = json.load(f_1)
        rows = []
        for access_level, value in data.items():
            for user_id, user_name in value.items():
                rows.append({'level': int(access_level), 'id': int(user_id), 'name': user_name})
        csv_write = csv.DictWriter(f_2, dialect='excel', fieldnames=['level', 'id', 'name'])
        csv_write.writeheader()
        csv_write.writerows(rows)


json_to_csv('users.json')
