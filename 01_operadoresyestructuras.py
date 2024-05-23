"""
/*
 * EJERCICIO:
  1- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
  2- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
  3- Debes hacer print por consola del resultado de todos los ejemplos.
 
  4 DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 """

#1 -------------------------------OPERADORES--------------------------------

# OPERADORES ARITMETICOS

print(f'suma: 4 + 2 ={4+2}')
print(f'resta: 4 - 2 ={4-2} ')
print(f'multiplicacion: 4 X 2 = {4*2}')
print(f'division: 4 / 2 = {4/2}')
print(f'modulo: 4 % 2= {4%2}')
print(f'exponente: 4 ** 2 = {4**2}')
print(f'division entera: 4 // 2 = {4//2}')

# OPERADORES DE COMPARACION

print(f'igualdad: 10 == 3 es {10==3}')
print(f'desigualdad: 10 != 3 es {10!=3}')
print(f'Mayor que: 10 > 3 es {10>3}')
print(f'Menor que: 10 < 3 es {10<3}')
print(f'Mayor o igual que: 10 >= 3 es {10>=3}')
print(f'Menor o igual que: 10 <= 3 es {10<=3}')

# OPERADORES LOGICOS

print(f'AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10+3==13 and 5-1==4}')
print(f'OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10+3==13 or 5-1==4}')
print(f'NOT !: not 10 + 3 == 14 es {not 10+3==14}')

# OPERADORES DE ASIGNACION

my_number = 11 #Asignacion
print(my_number)

my_number += 1 #Suma y asignacion
print(my_number)

my_number -= 1 #Resta y asignacion
print(my_number)

my_number *= 2 #Multiplicion y asignacion 
print(my_number)

my_number /= 2 #Division y asignacion
print(my_number)

my_number %= 2 #Modulo y asignacion
print(my_number)

my_number **= 1 #Exponente y asignacion
print(my_number)

my_number //= 1 #Division entera y asignacion
print(my_number)

# OPERADORES DE IDENTIDAD

my_new_number = my_number
print(f'my_number is my_new_number es {my_number is my_new_number}')
print(f'my_number is not my_new_number es {my_number is not my_new_number}')

# OPERADORES DE PERTENENCIA

print(f"'u' in 'Mouredev' = {'u' in 'Mouredev'}")
print(f"'u' not in 'Mouredev' = {'u' not in 'Mouredev'}")

# OPERADORES DE BIT

a = 10 #1010
b = 3 #0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

# 2 y 3 ----------------ESTRUCTURAS DE CONTROL--------------------

# Condicionales

my_string = 'Santiago'

if my_string == 'Emmanuel':
    print('my string is Emmanuel')
elif my_string == 'Santiago':
    print('My string is Santiago')

else:
    print('My string is not Emmanuel ni Santiago')    


# Iterativas

for i in range(6):
    print(i)

i = 3
while i <= 10:
    print(i)
    i += 1

# Excepciones
try:
    print(10 / 0)
except:
    print('Se ha producido un error')
finally:
    print('Ha finalizado el manejo de errores')

# 4 --------------------------------DIFICULTAD EXTRA----------------------------------------
"""Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

for number in range(10,56):
    if number % 2 == 0 and number != 16 and number & 3 != 0:
        print(number)
