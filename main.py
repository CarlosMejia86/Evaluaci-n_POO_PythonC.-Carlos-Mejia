from auto import Auto
from moto import Moto
from taxi import Taxi

def main():
    # Crear instancias
    mi_auto = Auto("Toyota", "Corolla", 50000, 4)
    mi_moto = Moto("Yamaha", "R3", 30000, 321)
    mi_taxi = Taxi("Hyundai", "Accent", 60000, 5000)

    # Mostrar información inicial
    print(mi_auto.mostrar_informacion())
    print(mi_moto.mostrar_informacion())
    print(mi_taxi.mostrar_informacion())

    # Probar Alquiler
    print(mi_auto.alquilar())
    print()

    # Información después de alquilar
    print(mi_auto.mostrar_informacion())

    # Devolver vehículo
    print(mi_auto.devolver())

    # Probar Taxi
    distancia = 15
    costo_taxi = mi_taxi.calcular_tarifa(distancia)
    print(f"Costo del viaje en taxi por {distancia} km: {costo_taxi}")
    print(mi_taxi.mostrar_informacion())
    print(mi_taxi.devolver())

if __name__ == "__main__":
    main()
