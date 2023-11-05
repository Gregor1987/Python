import os
import shutil


def sort(folder, **kwargs):
    for _, _,  files in os.walk(folder):
        for file in files:
            ext = file.split('.')[-1]
            for item in kwargs:
                if ext in kwargs[item]:
                    if not os.path.isdir(item):
                        os.mkdir(item)
                    shutil.move(f'{folder}/{file}', item)


sort('new_folder', video=['avi', 'mov'], images=['jpg', 'png'], text=['txt', 'doc'])
