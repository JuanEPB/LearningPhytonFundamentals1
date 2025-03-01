result = None
numero_x = 10
numero_y = 2

try:
    numero_x = float(input("Ingresa un numero para x: "))
    numero_y = float(input("Ingresa un numero para y: "))
    result = numero_x / numero_y
    print(f'el resultado es: {result}')
except ZeroDivisionError as e:
    print(f'la excepcion es la siguiente: {e}')
except ValueError as e:
    print(f'la excepcion de value error  genero el siguiente mensahe: {e}')
finally:
    print(f'Nuestro programa ha finalizado')