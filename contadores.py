# Sistema de Compra
import time, os
contadorProductos = 0
acumuladorPrecios = 0
Bienvenido = "Bienvenido selecciona con 1.SI o 2.NO los productos que desea agregar a su carrito de compra\n"
print(Bienvenido)

productos = int(input("Desea agregar agua por $600?   1.Si  2.NO\n"))
if productos == 1:
    contadorProductos += 1
    acumuladorPrecios += 600
    
productos = int(input("Desea llevar azucar por $1200  1.SI   2.NO\n"))
if productos == 1:
    contadorProductos +=1
    acumuladorPrecios += 1200
    
productos = int(input("Desea llevar aceite por $1500  1.SI  2.NO\n")) 
if productos == 1:
    contadorProductos += 1
    acumuladorPrecios += 1500
    
productos = int(input("Desea llevar fideos por $790  1.SI  2.NO\n"))
if productos == 1:
    contadorProductos += 1
    acumuladorPrecios += 790

productos = int(input("Desea llevar bebida por $1780  1.SI   2.NO\n"))
if productos ==1:
    contadorProductos += 1
    acumuladorPrecios += 1780
    
productos = int(input("Desea llevar chocolate por $2500  1.SI  2.NO\n"))
if productos == 1:
    contadorProductos += 1
    acumuladorPrecios += 2500
    
productos = int(input("Desea llevar pan de molde por $1340  1.SI  2.NO\n"))
if productos == 1:
    contadorProductos += 1
    acumuladorPrecios += 1340
    
print(f"LLeva acumulado un total de {contadorProductos} productos y en precio: ${acumuladorPrecios} a pagar")
time.sleep(2)

preferencial = int(input("Usted es cliente preferencial?  1.SI  2.NO\n"))
if preferencial == 1:
    total = acumuladorPrecios * 0.75
    descuento = acumuladorPrecios * 0.25
else:
    total = acumuladorPrecios
    descuento = 0
print(f"su descuento por cliente preferencial es: ${descuento}")
print(f"total a pagar en su compra es: ${total}")

pago = int(input("Ingrese su forma de pago 1.EFECTIVO  2.CREDITO/DEBITO\n"))
if pago == 1:
    efectivo = int(input("Ingrese la cantidad de efectivo"))
    if efectivo < total:
        print("SALDO INSUFICIENTE, GUARDIAS!!")
    else:
        vuelto = efectivo - total
        print("Muchas gracias")
        print(f"Su vuelto es: ${vuelto}")
else:
    print("No olvides llevar tu voucher")
    print("HASTA PRONTO!!!")
            
