import os
from repositories.user_repository import UserRepository
from entities.user import User


class UserHandler:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.user_repository = UserRepository(
            os.path.join(dirname, "../..", "data", "users.csv"))

    def add_new_user(self, username: str):
        samples = []
        user = User(username, samples)
        success = self.user_repository.add_user(user)
        if not success:
            return None
        return user

    def find_user_by_username(self, username: str):
        return self.user_repository.find_user(username)

    def add_sample_to_user(self, user: User, sample_id: str):
        self.user_repository.add_sample(user, sample_id)

    def get_all_users(self):
        usernames = self.user_repository.get_usernames()
        if len(usernames) == 0:
            return "Ei vielä käyttäjiä."
        return usernames

    def get_number_of_samples(self, user: User):
        samples = self.user_repository.get_sample_ids_by_user(user)
        return len(samples)

    def get_samples_by_user(self, user: User):
        sample_ids = self.user_repository.get_sample_ids_by_user(user)
        return sample_ids
