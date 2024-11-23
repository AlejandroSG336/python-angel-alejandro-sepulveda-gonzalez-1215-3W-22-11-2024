#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024

def es_palindromo(cadena, valor_extra=''):
    invertida = cadena[::-1] + valor_extra[::-1]  # Inversión de cadena con valor_extra si existe
    return (cadena + valor_extra) == invertida

cadena = input("Ingrese una palabra: ")
valor_extra = input("Ingrese un valor extra (opcional): ")
print("Es palíndromo:", es_palindromo(cadena, valor_extra))
