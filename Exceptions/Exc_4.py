import json


class User:
    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level

    def __str__(self):
        return f'\n\nUser:\nid: {self.id}\nname: {self.name}\naccess level: {self.level}'


def users_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data)
    users = set()
    for id in data.keys():
        for k, v in data[id].items():
            users.add(User(id, v, k))
    return users


print(*users_from_json('users.json'))