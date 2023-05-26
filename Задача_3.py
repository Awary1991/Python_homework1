print("введите шестизначное число")
a = int(input())

Left = (a // 1000)

Right = (a % 1000)

b = (Left % 10)

c = (Left // 10)

f = (c % 10)

d = (Left // 100)

SumLeft = (b + f + d)

g = (Right % 10)

h = (Right // 10)

i = (h % 10)

j = (Right // 100)

SumRight = (g + i + j)

if SumLeft != SumRight:

    print("не счастливый")

else:

    print("счастливый")