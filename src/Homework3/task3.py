'''
3.	Tuple practice
1.	Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2.	Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3.	Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4.	Создайте кортеж из одного элемента,
чтобы при итерировании по этому элементы последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
Задачу поместите в файл task3.py в папке src/homework3.

'''
list_ = ['a', 'b', 'c']
list_ = tuple(list_)
print('1. ', list_)
tpl2 = ('a', 'b', 'c')
tpl2 = list(tpl2)
print('2. ', tpl2)
a, b, c = 'a', 2, 'python'
tpl4 = ([1, 2, 3], )
print('4.1. len: ', len(tpl4))
for i in tpl4:
    print('4.2. iter:', i)
