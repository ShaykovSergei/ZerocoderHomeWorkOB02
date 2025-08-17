class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = 'user'

    def get_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = 'admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь успешно добавлен в список")
        print(user_list)

    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"Пользователь удалён")


users = []
admin = Admin('A001', 'Алексей Смирнов')
user1 = User('U001', 'Иван Иванов')
user2 = User('U002', 'Анна Петрова')

print(user1.get_name())
admin.add_user(users, user1)






