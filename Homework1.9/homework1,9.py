def summa(deposit, mesyac, procent ):
    b = deposit
    for i in range(mesyac):

        b = procent / 100 / 12 * b + b
    return int(b)
print(summa(100000, 6, 12))


