from api.core.providers.user import UserProvider


class UserRepository(UserProvider):
    def show(self):
        dummy_user_list = [
            {
                "name": "Rene",
                "apells": "Mendoza"
            },
            {
                "name": "Javier",
                "apells": "",
            },
            {
                "name": "Omar",
                "apells": "Santiago"
            }
        ]
        return dummy_user_list
