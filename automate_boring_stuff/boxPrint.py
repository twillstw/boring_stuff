def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol must be a single character str')
    if width <= 2:
        raise Exception('must be more than 2, yo')
    if height <= 2:
        raise Exception('must be at least 2')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width -2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

