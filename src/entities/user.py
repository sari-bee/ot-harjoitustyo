class User:

    def __init__(self, username: str, sample_ids: list):
        self.__username = username
        self.__sample_ids = sample_ids

    @property
    def username(self):
        return self.__username

    @property
    def sample_ids(self):
        return self.__sample_ids

    def add_sample_id(self, sample_id: str):
        self.__sample_ids.append(sample_id)
