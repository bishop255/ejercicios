mensaje = "hola mundo"

print (mensaje)

#Ejercicio 1 y 2
a = "Bienvenido al mundo de la programación"
print (a)

nom = (input("Para comenzar, ingresa tu nombre\n"))
print (f"Bienenido {nom}")

#Ejercicio 3

print ("ingrese un valor para x y podras resolver la siguiente ecuacion")
x = int(input("(X^2+3X+1)/4\n"))
formula = (x**2+3*x+1)/4
print(f"el resultado de la operacion con el valor {x} es: {formula}")

#ejercicio 4

nombre = input ("Ingrese su nombre\n")
rut = input ("ingrese su rut\n")
correo = input ("ingrese su correo\n")
telefono = input ("ingrese su numero de telefono\n")
print ("Datos personales")
print ("Nombre: \t", nombre.upper())
print ("RUT: \t", rut)
print ("Correo: \t", correo.upper())
print ("Telefono: \t", telefono)
