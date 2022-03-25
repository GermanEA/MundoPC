from DispositivoEntrada import DispositovoEntrada


class Teclado(DispositovoEntrada):
    contador_teclados = 0

    @classmethod
    def aumentar_contador(cls):
        cls.contador_teclados += 1
        return cls.contador_teclados

    def __init__(self, tipo_entrada, marca):
        self._id_teclado = self.aumentar_contador()
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return f'Id: {self._id_teclado}, Marca: {self.marca}, Tipo Entrada: {self.tipo_entrada}'


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    teclado2 = Teclado('Gamer', 'Bluetooth')
    print(teclado1)
    print(teclado2)
