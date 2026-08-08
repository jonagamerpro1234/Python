# Se pide realizar un programa tipo cajero que permita al usuario cargar su tarjeta Bip
# Se le cobrara un 2% de comision y luego se le dara un resultado final
# Propuesta del dev: Añadir opciones como consultar saldo o ultimos movimientos

# Definicion de variables del usuario
global saldo
saldo = 0.0

# Funcion principal
def main():
    while True:
        try:
            print("--Cajero--")
            print ("Opciones:")
            print("1. Consultar saldo")
            print("2. Cargar saldo")
            print("3. Salir")
            opc = int(input(""))
        except ValueError:
            print("Valor invalido")
            continue

        # Control de opciones
        if opc < 1 or opc > 3:
            print("Valor invalido")
            continue
        if opc == 1:
            print(f"Saldo actual: ${saldo}")
        if opc == 2:
            cargar_saldo()
        if opc == 3:
            print("Saliendo..")
            break

# Funcion para cargar saldo junto a la comision del 2%
def cargar_saldo():
    # Menu de carga de saldo
    while True:
        try:
            carga = float(input("salir: 0\ncargar saldo: $"))
        except ValueError:
            print("Valor invalido")
            continue

        # Control de opciones de carga
        if carga < 0:
            print("Valor invalido")
            continue

        if carga == 0:
            print("Saliendo..")
            return
        
        else:
            comision = carga * 0.02
            carga = carga - comision
            global saldo
            saldo = saldo + carga
            print(f"Se a añadido ${carga} \nComision cobrada: ${comision}\nSaldo actual: ${saldo}")
            return

# Programa principal
main()
    
