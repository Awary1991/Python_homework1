# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("введите трехзначное число")
a = int(input())

b = (a % 10)

c = (a // 10)

f = (c % 10)

d = (a // 100)

e = (b + f + d)

print(e)