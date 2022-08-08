import abc


class Builder(abc.ABC):
    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass
