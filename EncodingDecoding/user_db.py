import random, string

class user_db():
    def __init__(self) -> None:
        self.salt = self.generate_salt()

    def generate_salt(self):
        _LENGTH=16

        string_pool=string.ascii_letters + string.digits + string.punctuation
        result=""
        for i in range(_LENGTH):
            result+=random.choice(string_pool)

        # print("salt is... "+result)
        return result.encode()