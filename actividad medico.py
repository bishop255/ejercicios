import os, time
banderaEdad = True
menu = True
banderaRut = True
banderaPaciente = True

while menu:
    try:
        print("\t\t CENTRO MEDICO DUOC")
        print("1. Registrar Paciente")
        print("2. Atencion Paciente")
        print("3. Consultar datos del Paciente")
        print("4. Salir")
        opcion = int(input("ingrese una opcion\n"))
        
        if opcion == 1:
            os.system("cls")
            print("\t\t***Registrar Paciente***")
            while banderaRut:
                    try:
                        rut = int(input("Ingrese rut del paciente sin digito verificador\n"))
                        while rut < 500000 or rut > 99999999:
                            rut = int(input("Ingrese rut del paciente sin digito verificador\n"))
                            banderaRut = False
                    except:
                        print("el campo edad no recibe texto ni simbolos")
            nombre = input("Ingrese el nombre del paciente\n")
            while not nombre:
                nombre = input("Ingrese el nombre del paciente, no puede ir una cadena de texto vacia\n")
            direccion = input("ingrese la direccion del paciente\n")
            while not direccion:
                direccion = input("ingrese la direccion del paciente, no puede ir cadena de texto vacia\n")
            correo = input("Ingrese el correo del paciente\n")
            while not "@" in correo:
                print("Correo invalido")
                correo = input("Ingrese el correo del paciente que sea valido\n")
            sexo = input("Ingrese sexo del paciente F = Femenino  M = Masculino\n").upper()
            while (sexo == "F") and (sexo == "M" ):
                print("Sexo registrado correctamente")
            else:
                print("Verifique que los datos que ingresan son correctos")
                time.sleep(1)
                sexo = input("Ingrese sexo del paciente F = Femenino  M = Masculino\n").upper()
            ps = input("Ingrese que grupo perteneciente el paciente: ISAPRE O FONASA\n").upper()
            while (ps == "ISAPRE") and (ps== "FONASA"):
                ps = input("Ingrese que grupo perteneciente el paciente: ISAPRE O FONASA (verifique que este en mayusuculas\n)").upper()
                while banderaEdad:
                    try:
                        edad = int(input("ingrese edad\n"))
                        while edad < 18 or edad > 110:
                            edad = int(input("ingrese edad entre rango 18 y 110\n"))
                            banderaEdad = False
                    except:
                        print("el campo edad no recibe texto ni simbolos")
            registro = ""
        
        elif opcion == 2:
            os.system("cls")
            print("\t\t***Atencion Paciente***")
            while banderaPaciente:
                try:
                    id_paciente = input("Ingrese rut sin digito verificador del paciente\n")
                    if rut == id_paciente:
                        print("Paciente Registrado")
                        fecha = input("Ingrese la fecha\n")
                        registro = input("Ingresa las observaciones de la visita\n")
                        banderaPaciente = False
                    else:
                        print("Paciente invalido")
                except:
                    print("no se acepta caracteres especiales")
            
        elif opcion == 3:
            os.system("cls")
            print("\t\t***Consultador datos del paciente***")
            
        elif opcion == 4:
            os.system("cls")
            print("Ha finalizado el programa")
            x = input ("presione enter para continuar")
            menu = False
            
            
    except:
        print("Opcion no existe")