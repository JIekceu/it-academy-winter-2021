while True:
    m = int(input("Цена товара, руб.: "))
    n = int(input("Цена товара, коп.: "))
    l = int(input("Введите количество товара: "))
    sm = int(m * l)
    sl = int(n * l)
    if sl > 100:
        sm = sm + sl // 100
        ssl = int(sl % 100)
        print('Общая цена ' + str(sm) + ' рублей ' + str(ssl) + ' копеек')
    else:
        print('Общая цена ' + str(sm) + ' рублей ' + str(sl) + ' копеек')
