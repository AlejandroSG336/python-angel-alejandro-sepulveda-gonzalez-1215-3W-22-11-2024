#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024
def max(a, b, valor_extra=0):
    return (a if a > b else b) + valor_extra

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
valor_extra = int(input("Ingrese un valor extra (opcional): "))
print("El mayor es:", max(a, b, valor_extra))
