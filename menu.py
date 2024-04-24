import time, os
import sys

usuario1=None 
usuario2=None 
usuario3=None
contrasena1=None 
contrasena2=None 
contrasena3=None

menu = True

while menu: 
    print(" 1. INICIAR SESION\n 2. REGISTRAR USUARIO\n 3. SALIR\n")
    opcion = int(input("Ingrese una opcion\n"))
    if opcion == 1:
        print ("1. INICIAR SESION")
        if (usuario1 == None and contrasena1 == None) and (usuario2 == None and contrasena2 == None) and (usuario3 == None and contrasena3 == None):
         print ("Necesario registrar un usuario antes")
         continue
        else:
            usu = input("ingrese usuario\n")
            if usu == usuario1:
                print("Usuario correcto")
            contr = input("Ingrese contraseña\n")
            if contr == contrasena1:
             print("Sesion Iniciada")
            else:
                print("Usuario o clave incorrecta")
    elif opcion == 2:
        print ("2. Registrar Usuario")
        usuario1 = input("Ingrese usuario\n")
        contrasena1 = input("Ingrese su clave\n")
        opc = int(input("Desea agregar mas usuarios?\n 1.SI\n 2.NO\n"))
        time.sleep(2)
        if opc == 1:
            usuario2 = input("Ingrese usuario\n")
            contrasena2 = input("Ingrese su clave\n")
            opc =int(input("Desea agregar mas usuarios?\n 1.SI\n 2.NO\n"))
            if opc == 1:
                usuario3 = input("Ingrese usuario\n")
                contrasena3 = input("Ingrese su clave\n")
                print(f"usuario: {usuario1}")
                print(f"clave: *******")
                print(f"usuario: {usuario2}")
                print(f"clave: *******")
                print(f"usuario: {usuario3}")
                print(f"clave: *******")
        
            
            
        
         
        
    
        
    
