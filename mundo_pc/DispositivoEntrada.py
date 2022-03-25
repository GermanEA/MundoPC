from abc import ABC, abstractmethod


class DispositovoEntrada(ABC):

    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    @property
    def tipo_entrada(self):
        return self._tipo_entrada

    @property
    def marca(self):
        return self._marca

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @abstractmethod
    def __str__(self):
        pass