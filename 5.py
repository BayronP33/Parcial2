import numpy as np

m=np.array([2, 8, -14, 3, 1])
l=np.array([5, -2, -1, 7])

def orden_mediana(a):
    orden=np.sort(a)
    cantidad = len(orden)
    if cantidad %2 != 0: 
        mediana = orden[cantidad // 2] 
    else:
        mediana = (orden[cantidad // 2 - 1] + orden[cantidad //2]) / 2 #
        
    return mediana

resultado1=orden_mediana(m)
resultado2=orden_mediana(l)
print(f'la mediana del arreglo de enteros v y w es respectivamente: \n v:{np.sort(m)} \n la mediana es: {resultado1} \n w:{np.sort(l)} \n la mediana es: {resultado2}')