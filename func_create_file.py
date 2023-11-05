import random
import os


def mult_files(folder, **kwargs):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    os.chdir(folder)
    for k, v in kwargs.items():
        create_file(k, num_files=v)


def create_file(ext, min_len=6, max_len=30, min_byte=256, max_byte=4096, num_files=42):
    for i in range(num_files):
        name = ''.join([chr(random.randint(97, 122)) for _ in range(random.randint(min_len, max_len))])
        while True:
            if not os.path.isfile(f'{name}.{ext}'):
                with open(f'{name}.{ext}', 'w', encoding='utf-8') as f:
                    for j in range(min_byte, max_byte):
                        print(chr(random.randint(97, 122)), end='', file=f)
                break


mult_files('new_folder', txt=5, cfg=3)


