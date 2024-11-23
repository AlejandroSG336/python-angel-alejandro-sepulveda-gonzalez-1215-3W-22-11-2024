#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024

def sum(lista, valor_extra=0):
    total = valor_extra
    for num in lista:
        total += num
    return total

lista = list(map(int, input("Ingrese una lista de números separados por comas: ").split(',')))
valor_extra = int(input("Ingrese un valor extra (opcional): "))
print("La suma es:", sum(lista, valor_extra))
