class Vehiculo:
    def __init__(self, marca, modelo, precio_alquiler, disponible=True):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio_alquiler = precio_alquiler
        self.__disponible = disponible
        self.__encendido = False
        self.__velocidad = 0

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_precio_alquiler(self):
        return self.__precio_alquiler

    def get_disponible(self):
        return self.__disponible

    def get_encendido(self):
        return self.__encendido

    def get_velocidad(self):
        return self.__velocidad

    def encender(self):
        if not self.__encendido:
            self.__encendido = True
            return f"El {self.__marca} {self.__modelo} se ha encendido."
        return f"El {self.__marca} {self.__modelo} ya está encendido."

    def mostrar_informacion(self):
        estado = "True" if self.__disponible else "False"
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Precio: {self.__precio_alquiler}, Disponible: {estado}"

    def alquilar(self):
        if self.__disponible:
            self.__disponible = False
            return "Vehículo alquilado con éxito."
        return "Vehículo ya alquilado."

    def devolver(self):
        self.__disponible = True
        return "Vehículo devuelto con éxito."

    def __str__(self):
        return f"Vehículo {self.__marca} {self.__modelo}"
