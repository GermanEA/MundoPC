class Monitor:
    contador_monitores = 0

    @classmethod
    def aumentar_contador(cls):
        cls.contador_monitores += 1
        return cls.contador_monitores

    def __init__(self, marca, tamano):
        self._id_monitor = self.aumentar_contador()
        self._marca = marca
        self._tamano = tamano

    @property
    def marca(self):
        return self._marca

    @property
    def tamano(self):
        return self._tamano

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

    def __str__(self):
        return f'Id: {self._id_monitor}, Marca: {self.marca}, Tamaño: {self.tamano}'


if __name__ == '__main__':
    monitor1 = Monitor('HP', 15)
    monitor2 = Monitor('Acer', 27)
    print(monitor1)
    print(monitor2)