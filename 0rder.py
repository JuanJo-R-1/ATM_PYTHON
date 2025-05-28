numeros=[2,6,9,2,1,0,3,2,7,5,3]
numeros.sort(reverse=True)
print(numeros)

print("_______________________________________________________________")

Frase='!elbiercni'
Invertir=Frase[::-1]
print(Invertir)

print("_______________________________________________________________")

lista=[3,9,1]
lista.sort(reverse=True)
print(lista)

print("_______________________________________________________________")

Orden=[3,9,1]

if Orden[0] < Orden[1] or Orden[0] > lista[2]:
    temp=Orden[1]
    Orden[1]=Orden[0]
    Orden[0]=temp

if Orden[1] < Orden[2]:
    temp=Orden[2]
    Orden[2]=Orden[1]
    Orden[1]=temp

print(Orden)

print("_______________________________________________________________")
#    0 1 2
Mix=[3,9,4,7]

def ordenar():
    for izq in range(len(Mix)-1):
        for der in range(izq + 1, len(Mix)):
            if Mix[izq] < Mix[der]:
                tem=Mix[izq]
                Mix[izq]=Mix[der]
                Mix[der]=tem
            pass
        print(f"der: {Mix}")
    print(f"izq. {Mix}")
ordenar()
