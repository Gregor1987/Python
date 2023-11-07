import json
from json import JSONDecodeError


def add_to_base():
    while True:
        user_name = input('input name:\n')
        # try:
        access_level = input('input your access level:\n')
        while not access_level.isdigit() or not 1 <= int(access_level) <= 7:
            access_level = input('incorrect input, please, try again:\n')
        user_id = input('input your id:\n')
        while not user_id.isdigit():
            user_id = input('incorrect input, please, try again:\n')
        user = {access_level: {user_id: user_name}}
        try:
            with open('users.json', 'r', encoding='utf-8') as f:
                users_dict = json.load(f)
                for k in users_dict.keys():
                    while not user_id.isdigit() or user_id in users_dict[k].keys():
                        user_id = input('id incorrect or already exists, try again:\n')
                if access_level in users_dict.keys():
                    users_dict[access_level].update({user_id: user_name})
                else:
                    users_dict[access_level] = {user_id: user_name}
            with open('users.json', 'w', encoding='utf-8') as f:
                json.dump(dict(sorted(users_dict.items())), f, indent=2)
        except FileNotFoundError and JSONDecodeError:
            with open('users.json', 'w', encoding='utf-8') as f:
                json.dump(user, f, indent=2)


add_to_base()
