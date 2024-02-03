#variable y operadores aritmeticos
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))


suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero."


print("\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#Condicionales (if/else) y Operadores Relacionales:
numero = float(input("ingrese un numero:"))
if numero > 0:
        resultado = "positivo"
elif numero < 0:
        resultado = "negativo"
else: 
        resultado = "cero"
print(f"el numero ingresado es:  {resultado} ")

#Ciclos (while/for) y Operadores Lógicos:
#programa con for
for i in range(2, 21, 2):
    print(i)

#programa con while
    contador = 1
while contador <= 10:
    numero_par = contador * 2
    print(numero_par)
    contador += 1

 #Funciones y Condicionales:
def suma_es_par(numero1, numero2):
    suma = numero1 + numero2
    if suma % 2 == 0:
        return True
    else:
        return False

# Ejemplo de uso
def main():
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))

        resultado = suma_es_par(numero1, numero2)

        print(f"¿La suma de {numero1} y {numero2} es par? {resultado}")

    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

if __name__ == "__main__":
    main()

   


#clases y metodos
class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar_aprobacion(self):
        return self.calificacion >= 60

def main():
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    edad_estudiante = int(input("Ingrese la edad del estudiante: "))
    calificacion_estudiante = float(input("Ingrese la calificación del estudiante: "))

    estudiante = Estudiante(nombre_estudiante, edad_estudiante, calificacion_estudiante)

    if estudiante.verificar_aprobacion():
        print(f"{estudiante.nombre} ha aprobado.")
    else:
        print(f"{estudiante.nombre} no ha aprobado.")

if __name__ == "__main__":
    main()
