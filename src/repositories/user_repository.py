from pathlib import Path
from entities.user import User


class UserRepository:

    def __init__(self, path: str):
        self.path = path

    def read(self):
        users = []
        Path(self.path).touch()
        with open(self.path) as file:
            for row in file:
                if row == "":
                    pass
                if row == "\n":
                    pass
                row = row.replace("\n", "")
                split = row.split(";")
                username = split[0]
                sample_ids = []
                i = 1
                while i < len(split):
                    sample_ids.append(split[i])
                    i = i+1
                user = User(username, sample_ids)
                users.append(user)
        return users

    def write(self, users):
        Path(self.path).touch()
        with open(self.path, "w") as file:
            for user in users:
                row = user.username
                for sample_id in user.sample_ids:
                    row = row + ";" + str(sample_id)
                row = row + "\n"
                file.write(row)

    def add_user(self, new_user: User):
        users = self.read()
        for user in users:
            if user.username == new_user.username:
                return False
        users.append(new_user)
        self.write(users)
        return True

    def find_user(self, username: str):
        users = self.read()
        for user in users:
            if user.username == username:
                return user
        return None

    def add_sample(self, user: User, added_sample_id: str):
        users = self.read()
        i = 0
        while i < len(users):
            if users[i].username == user.username:
                right_user = users[i]
                break
            i = i+1
        right_user.add_sample_id(added_sample_id)
        users[i] = right_user
        self.write(users)

    def get_usernames(self):
        users = self.read()
        usernames = []
        for user in users:
            usernames.append(user.username)
        return usernames

    def get_sample_ids_by_user(self, wanted_user: User):
        users = self.read()
        for user in users:
            if user.username == wanted_user.username:
                return user.sample_ids
        return None
