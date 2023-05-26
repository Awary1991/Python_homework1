print("Введите длинну шоколадки")

a = int(input())

print("Введите ширину шоколадки")

b = int(input())

print("сколько отломить долек")

c = int(input())

if c < a * b and (c % a == 0 or c % b == 0):
    print("Можно")
else:
    print("Нельзя")