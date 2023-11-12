import time
import os


class MyStr(str):
    log = []

    def __new__(cls, row):
        instance = super().__new__(cls, row)
        cls.log.append({os.getlogin(): time.time()})
        return instance



my_str = MyStr('asdfjnlasfd')
print(my_str)
print(my_str)
print(my_str.log)
