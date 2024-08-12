import array
clave=array.array('i',[2, 8, 14, -2, 8])
def main():
    def promedio(a):
        suma=sum(a)
        cantidad=len(a)
        p=suma/cantidad
        return p
    resultado=promedio(clave)
    print(f'el promedio de el array clave con los elementos {list(clave)} es igual a {resultado}' )
if __name__=='__main__':
    main()