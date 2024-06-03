
def lenCaserito (secuencia):
    """
    Return the number of items in a container.
    Hola clase!!! Comision campeona
    """
    contador = 0
    for iterable in secuencia:
        contador = contador + 1
    return contador

cantidad = lenCaserito("Hola")

print(cantidad)     
print(lenCaserito([4,5,True,"",3.5]))   
