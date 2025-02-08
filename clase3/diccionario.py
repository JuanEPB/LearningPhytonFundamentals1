student = {
    'name': 'pedrito perez',
    'age': 25,
    'language': 'python',
    'city': 'Lerma'
}
#Acceso a los valores de un diccionario
print(f'Contenido de los estudiante: {student}')
print(f'\n Nombre: {student["name"]}')
print(f'\n Edad: {student["age"]}')


print('----- Operqciones basicas sobre dicionarios -----')

#modificar los valores de un dicionario
student ['language'] = 'C#'
print(f'Contenido actual del estudiante una vez modificado el lenguaje: {student}')

#eliminar un elemento del diccionario
student.pop('city')
print(f'\nContenido del estudiante una vez eliminada la ciudad: {student}')


#Agregar un nuevo elemnto
student['food'] = 'Galletas'
print(f'Contenido del estudiante una vez agregada una nueva propiedad: {student}')

print('\n\n\n ---- Iterar sobre un diccionario ----')
print('\nInteracion de los elementos en un diccionario, simple ')

for elemento in student:
    print(f'{elemento}: {student[elemento]}')

print('\nInteracion de los elementos en un diccionario, destruturacion - unpacking ')
for key, value in student.items():
    print(f'Llave: {key}, Valor:{value}')

print('\nInteracion de los elementos en un diccionario, Llaves ')
for key in student.keys():
    print(f'Llave: {key}')

print('\nInteracion de los elementos en un diccionario, Valores ')
for value in student.values():
    print(f'Valor: {value}')