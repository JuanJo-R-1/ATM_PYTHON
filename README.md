# Ingresar una cifra X y vamos a calcular cuantos
#billetes de 50,20,10 y 5 tenemos que devolverle al usuario

dinero_disponible=[10, 8, 10, 30]

def mostrarDisponible(montos):
   print(f"disponible $")
   print(f"50k: {montos[0]}\n20k: {montos[1]}",
       f"\n10k: {montos[2]}\n5k: {montos[3]}")
   
def validarMonto():
   cantidad=-1
   while True:
      cantidad = int(input("ingrese la cantidad de $ a retirar: "))
      if not cantidad %5_000 !=0:
         input("ingrese un monto valido huevón, solo multiplos de ", [denominacion])
   else: 
      return cantidad
   
def validarDenominacionMenor(denominacion):
   can = len(denominacion)
   for item in range(can):
      if item ==0:
         temp = 50_000
      elif item ==1:
         temp = 20_000
      elif item ==2:
         temp = 10_000
      else:
         temp = 5_000
   pass

denominacion=validarDenominacionMenor(denominacion= dinero_disponible)
print(f"la minima{denominacion}")
mostrarDisponible(montos=dinero_disponible)

cantidad = validarMonto()
       
can_50 = 0
can_20 = 0
can_10 = 0
can_5 = 0
total = cantidad

while cantidad > 0:

    if total >= 50_000:
       can_50 = can_50 + 1
       total = total - 50_000
       dinero_disponible[0]=dinero_disponible[0]-1
    elif total >= 20_000:
       can_20+=1
       total-= 20_000
       dinero_disponible[1]-=1
    elif total >= 10_000:
       can_10+=1
       total-= 10_000
       dinero_disponible[2]-=1
    elif total >= 5_000:
       can_5 +=1
       total-= 5_000
       dinero_disponible[3]-=1
    elif total==0:
       break
    else:
       print("no tenemos tal semejante cantidad de dinero bro")


print(f"la cantidad a devolver es de {cantidad}\n50k: {can_50}\n20k {can_20}",
      f"\n10k {can_10}\n5k {can_5}")


mostrarDisponible(montos= dinero_disponible)
