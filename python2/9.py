#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024

def superposicion(lista1, lista2, valor_extra=None):
    if valor_extra is not None:
        lista2.append(valor_extra)
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1 == elem2:
                return True
    return False

lista1 = input("Ingrese la primera lista de elementos separados por comas: ").split(',')
lista2 = input("Ingrese la segunda lista de elementos separados por comas: ").split(',')
valor_extra = input("Ingrese un valor extra (opcional): ")
print("Tienen elementos en común:", superposicion(lista1, lista2, valor_extra))
