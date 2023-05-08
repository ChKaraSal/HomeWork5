# Задача 26:  
# Напишите программу, 
# которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

A = int(input("Enter A: "))
B = int(input("Enter B: "))


def func(A, B):
    if B == 0:
        return 1

    return A * func(A, B - 1)


print(func(A, B))


# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 


print("Task: 28")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

def recursive_sum(a, b):
    if a == 0:
        return b
    else:
        return recursive_sum(a - 1, b + 1)


print(recursive_sum(a, b))