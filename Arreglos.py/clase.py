matriz = [
[1,2,3],
[4,5,6]
]
print("mostrando la matriz")
for fila in matriz:
    print(fila)
    print("mostrar el 6")
    print(matriz[1][2])
print(matriz[0])
""""Modificar el valor de la matriz"""
matriz[1][1]=8
print("matriz modificada:")
print(matriz)
matriz.append([7,8,9])
print("matriz despues de agregar una fila:")
print(matriz)
matriz[0].pop(2) #Elimina el segundo elemento de la primera fila
print("matriz despues de eliminar un elemento:")
print(matriz)
from collections import deque
#1.crear la cola (fila de personas)
cola=deque(["Ana","Carlos"])
cola.append("jorge")
cola.append("Andres")
print("cola actual:",cola)
atendido = cola.popleft()
print(f"Se atendió a: {atendido}")

print("Cola nestante:",cola)

atendido = cola.popleft()
print(f"Se atendió a: {atendido}")
print("Cola restante:", cola)