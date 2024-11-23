#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024

def inversa(cadena, valor_extra=''):
    return cadena[::-1] + valor_extra

cadena = input("Ingrese una cadena: ")
valor_extra = input("Ingrese un valor extra (opcional): ")
print("La cadena invertida es:", inversa(cadena, valor_extra))
