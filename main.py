class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, admin_id, name):
        super().__init__(admin_id, name)
        self.__access_level = 'admin'

        self.__users_list = []

    def add_user(self, new_user):
        if isinstance(new_user, User):
            self.__users_list.append(new_user)
            print(f"Пользователь {new_user.get_name()} успешно добавлен.")
        else:
            raise TypeError("Можно добавить только экземпляр класса User")

    def remove_user(self, target_user):
        for u in self.__users_list:
            if u.get_id() == target_user.get_id():
                self.__users_list.remove(u)
                print(f"Пользователь {target_user.get_name()} удалён.")
                break
        else:
            print("Пользователь не найден.")

    def show_users(self):
        print("\nСписок пользователей:")
        for u in self.__users_list:
            print(f"{u.get_id()} | {u.get_name()} | Доступ: {u.get_access_level()}")