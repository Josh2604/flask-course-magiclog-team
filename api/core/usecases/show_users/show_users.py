from api.respository.user.user import UserRepository


class UserCase:
    @classmethod
    def show_users(cls):
        return UserRepository().show()
