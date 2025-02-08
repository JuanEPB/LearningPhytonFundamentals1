

def saludar():
    print("Hola mundo desde una funcion")

#funcion con argumentos
def sumar_numeros(numero_x, numero_y):
    suma = numero_x + numero_y
    print(f"El resultado es: {suma}")
    return suma

#funcion con valores por defecto
def valores_por_defecto_suma(numero_x = 0, numero_y = 1, numero_z = 2):
    suma = numero_x + numero_y + numero_z
    print(f"El resultado de la suma con valore por defecto: {suma}")
    return suma


def alumnos_materias(nombre, *args):
    print(f"Nombre {nombre}, materias  {args}")
    print(f'Nombre: {type(nombre)}, materias: {type(nombre)}')
def alumno_calificaciones(nombre, **kwargs):
    print(f'Nombre: {nombre}, calificaciones: {kwargs}')
    print(f'Nombre: {type(nombre)}, calificaciones: {type(kwargs)}')

#saludar()
#sumatoria = sumar_numeros(10, 20)
#print(f"El resultado es: {sumatoria}"'')
#sumatoria = valores_por_defecto_suma(numero_x = 10, numero_y = 20,)
alumnos_materias('Juan','programacio','matematicas','ingles')
alumno_calificaciones(nombre='Juan', programacion=10, matematicas=9, ingles=10)