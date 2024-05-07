import os, time

menu = True

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
            print("\t\tRegistrar Paciente")
            rut = int(input("Ingrese rut del paciente sin digito verificador\n"))
            while rut <= 500000 or rut >= 99999999:
                rut = int(input("Ingrese rut del paciente sin digito verificador\n"))
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
            sexo = input("Ingrese sexo del paciente F = Femenino  M = Masculino\n")
            while (sexo == "F" and "f") or (sexo == "M" and "m"):
                print("Sexo registrado correctamente")
            else:
                print("Verifique que los datos que ingresan son correctos")
                time.sleep(1)
                sexo = input("Ingrese sexo del paciente F = Femenino  M = Masculino\n")
            ps = input("Ingrese que grupo perteneciente el paciente: ISAPRE O FONASA\n")
            while not "ISAPRE" or "F" in ps:
                ps = input("Ingrese que grupo perteneciente el paciente: ISAPRE O FONASA (verifique que este en mayusuculas\n)")
        
        elif opcion == 2:
            os.system("cls")
            print("\t\tAtencion Paciente")
            id_paciente = input("Ingrese rut sin digito verificador del paciente\n")
            if rut == id_paciente:
                print("Paciente Registrado")
                fecha = input("Ingrese la fecha\n")
                observacions = input("Ingresa las observaciones de la visita\n")
                
            else:
                print("Paciente invalido")
            
            
            
                
                
            
        
    except:
        print("Opcion no existe")