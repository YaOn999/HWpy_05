# Задача 26:  Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую неотрицательную
# степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def get_res_degree(a, b):
    if b == 1:
        return a
    return a * get_res_degree(a, b - 1)

a, b = map(int, input().split())
print(get_res_degree(a, b))
