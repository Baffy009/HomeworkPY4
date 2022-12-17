# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n_list = []
n_num = int(input("N: "))
simple = 2
n_list.append(simple) 
while simple <= n_num:
    if n_num % simple == 0:
        if simple != 2:
            n_list.append(simple)
        n_num //= simple
        simple = 2
    else: simple += 1
print(n_list)
