import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'  # получаем директорию где хранятся блоки ./blockchain/

def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def get_files():
    files = os.listdir(blockchain_dir)                # получаем список файлов в папке
    return sorted([int(i) for i in files])            #приводим элементы списка к целому типу для сортировки по порядку


def check_integrity():
    # 1. считать хэш предыдущего блока
    # 2. вычислить хэш предыдущего блока
    # 3. сравнить полученные данные
    files = get_files()# получили список чисел

    results = []

    for file in files[1:]: #прокручиваем список в цикле. На каждой итерации берем файл,считываем хэш и вычисляем хэш предыдущего блока
        f = open(blockchain_dir + str(file)) #обращаемся к директории и преобразовываем значение переменной файл в тип строки
        h = json.load(f)['hash']  # принимает значения результата функции load из модуля json и образаемся к ключу "хэш"
        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash: #условие для проверки хэша
            res = 'Okey'
        else:
            res = 'Corrupted'

            #print(f'block {prev_file} is: {res}')
        results.append({'block': prev_file, 'result': res})
    return results




# функция
def write_block(name, amount, to_whom, prev_hash=''):
    files = get_files()
    prev_file = files[-1]

    filename = str(prev_file + 1)
    # переопределяем параметр
    prev_hash = get_hash(str(prev_file))

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    # write_block(name='kirill', amount=5, to_whom='ksu')
    print(check_integrity())


if __name__ == '__main__':
    main()