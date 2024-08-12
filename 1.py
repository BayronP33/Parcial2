# desarrollar un programa que determine si en una lista no existen elementos repetidos
v = [-1, -3, 4, -5, 6]
w = [-1, -1, 4, 4]



def elementos_rep(a):
    tamaño=len(a)
    eliminar_rep=set(a)
    cantidad_set=len(eliminar_rep)
    if tamaño != cantidad_set:
        return 'Hay elementos repetidos'
    else:
        return 'No hay elementos repetidos'
    
resultado=elementos_rep(v)
resultado_w=elementos_rep(w)
print(f"En la lista v {resultado} \nEn la lista w {resultado_w}")