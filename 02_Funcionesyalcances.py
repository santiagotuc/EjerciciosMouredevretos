"""
  EJERCICIO:
  1- Crea ejemplos de funciones básicas que representen las diferentes
    posibilidades del lenguaje:
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
  2- Comprueba si puedes crear funciones dentro de funciones.
  3- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
  4- Pon a prueba el concepto de variable LOCAL y GLOBAL.
  5- Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 
  6 DIFICULTAD EXTRA (opcional):
  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 
  Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
  Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""


# 1  ----------------------Funciones definidas por el usuario---------------------------

# Simple

def greet():
    print('Hola a todos')

greet()

# Con retorno

def return_greet():
    return('Hola de nuevo')

print(return_greet())

# CON UN ARGUMENTO

def greet(name):
    print(f'Hola, {name}')

greet('santiago')    

# CON ARGUMENTOS

def arg_greet(greet, name):
    print(f'{greet} {name}')

arg_greet('Saludos', 'santiago')
arg_greet(name='santiago', greet='Saludos')

# Con un argumento predeterminado


def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")


default_arg_greet()
default_arg_greet("Santiago")

# Con argumentos y return


def return_args_greet(greet, name):
    return f"{greet}, {name}!"


print(return_args_greet("Hi", "Brais"))

# Con retorno de varios valores


def multiple_return_greet():
    return "Hola", "Python"


greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos


def variable_arg_greet(*names):
    for name in names:
        print(f'Hola, {name}!')

variable_arg_greet('Santiago', 'Franchu', 'Cyntia')  

# Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{key} ({value})!")

variable_key_arg_greet(
    Nombre='Santiago',
    Apellido='Molina',
    Edad= '30',
    alias='Santiagotuc'
)        
   


# 2  -----------------------------Funciones dentro de funciones-------------------------------------



def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()

outer_function()    



# 3 ------------------------------Funciones del lenguaje (built-in)----------------------------------


print(len('santiago'))
print(type(30))
print('santiago'.upper())

# 4 Y 5 ------------------------------Variables locales y globales----------------------------------

global_var = "Python"

print (global_var)

def hello_python():
    print(f"hola, {global_var}!")

hello_python()
#-----------------------------------------------------------------------------------------------
    
global_var = "Python"
def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")


hello_python()

#--------------------------------------------------------------------------------------------

def hello_python():
    local_var = "Hola"
    print(f"{local_var}!")

hello_python()    

# 6 ---------------------------------------------EXTRA--------------------------------------

""" DIFICULTAD EXTRA (opcional):
  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 
  Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
  Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""  

def print_number(text1,text2) -> int:
    count= 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2) 
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        
        else:
            print(number)    
            count += 1
    return count             

    

print(print_number("fizz","buzz"))       