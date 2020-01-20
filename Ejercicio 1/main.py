from sumar_divisores import *
from array import *

#Vector de valores (obtenidos de Wikipedia) para realizar el test.
Vector=[1, 2, 3, 4, 5, 6, 28, 496, 8128, 12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102]

suma=0 #Inicialiación de la suma a cero.
print("Los valores menos a cero serán calculados en su valor absoluto.")
for valor in Vector: #Recorremos todo el vector de prueba.
    suma=sumar_divisores(valor) #Obtenemos la suma de todos los divisores del valor en la posición "i".
    if suma < valor: #Si la suma es menor al valor es DEFECTIVO.
        print("El valor ", valor, "es DEFECTIVO")
    elif suma == valor: #Si la suma es igual al valor es PERFECTO.
        print("El valor ", valor, "es PERFECTO")
    else: # suma > valor #Si la suma es mayor es ABUNDANTE.
        print("El valor ", valor, "es ABUNDANTE")
