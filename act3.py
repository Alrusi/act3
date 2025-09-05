print("==============================================================================")
print("\tBienvenido a La TecmiCalculadora de consumo energetico y costos")
print("==============================================================================") 
def calcular_consumoycosto(consumo_w, tiempo_uso, costo_kwh):
    consumo_diariokwh=(consumo_w * tiempo_uso)/1000
# tabla
def mostrar_menu():
    print("1. Mostrar la tabla completa con su consumo")
    print("2. Consultar el gasto energético y costo mensual de un dispositivo en particular")
    print("3. Consultar el gasto energético y costo mensual de un dispositivo en particular")
    print("4. Salir")
# Guardado de datos
def main():
    dispositivos=[]
    n=int(input("Cuantos dispositivos deseas registrar?"))
    costo_kwh=float(input("Ingresa el costo del kwh"))

    for i in range(n):
        print("Dispositivo: " [i + 1])
        nombre_disp=input("Nombre del dispositivo: ")
        consumo_w=float(input("Consumo en watts del dispositivo: "))
        tiempo_uso=float(input("Horas de uso diario: "))
        dispositivos.append(nombre_disp, consumo_w, tiempo_uso)

    while True:

        mostrar_menu()

        opcion=input("Seleccione la opcion deseada: ")
        if opcion=="1":
             
             print("Tabla de dispositivos registrados:")
             print("Nombre\t\Watts\tHoras/Dia")
             for d in dispositivos:
                  print({"d[0]\t,d[1]w\t, d[2]h"})
        elif opcion=="2":
            nombre_buscar=input("Ingresa el nombre del dispositivo que deseas consultar: ")
            encontrado=False
            for d in dispositivos:
                if d[0]==nombre_buscar:
                    consumo, costo=calcular_consumoycosto
