#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024

def generar_n_caracteres(n, caracter, valor_extra=''):
    return (caracter * n) + valor_extra

n = int(input("Ingrese el número de repeticiones: "))
caracter = input("Ingrese un carácter: ")
valor_extra = input("Ingrese un valor extra (opcional): ")
print("Cadena generada:", generar_n_caracteres(n, caracter, valor_extra))
