import os


def rename_files(numbers_count: int, ext_init: str, ext_final: str, init_range: tuple, folder: str, file_name=''):
    counter = 0
    for _, _, files in os.walk(folder):
        for file in files:
            if ext_init == file.split('.')[-1]:
                final_name = list(file.split('.')[0][init_range[0] - 1: init_range[1] - 1])
                counter += 1
                file_count = list(str(counter))
                while len(file_count) < numbers_count:
                    file_count.insert(0, '0')
                file_count = ''.join(file_count)
                final_name.extend((file_name, file_count, '.', ext_final))
                final_name = ''.join(final_name)
                os.rename(f'{folder}/{file}', f'{folder}/{final_name}')


rename_files(3, 'txt', 'jpg', (2, 5), 'new_folder', 'new_name')