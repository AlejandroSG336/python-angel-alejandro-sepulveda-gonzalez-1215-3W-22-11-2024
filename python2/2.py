#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024

def max_de_tres(a, b, c, valor_extra=0):
    return max(a, b, c) + valor_extra

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
valor_extra = int(input("Ingrese un valor extra (opcional): "))
print("El mayor es:", max_de_tres(a, b, c, valor_extra))
