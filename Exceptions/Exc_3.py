class UserException(Exception):
    pass


class LevelException(UserException):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f'User {self.name} is not authorized to add new users with access level {self.level}'


class AccessException(UserException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'User {self.name} not found'
