#          0 A 30      31 A 60      61 A 80     81 A 100
score=(["BAJO", 0, 30],["MEDIO", 31, 60],["ALTO", 61, 80],["SUPERIOR", 81, 100])

#print(score[:])
#print(score[1:])
#print(score[:1])
#print(score[1:1])
#print(score[1:-1:2]) 
print(score[::-1])

def funcion(nota):
    for i, n in enumerate(score, start=1):
        if(nota >= n[1] and nota <= n[2]):
            print(f"la nota es: {i} - {n[0]}")
            break

def promedios():
    mensaje="Notas: \n"
    for i, n in enumerate(score, start=1):
        
        nombre, min, max = n
        
        mensaje+= promedioNota(posicion= i, nombre= nombre, rango=[min, max]) + "\n"
        #mensaje += f"{i}. {n[1]} a {n[2]} -> {n[0]} \n"
    return mensaje
    
def promedioNota(posicion: int, nombre: str, rango: list):
    return f"{posicion}. {rango[0]} a {rango[1]} -> {nombre}"


nota=float(input("ingrese la nota del alumno: "))
print(promedios())
funcion(nota)
#
#
