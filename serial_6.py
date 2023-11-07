import pickle
import csv


def pickle_to_csv(file):
    with open(file, 'rb') as f_1, \
          open(f'{file.rsplit(".", 1)[0]}.csv', 'w', encoding='utf-8', newline='') as f_2:
        data = pickle.load(f_1)
        field_names = []
        for key in data[0].keys():
            field_names.append(key)
        csv_write = csv.DictWriter(f_2, fieldnames=field_names, dialect='excel')
        csv_write.writeheader()
        csv_write.writerows(data)


pickle_to_csv('users_new.pickle')
