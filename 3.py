# Desarrollar un algoritmo que dadas dos listas determine que elementos tiene la primera lista que no contenga la segunda

v={2, 8, -14, 3, 1, 15} #1
w={2, 3, 1, 7, 19, 6} #2 no contien con respecto al numero 1  8, -14, 15

def diferencia_elemts(a, b):
    diferencia=set.difference(a, b)
    return diferencia

resultado_elementos_diferentes=diferencia_elemts(v, w)
print(f"Los elementos que contien v que no contien W son:{resultado_elementos_diferentes}")
