# programa1
def suma_lista(lista):
    sumal = 0
    for numeros_en_lista in lista:
        sumal += numeros_en_lista
    return sumal

# suma de los numeros
primera_lista = [2, 4, 6, 8, 10]
resultado = suma_lista(primera_lista)
print("el resultado de la suma de los numeros es:", resultado)

# programa2
def inverso_palabra(cadena_palabras):
    return cadena_palabras[::-1]

# entradas y salidas
entrada = "programacion"
resultado = inverso_palabra(entrada)
print(resultado)  # la salida tendria que ser noicamargorp

# programa3
def suma_numerospares(lista):
    suma = 0
    for nume in lista:
        if nume % 2 == 0:
            suma += nume
    return suma

def main():
    numeros = input("Ingrese una lista de 10 numeros: ")
    lista = [int(x) for x in numeros.split()]
    suma = suma_numerospares(lista)
    print("La suma de los 10 numeros ingresados es:", suma)

if __name__ == "__main__":
    main()

