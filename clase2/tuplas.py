print('ejemplo de tuplas \n\n')

#definicion de tuplas

tupla_information = ('Ana', 22, 95.5)
print(f'tupla_information: {tupla_information}')

#desestrcuturacion o unpacking

full_name, age, salary = tupla_information
print(f'Nombre: {full_name}, age: {age}, salary: {salary}')

print(f'\n\nImpresion de una tupla con un ciclo FOR \n')
# Impresion de los elemntos de una tupla
for item in tupla_information:
    print(item)