# ПРЕОБРАЗОВЫВАЕТ СПИСОК СТРОКИ В СПИСОК ЧИСЕЛ
def number_list(x):
    for i, item in enumerate(x):
        x[i] = int(item)
    return x

# РАСПОКАВАТЬ СПИСОК В СПИСКЕ В ОДИН ОБЩИЙ СПИСОК
def unpacking(x):
    x= [i for j in x for i in j]
    return x
