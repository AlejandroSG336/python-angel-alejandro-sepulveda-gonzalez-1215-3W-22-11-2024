#angel-alejandro-sepulveda-gonzalez-1215-3W-22-11-2024

def longitud(secuencia, valor_extra=0):
    contador = 0
    for _ in secuencia:
        contador += 1
    return contador + valor_extra

secuencia = input("Ingrese una cadena o lista (como 'a,b,c'): ").split(',')
valor_extra = int(input("Ingrese un valor extra (opcional): "))
print("La longitud es:", longitud(secuencia, valor_extra))
