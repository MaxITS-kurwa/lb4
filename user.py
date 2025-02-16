class User:
    def __init__(self, name="", age=0, location=""):
        self.name = name
        self.age = age
        self.location = location

    def __str__(self):
        return f"Имя: {self.name}\nВозраст: {self.age}\nАдрес: {self.location}"

def get_user_info():

    name = input("Как вас зовут? ")
    while True:
        try:
            age = int(input("Сколько вам лет? "))
            if age < 0:
                print("Возраст не может быть отрицательным.")
            else:
                break
        except ValueError:
             print("Некорректный ввод. Пожалуйста, введите целое число для возраста.")
    location = input("Где вы живёте? ")
    return User(name, age, location)

if __name__ == "__main__":
    user = get_user_info()
    print("\nИнформация о пользователе:")
    print(user)