#imprime el valor de la posicion 2 del arreglo
numeros=[10,20,30,40,50]
print(numeros[2])
#cambio el valor del arreglo en la posicion 3
numeros[3]=15
print(numeros[3])
#agregamos un valor al arreglo
numeros.append(60)
print(numeros)
#elimino el valor de la posicion 1 del arreglo
numeros.pop(1)
print(numeros)
#elimino el valor 30 del arreglo
numeros.remove(30)
print(numeros)

frutas=["manzana","pera","uva","maracuya","Mango"]
frutas.remove("uva")
print(frutas)
frutas.pop(3)
print(frutas)
frutas.append("fresa")
print(frutas)
frutas[1]="kiwi"
print(frutas)
arreglo=[]
#declare la longitud del arreglo
n=int(input("Ingrese la longitud del arreglo: "))