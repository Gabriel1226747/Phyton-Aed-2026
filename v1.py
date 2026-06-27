import os

class CajeroAutomatico:
    def __init__(self):
        # Ruta del archivo datos.txt
        ruta = os.path.join(os.path.dirname(__file__), "datos.txt")

        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()

        # Datos de acceso
        self.usuario = lineas[0].strip()
        self.contrasena = lineas[1].strip()

        # Datos de cuenta
        self.saldo = float(lineas[2].strip())
        self.limite_extraccion = float(lineas[3].strip())

        # Registro de operaciones
        self.historial = []
        self.contador_operaciones = 0

    # Inicio de sesión
    def iniciar_sesion(self):
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if usuario == self.usuario and contrasena == self.contrasena:
            print("\nAcceso concedido.")
            return True
        else:
            print("\nUsuario o contraseña incorrectos.")
            return False

    # Consultar saldo
    def consultar_saldo(self):
        print(f"\nSaldo disponible: ${self.saldo:.2f}")
        self.historial.append("Consulta de saldo")
        self.contador_operaciones += 1

    # Depositar dinero
    def depositar(self):
        try:
            monto = float(input("Ingrese el monto a depositar: $"))

            if monto <= 0:
                print("Error: El monto debe ser mayor que cero.")
            else:
                self.saldo += monto
                self.historial.append(f"Se depositaron ${monto:.2f}")
                self.contador_operaciones += 1
                print("Depósito exitoso.")

        except ValueError:
            print("Error: Ingrese un número válido.")

    # Extraer dinero
    def extraer(self):
        try:
            monto = float(input("Ingrese el monto que desea extraer: $"))

            if monto <= 0:
                print("Error: El monto debe ser mayor que cero.")
            elif monto > self.saldo:
                print("Error: Fondos insuficientes.")
            elif monto > self.limite_extraccion:
                print(f"Error: El monto excede el límite de extracción de ${self.limite_extraccion:.2f}.")
            else:
                self.saldo -= monto
                self.historial.append(f"Se retiraron ${monto:.2f}")
                self.contador_operaciones += 1
                print("Extracción exitosa.")

        except ValueError:
            print("Error: Ingrese un número válido.")

    # Transferir dinero
    def transferir(self):
        try:
            monto = float(input("Ingrese el monto que desea transferir: $"))
            cbu = input("Ingrese el CBU del destinatario: ")

            if monto <= 0:
                print("Error: El monto debe ser mayor que cero.")
            elif monto > self.saldo:
                print("Error: Fondos insuficientes.")
            else:
                self.saldo -= monto
                self.historial.append(f"Transferencia de ${monto:.2f} al CBU {cbu}")
                self.contador_operaciones += 1
                print("Transferencia exitosa.")

        except ValueError:
            print("Error: Ingrese un número válido.")

    # Mostrar historial
    def mostrar_historial(self):
        if len(self.historial) == 0:
            print("\nNo se registraron operaciones.")
        else:
            print("\nHistorial de operaciones:")
            for operacion in self.historial:
                print("-", operacion)

    # Mostrar cantidad de operaciones
    def mostrar_contador(self):
        print(f"\nCantidad total de operaciones realizadas: {self.contador_operaciones}")

    # Guardar datos
    def guardar_datos(self):
        ruta = os.path.join(os.path.dirname(__file__), "datos.txt")

        with open(ruta, "w") as archivo:
            archivo.write(f"{self.usuario}\n")
            archivo.write(f"{self.contrasena}\n")
            archivo.write(f"{self.saldo}\n")
            archivo.write(f"{self.limite_extraccion}\n")


# Programa principal
iniciar = input("¿Desea iniciar sesión? (s/n): ")

if iniciar.lower() == "s":
    try:
        cajero = CajeroAutomatico()

        if cajero.iniciar_sesion():

            while True:
                print("\n===== MENÚ =====")
                print("1. Consultar saldo")
                print("2. Depositar dinero")
                print("3. Extraer dinero")
                print("4. Transferir dinero")
                print("5. Mostrar historial")
                print("6. Mostrar cantidad de operaciones")
                print("7. Salir")

                opcion = input("Ingrese una opción: ")

                if opcion == "1":
                    cajero.consultar_saldo()

                elif opcion == "2":
                    cajero.depositar()

                elif opcion == "3":
                    cajero.extraer()

                elif opcion == "4":
                    cajero.transferir()

                elif opcion == "5":
                    cajero.mostrar_historial()

                elif opcion == "6":
                    cajero.mostrar_contador()

                elif opcion == "7":
                    cajero.guardar_datos()
                    print("\nGracias por usar el cajero automático. ¡Hasta luego!")
                    break

                else:
                    print("Opción no válida. Intente nuevamente.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'datos.txt'.")
        print("Verifique que el archivo esté en la misma carpeta que este programa.")

else:
    print("Sesión no iniciada. ¡Hasta luego!")
