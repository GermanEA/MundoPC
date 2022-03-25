class Orden:
    contador_ordenes = 0

    @classmethod
    def aumentar_contador(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, computadora):
        self._id_orden = self.aumentar_contador()
        self._computadoras = computadora

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
            Orden: {self._id_orden}
            Computadoras: {computadoras_str}
        '''