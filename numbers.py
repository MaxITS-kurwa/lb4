def numbers():

    try:
      num1 = float(input("Введите первое число: "))
      num2 = float(input("Введите второе число: "))
      num3 = float(input("Введите третье число: "))
      num4 = float(input("Введите четвертое число: "))

      sum1 = num1 + num2
      sum2 = num3 + num4

      if sum2 == 0:
          print("Ошибка: Деление на ноль невозможно.")
          return

      result = sum1 / sum2
      print(f"Результат: {result:.2f}")

    except ValueError:
      print("Ошибка: Некорректный ввод. Пожалуйста, введите числа.")


if __name__ == "__main__":
    numbers()