import os, time

usu = "admin"
passw = 1234
menu = True


while menu:
    try:
        print("\t\t BIENVENIDO AL HOTEL PARADISE DREAMS")
        print ("\t\t Sistema de Gestión de Huéspedes")
        print ("1. Registrar Huesped")
        print ("2. Consultar Datos de Huésped")
        print ("3. Salir")
        opcion = int(input("Ingrese una opcion\n"))
        
        if opcion == 1:
            os.system("cls")
            print("\t\tRegistrar Huesped")
            nombre = input("Ingrese el nombre del huesped\n")
            while not nombre:
                nombre = input("Debe ingresar un nombre del huesped, no puede ir cadena de texto vacia\n")
            direccion = input("Ingrese la direccion del huesped\n")
            while not direccion:
                direccion = input("Ingrese la direccion del huesped, no puede ir una cadena de texto vacia\n")
            numero_reserva = int(input("Ingrese el numero de reserva del huesped\n"))
            while numero_reserva < 1000 or numero_reserva > 9999:
                numero_reserva = int(input("Ingrese el numero de reserva del huesped dentro del rango 1000 y 9999\n"))
            edad = int(input("Ingrese la edad del huesped\n"))
            while edad < 18 or edad > 120:
                edad = int(input("Ingrese la edad del huesped, dentro del ragno de 18 a 120 años\n"))
            correo = input("Ingrese el correo del huesped\n")
            while not "@" in correo:
                correo = input("CORREO INVALIDO\n porfavor ingreselo nuevamente\n")
            numero_acompañantes = int(input("Ingrese el numero de acompañantes del huesped\n"))
            while numero_acompañantes < 0:
                numero_acompañantes = int(input("Ingrese un numero valido, tiene que ser mayor o igual a 0\n"))
        
        elif opcion == 2:
            os.system("cls")
            print ("\t\tConsultar Datos de Huésped")
            print ("\t\tBIENVENIDO")
            usuario = input("Ingrese su usuario\n")
            password = int(input("Ingrese su clave de digitos\n"))
            if (usuario == usu) and (password == passw):
                print("Ingreso correcto")
            else:
                print("Usuario o clave incorrecto")
                usuario = input("Ingrese su usuario\n")
                password = int(input("Ingrese su clave de digitos\n"))
            
            consultador = int(input("Ingrese el numero de reserva\n"))
            if consultador == numero_reserva:
                print(f"Nombre del huesped: {nombre}")
                print(f"Direccion del huesped: {direccion}")
                print(f"Edad del huesped: {edad}") 
                print(f"Correo del huesped: {correo}")
                if numero_acompañantes > 0 and numero_acompañantes < 2:
                    print("Huesped dentro del limite de acompañantes")
                else:
                    print("Huesped con demasiados acompañantes")
                time.sleep(2)
                print("Pulsa espacio para continuar")
                espacio = input(" ")
            else:
                print("Numero de reserva invalido")
        
        elif opcion == 3:
            print("Gracias por preferir Hotel Paradise Dreams")
            print("Programa finalizado...")
            menu = False
    except:
        print("No existe")