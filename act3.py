print("==============================================================================")
print("\tBienvenido a La TecmiCalculadora de consumo energético y costos")
print("==============================================================================") 

# funciones para calcular el costo y el consumo
def calcular(consumo_w, tiempo_uso, costo_kwh):
    consumo_mensual = (consumo_w * tiempo_uso / 1000) * 30
    costo_mensual = consumo_mensual * costo_kwh
    return consumo_mensual, costo_mensual

# tabla
def mostrar_menu():
    print("\n1. Mostrar la tabla completa con su consumo")
    print("2. Consultar el gasto energético y costo mensual de un dispositivo en particular")
    print("3. Calcular el consumo y costo total mensual de todos los dispositivos")
    print("4. Salir")

# programa principal
def main():
    dispositivos = []
    n = int(input("Cuántos dispositivos deseas registrar? "))
    costo_kwh = float(input("Ingresa el costo del kWh: "))

# datos de los dispositivos
    for i in range(n):
        print("\nDispositivo", i + 1)
        nombre_disp = input("Nombre del dispositivo: ")
        consumo_w = float(input("Consumo en watts (W): "))
        tiempo_uso = float(input("Horas de uso diario: "))
        dispositivos.append([nombre_disp, consumo_w, tiempo_uso])
    

    while True:
        mostrar_menu()
        opcion = input("Seleccione la opción deseada: ")

        if opcion == "1":
            print("\nTabla de dispositivos registrados:")
            print("Nombre\t\tWatts\tHoras/Día")
            for d in dispositivos:
                print(d[0], "\t", d[1], "W\t", d[2], "h/día")

        elif opcion == "2":
            nombre_buscar = input("Ingresa el nombre del dispositivo a consultar: ")
            encontrado = False
            for d in dispositivos:
                if d[0] == nombre_buscar:
                    consumo, costo = calcular(d[1], d[2], costo_kwh)
                    print("\nDispositivo:", d[0])
                    print("Consumo mensual:", consumo, "kWh")
                    print("Costo mensual: $", costo)
                    encontrado = True
            if not encontrado:
                print("Dispositivo no encontrado")

        elif opcion == "3":
            consumo_total = 0
            costo_total = 0
            for d in dispositivos:
                consumo, costo = calcular(d[1], d[2], costo_kwh)
                consumo_total += consumo
                costo_total += costo
            print("\nConsumo mensual total:", consumo_total, "kWh")
            print("Costo mensual total: $", costo_total)

        elif opcion == "4":
            print("Gracias por usar la TecmiCalculadora")
            break

        else:
            print("Opción no válida, intenta de nuevo")



main()