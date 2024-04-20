# #ejercicios 1
# for i in range (5):
#    print (i)

# #ejercicio 2

# for i in "hola":
#     print (i)

#  #ejercicio 3
# for i in range (5):
#     i = i+2
#     print (i)

# #ejericio 4
# num1 = int(input("ingrese una variable numerica\n"))
# i = 1
# fact = 1
# while i<=num1:
#     fact = fact * i
#     i += 1
# print(f"el resultado de {num1} es {fact}")

#ejercicio 5

# while True:
#     numero = int(input("ingrese un numero\n"))
#     if  numero%2==0:
#         print("ERROR")
#         continue
#     else:
#         aux=numero*4
#         print(f"el {numero} multiplicado por 4 es: {aux}")
#         break

#ejercicio 6
# resultado = 1
# base = int(input("ingrese base\n"))
# exponente = int(input("ingrese exponente\n"))
# for i in range (exponente):
#     resultado = resultado * base
# print (f"el resultado {base} elevado a {exponente}")

#ejercicio 10
num2 = 1
num = int(input("ingrese un numero entero entre 7 y 10"))
while num <= 1000:
    print(num)
    (num,num2) = (num2, num+num2)
    

numero = int(input("ingrese numero\n"))
esPrimo = True
if numero <= 1:
    esPrimo = False
else:
    for i in range (2, int(numero**0.5) + 1):
        if numero%i==0:
         esPrimo = True
        break

if esPrimo:
    print(f"el numero {numero} es primo")
else:
    print(f"el numero {numero} no es primo")
    
    





