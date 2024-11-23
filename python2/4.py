#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024

def es_vocal(caracter, valor_extra=0):
    return caracter.lower() in 'aeiou'

caracter = input("Ingrese un carácter: ")
print("Es una vocal:", es_vocal(caracter))
