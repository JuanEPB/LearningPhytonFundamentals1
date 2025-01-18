#Otros   metodos
message="Los cuervos  de la   Utvt"

#len
size=len(message)

#replace
new_message =message.replace('',',')

#find
indexOf=new_message.find('U')

#Split
message_sliced=message.split()

print(f'Longitud  de la  cadena :{size}')
print(f'Nueva cadena:{new_message}')
print(f'Posicion del elecmento   buscado :{indexOf}')
print(f'Cadena  particionada:{message_sliced}')
