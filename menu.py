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
        print ("1.INICIAR SESION")
        if (usuario1 == None and contrasena1 == None) and (usuario2 == None and contrasena2 == None) and (usuario3 == None and contrasena3 == None):
         print ("Necesario registrar un usuario antes")
         time.sleep(2)
         continue
        
        else:
            usu = input("ingrese usuario\n")
            contr = input("Ingrese contraseña\n")
            if (usu == usuario1 and contr == contrasena1) or (usu == usuario2 and contr == contrasena2) or (usu == usuario3 and contr == contrasena3):
             print("Sesion Iniciada")
             
             while True:
                  print("1.Realizar llamada")
                  print("2.Enviar correo electronico")
                  print("3.Cerrar cesion")
                  opc2 = int(input("Ingrese una opcion\n"))
                  if opc2 == 1:
                      print("1.Realizar llamada")
                      numero = int(input("Ingrese un numero de celular de 9 digitos empezando con 9\n"))
                      if len(numero) == 9 and numero.startswith('9'):
                         print(f"LLAMANDO AL NUMERO {numero}")
                         time.sleep(2)
                      else:
                         print("Numero ingresado invalido")
                         time.sleep(2)
                         continue
                  elif opc2 == 2:
                         print("2.Enviar correo electronico")
                         correo = input("Ingrese un correo electronico\n")
                         while not ("@") in correo:
                             print("CORREO INVALIDO, PORFAVOR INGRESE OTRO")
                             break
                         else:
                             print("CORREO INGRESA CORRECTAMENTE")
                             mensaje = input("Ingrese el mensaje que desea enviar:\n")
                             print("Mensaje enviado")
                             time.sleep(1)
                  elif opc2 == 3:
                      print("CESION FINALIZADA")
                      break
                         
            else:
             print("Usuario o clave incorrecta")
        
    elif opcion == 2:
        print ("2.REGISTRAR USUARIO")
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
            else:
                print(f"usuario: {usuario1}")
                print(f"clave: ****")
                print(f"usuario: {usuario2}")
                print(f"clave: ****")
        else:
         print(f"usuario: {usuario1}")
         print(f"clave: ****")
    elif opcion == 3:
        print("HASTA LUEGO")
        menu = False
        
         
        
            
            
        
         
        
    
        
    
