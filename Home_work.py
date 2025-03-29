class User:
    def __init__(self, user_id, name, access_level="user"):
        # Инициализируем закрытые атрибуты
        self.__id = user_id
        self.__name = name
        self.__access_level = access_level

    # Геттеры для доступа к закрытым атрибутам
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Сеттер для изменения имени
    def set_name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return f"User(ID: {self.__id}, Name: {self.__name}, Access: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        # Вызываем конструктор базового класса и устанавливаем уровень доступа 'admin'
        super().__init__(user_id, name, access_level="admin")
        # Список пользователей, которыми управляет администратор
        self.__user_list = []

    def add_user(self, user: User):
        self.__user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен администратором {self.get_name()}.")

    def remove_user(self, user_id: int):
        for i, user in enumerate(self.__user_list):
            if user.get_id() == user_id:
                removed_user = self.__user_list.pop(i)
                print(f"Пользователь {removed_user.get_name()} удален администратором {self.get_name()}.")
                return removed_user
        print(f"Пользователь с ID {user_id} не найден.")
        return None

    def list_managed_users(self):
        print("Управляемые пользователи:")
        for user in self.__user_list:
            print(user)

    def get_user_list(self):
        return self.__user_list


# Демонстрация работы
if __name__ == "__main__":
    # Создаем пользователей
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    user3 = User(3, "Charlie")

    # Создаем администратора
    admin1 = Admin(100, "AdminJohn")

    # Администратор добавляет пользователей
    admin1.add_user(user1)
    admin1.add_user(user2)
    admin1.add_user(user3)

    # Выводим список управляемых пользователей
    admin1.list_managed_users()

    # Удаляем пользователя
    admin1.remove_user(2)

    # Выводим список управляемых пользователей после удаления
    admin1.list_managed_users()

    # Выводим информацию о пользователях
    print(user1)
    print(user2)
    print(user3)
    print(admin1)
