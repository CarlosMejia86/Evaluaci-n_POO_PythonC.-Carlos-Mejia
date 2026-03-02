from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio_alquiler, cilindrada, disponible=True):
        super().__init__(marca, modelo, precio_alquiler, disponible)
        self.__cilindrada = cilindrada

    def get_cilindrada(self):
        return self.__cilindrada

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Cilindrada: {self.__cilindrada} cc"
