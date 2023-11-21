def get_value(dic: dict, key, value=None):
    try:
        return dic[key]
    except KeyError:
        return value


print(get_value({1: 10, 2: 20}, 2))
