#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024

def multip(lista, valor_extra=1):
    total = valor_extra
    for num in lista:
        total *= num
    return total

lista = list(map(int, input("Ingrese una lista de números separados por comas: ").split(',')))
valor_extra = int(input("Ingrese un valor extra (opcional): "))
print("El producto es:", multip(lista, valor_extra))
