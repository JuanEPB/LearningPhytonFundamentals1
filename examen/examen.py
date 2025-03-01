#formulario para calcular primedio dependiendo de las materias

print('Cual es tu nombre?: ')
nombre = input()

print('Ingresa el numero de materias: ')
materias = int(input())

for i in range(materias):
    print(f'Ingresa la calificacion de la materia #{i+1}: ')
    calificacion = int(input())

    promedio = materias * calificacion /materias

print(f'{nombre.title()} el promedio de su cuatimestre es: {promedio}')
