def arithmetic():

    expression = "4 * 100 - 54"
    correct_answer = 4 * 100 - 54

    print(f"Решите следующий пример: {expression}")
    user_answer = int(input("Ваш ответ: "))

    print(f"Правильный ответ: {correct_answer}")
    print(f"Ваш ответ: {user_answer}")

    if user_answer == correct_answer:
      print("Правильно!")
    else:
      print("Неправильно!")


print(arithmetic())