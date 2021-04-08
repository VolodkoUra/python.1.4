"""Проверить, есть ли в последовательности дубликаты"""

"""Способ 1"""
def power():
    a = [1, 4, 2, 7, 2, 3, 5, 1, 8, 0]
    b = [1, 4, 2, 7, 9, 3, 5, 6, 0]
    for i in a:
        if a.count(i)>1:
            print("В последовательности есть дубликаты")
            break
        else:
            print("В последовательности нет дубликатов")


"""Способ 2"""
def power2():
    a = [1, 4, 2, 7, 2, 3, 5, 1, 8, 0]
    b = set(a)

    if len(a) == len(b):
        print("В последовательности нет дубликатов")
    else:
        print("В последовательности есть дубликаты")




if __name__ == '__main__':
    power()
    power2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
