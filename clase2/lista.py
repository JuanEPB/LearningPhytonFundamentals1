print('Manejo de listas en PHYTON\n\n')

#eclaracion de una lista
my_list = [1,2,3,4,5,6,7,8,9,10]

print(f'Valores actuales de mi lista: {my_list}')
#agregar elementos de mi lista append, 0 y 11

my_list.append(0)
my_list.append(11)
print(f'Valores modificados de mi lista: {my_list}')

#ordenar los elementos de mi lista mediante sort
my_list.sort()
print(f'Los elementos de mi lista han sido modificados: {my_list}')

# modificar y eliminar un elemento de mi lista
my_list[0] = 'esto es una cadena'
my_list.pop()

print(f'Valores actuales de mi lista, ejemplo POP: {my_list}')
#creacion de una sublistaa [0:5]

my_sublits = my_list[0:5]
print(f'valores actuales de mi sublista: {my_sublits}')

#imprimir los valores de mi lista

print(f'\n\nEstos son los elementos de mi lista, los cuales seran impresos mediante un ciclo for')
count = 0
for item in my_list:
    print(f'Elmento de mi lista {count}, {item}')
    count += 1


