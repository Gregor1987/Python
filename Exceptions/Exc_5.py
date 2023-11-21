import json
from Exc_3 import AccessException, LevelException


class User:
    def __init__(self, id, name, level=None):
        self.id = id
        self.name = name
        self.level = level

    def __str__(self):
        return f'\n\nUser:\nid: {self.id}\nname: {self.name}\naccess level: {self.level}'

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash((self.id, self.name))


class Project:

    def __init__(self, filename='users.json'):
        self.filename = filename
        try:
            self.users = self.users_from_json()
        except:
            print('error, no users')
            self.users = set()

    def users_from_json(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(data)
        users = set()
        for level in data.keys():
            for k, v in data[level].items():
                users.add(User(k, v, level))
        return users

    def login_to_system(self):
        login_id = input('input id: ')
        login_name = input('input name: ')
        login_user = User(login_id, login_name)
        for user in self.users:
            if login_user == user:
                self.user = user
                break
        else:
            raise AccessException

    def add_user(self):
        new_user_name = input("input new user's name: ")
        new_user_id = input("input new user's id: ")
        new_user_level = input("input new user's access level: ")
        if self.user.level > new_user_level:
            raise LevelException(self.user.name, new_user_level)
        else:
            self.users.add(User(new_user_id, new_user_name, new_user_level))


p = Project()
p.login_to_system()
p.add_user()
