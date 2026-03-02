from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio_alquiler, num_puertas, disponible=True):
        super().__init__(marca, modelo, precio_alquiler, disponible)
        self.__num_puertas = num_puertas

    def get_num_puertas(self):
        return self.__num_puertas

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Número de puertas: {self.__num_puertas}"
