import abc


class UserProvider(abc.ABC):
    @abc.abstractmethod
    def show(self): raise NotImplementedError
