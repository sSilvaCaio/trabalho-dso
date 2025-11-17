from abc import ABC, abstractmethod
import pickle


class BaseDAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self.datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        with open(self.datasource, "wb") as f:
            pickle.dump(self.__cache, f)

    def __load(self):
        with open(self.datasource, "rb") as f:
            self.__cache = pickle.load(f)

    def add(self, key, obj):
        if key in self.__cache:
            return False
        try:
            self.__cache[key] = obj
            self.__dump()
            return True
        except (OSError, pickle.PickleError):
            return False

    def update(self, key, obj):
        if key not in self.__cache:
            return False
        try:
            self.__cache[key] = obj  # atualiza a entrada
            self.__dump()  # atualiza o arquivo
            return True
        except (OSError, pickle.PickleError):
            return False

    def get(self, key):
        return self.__cache.get(key)

    def remove(self, key):
        if key not in self.__cache:
            return False
        try:
            self.__cache.pop(key)
            self.__dump()
            return True
        except (OSError, pickle.PickleError):
            return False

    def get_all(self):
        return list(self.__cache.values())
