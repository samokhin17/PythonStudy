from colorama import init
init()

# Калькулятор v.2

while True:
    what = input("Что делаем? (+, -): ")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if what == "+":
        c = a + b
        print("Результат " + str(c))
    elif what == "-":
        c = a - b
        print("Результат " + str(c))
    else:
        print("Выбрана неверная операция")

