print('Ejemplo del uso de colecciones tipo SET')

#definir ejemplos con colecciones
first_colection = {1, 2, 3, 4, 5}
second_colection = {3, 4, 5, 6, 7, 8}

#imprimir el contenido de una coleccion tipo SET
print(f'Mi coleccion de tipo SET: {first_colection}')

#Remover un elemento de la coleccion
first_colection.remove(4)
print(f'Mi coleccion actualizada: {first_colection}')

#Agregar un elemento a una coleccion

first_colection.add('HELLO WORLD!')
print(f'Mi coleccion actualizada, ADD: {first_colection}')

#iteracion sobre una coleccion con un ciclo FOR

print('\n\nImpresion del contenido de la coleccion\n')
for item in first_colection:
    print(item)
#Operaciones con colecciones

union_set = first_colection.union(second_colection)
intersection_set = first_colection.intersection(second_colection)
diference_set = first_colection.difference(second_colection)
print(f'\nUnion de colecciones: {union_set}')
print(f'Intersection de colecciones: {intersection_set}')
print(f'Diferencia de colecciones: {diference_set}')