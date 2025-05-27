palabras = []

palabras.append("Python")
palabras.append(5)
palabras.append(True)
palabras.append(input("ingrese un descripcion: "))

palabras[0, "ID: 2"]

print("Por elementos:")
for item in palabras:
    print(item)

palabras[3]=False

print("Por elementos despues del update:")
for item in palabras:
    respuesta=input(f"Quiere actualizar el valor de: {item}\ns\\n")
    if respuesta=="s":
        # palabras[x] = ""
        item=input("ingrese el nuevo valor: ")
    print(f"Valor nuevo: {item}")

print("Por elementos final:")
for item in palabras:
    print(item)


#for indice in range(len(palabras)):
#    print(indice)
#    print(type(indice))
#    print(palabras(indice))
#    print(type(palabras[indice]))