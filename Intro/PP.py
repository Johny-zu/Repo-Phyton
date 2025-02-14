# Variables y tipos de datos
entero = 10
flotante = 10.5
cadena = "Hola, mundo"
booleano = True

# Listas
lista = [1, 2, 3, 4, 5]

# Diccionariosa
diccionario = {"clave1": "valor1", "clave2": "valor2"}

# Condicionales
if entero > 5:
    print("El número es mayor que 5")
else:
    print("El número es 5 o menor")

# Bucles
# Bucle for
for numero in lista:
    print(numero)

# Bucle while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Funciones
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Mundo"))

# Clases y objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"

persona = Persona("Juan", 30)
print(persona.presentarse())