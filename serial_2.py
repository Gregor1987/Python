import json


def add_to_base():
    while True:
        name = input('input name:\n')
        try:
            access_level = input('input your access level:\n')
        except:
            continue
        if not 1 <= int(access_level) <= 7:
            print('incorrect access level')
            continue
        try:
            user_id = input('input your id:\n')
        except:
            continue
        with open('users.json', 'r+', encoding='utf-8') as f:
            try:
                users_dict = json.load(f)
                # print(users_dict)
                for k in users_dict.keys():
                    if user_id in users_dict[k].keys():
                        print('user id already exists')
                        continue
                # if access_level in users_dict.keys():
                #     users_dict[access_level].append({user_id: name})
                #     print(users_dict)
                # else:
                users_dict[access_level].append({user_id: name})
                print('hh')
                        #
                        # users_dict[access_level] = users_dict[access_level].append({user_id: name})
                        # print(users_dict)
            except:
                users_dict = {access_level: {user_id: name}}
                print('lala')
        with open('users.json', 'w', encoding='utf-8') as f_2:
            json.dump(users_dict, f_2, indent=2)


add_to_base()