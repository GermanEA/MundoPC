from DispositivoEntrada import DispositovoEntrada


class Raton(DispositovoEntrada):
    contador_ratones = 0

    @classmethod
    def aumentar_contador(cls):
        cls.contador_ratones += 1
        return cls.contador_ratones

    def __init__(self, tipo_entrada, marca):
        self._id_raton = self.aumentar_contador()
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self.marca}, Tipo Entrada: {self.tipo_entrada}'


if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    raton2 = Raton('Acer', 'Bluetooth')
    print(raton1)
    print(raton2)