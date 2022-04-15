'''
4.	В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
a.	Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b.	Найдите ТОП250 фильмов и извлеките заголовки.
c.	Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
Задачу поместите в файл task4.py в папке src/homework5.
'''

import numpy as np
import matplotlib.pyplot as plt

#  a
try:
    fh = open('ratings.list', 'r')
except FileNotFoundError:
    print('File not found')
else:
    fh.close()
#  b
str_file = ''
list_title = []
list_rank = []
list_year = []
list_str_array_year = []
dict_rank = dict

set_year = set()
dict_year = dict
y_list_year = []
try:
    open('ratings.list', 'rt')
except FileNotFoundError:
    print('File not found')
else:
    with open('ratings.list', 'rt') as fh:
        while str_file != 'New  Distribution  Votes  Rank  Title\n':
            str_file = fh.readline()  # found begin of TOP
        while str_file != '\n':
            str_file = fh.readline().replace('/I', '')
            list_title.append(str_file[(str_file.find('.') + 4):(len(str_file) - 8)])
            list_rank.append(str_file[(str_file.find('.') - 1):(str_file.find('.') + 2)])
            list_year.append(str_file[(len(str_file) - 6):(len(str_file) - 2)])
        #  c
        list_title.pop()
        list_rank.pop()
        list_year.pop()
        #        print(list_title)
        #        print(list_rank)
        #        print(list_year)

        file1 = open('top250_movies.txt', 'w')
        file1.writelines(line + '\n' for line in list_title)
        file1.close()
        file2 = open('ratings.txt', 'w')
        file2.writelines(line + '\n' for line in list_rank)
        file2.close()
        file3 = open('years.txt', 'w')
        file3.writelines(line + '\n' for line in list_year)
        file3.close()
        print('Export complete')

    x_rank = np.arange(float(min(list_rank)), (float(max(list_rank)) + 0.1), 0.1)
    float_x = []
    list_rank_y = []
    for elem in x_rank:
        float_x.append(str(round(elem, 1)))
    dict_rank = {key: 0 for key in float_x}
    for key in dict_rank:
        dict_rank[key] = list_rank.count(key)
    for _ in dict_rank.values():
        list_rank_y.append(_)
    y_rank = list_rank_y

    fig1, ax = plt.subplots()
    ax.bar(x_rank, y_rank)
    ax.set_facecolor('seashell')
    fig1.set_facecolor('floralwhite')
    fig1.set_figwidth(12)  # ширина Figure
    fig1.set_figheight(6)  # высота Figure
    plt.show()

    x_year = np.arange(int(min(list_year)), (int(max(list_year)) + 1), 1)
    for elem in x_year:
        list_str_array_year.append(str(elem))
    dict_year = {key: 0 for key in list_str_array_year}
    for key in dict_year:
        dict_year[key] = list_year.count(key)
    for _ in dict_year.values():
        y_list_year.append(_)

    fig2, bx = plt.subplots()
    bx.bar(x_year, y_list_year)
    bx.set_facecolor('seashell')
    fig2.set_facecolor('floralwhite')
    fig2.set_figwidth(12)  # ширина Figure
    fig2.set_figheight(6)  # высота Figure
    plt.show()
