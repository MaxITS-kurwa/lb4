from math import *

def individual():

    try:
        x1 = float(input("Введите координату x первой точки: "))
        y1 = float(input("Введите координату y первой точки: "))
        x2 = float(input("Введите координату x второй точки: "))
        y2 = float(input("Введите координату y второй точки: "))

        distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

        print(f"Расстояние между точками: {distance:.2f}")

    except ValueError:
        print("Ошибка: Некорректный ввод. Пожалуйста, введите числа.")


if __name__ == "__main__":
    individual()