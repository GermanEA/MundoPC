from mundo_pc.Monitor import Monitor
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado


class Computadora:
    contador_computadoras = 0

    @classmethod
    def aumentar_contador(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras

    def __init__(self, nombre, monitor, teclado, raton):
        self._id_computadora = self.aumentar_contador()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @property
    def monitor(self):
        return self._monitor

    @property
    def teclado(self):
        return self._teclado

    @property
    def raton(self):
        return self._raton

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''
            {self._nombre}: {self._id_computadora}
            Monitor: {self.monitor}
            Teclado: {self.teclado}
            Ratón: {self.raton}
        '''


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 15)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)