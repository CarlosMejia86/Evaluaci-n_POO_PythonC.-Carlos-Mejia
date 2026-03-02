from vehiculo import Vehiculo

class Taxi(Vehiculo):
    def __init__(self, marca, modelo, precio_alquiler, tarifa_por_km, disponible=True):
        super().__init__(marca, modelo, precio_alquiler, disponible)
        self.__tarifa_por_km = tarifa_por_km
        self.__kilometraje = 0

    def get_tarifa_por_km(self):
        return self.__tarifa_por_km

    def get_kilometraje(self):
        return self.__kilometraje

    def calcular_tarifa(self, km):
        self.__kilometraje = km
        tarifa_total = self.__tarifa_por_km * self.__kilometraje
        return tarifa_total

    def devolver(self):
        super().devolver()
        self.__kilometraje = 0
        return "Vehículo devuelto con éxito. Kilometraje reiniciado"

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Tarifa por km: {self.__tarifa_por_km}, Kilometraje: {self.__kilometraje}"
