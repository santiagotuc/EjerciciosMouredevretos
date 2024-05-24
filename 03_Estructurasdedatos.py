"""
  EJERCICIO:
  1- Muestra ejemplos de creación de todas las estructuras soportadas por defecto
    en tu lenguaje.
  2- Utiliza operaciones de inserción, borrado, actualización y ordenación.
 
  3 - DIFICULTAD EXTRA (opcional):
  Crea una agenda de contactos por terminal.
  - Debes implementar funcionalidades de búsqueda, inserción, actualización
    y eliminación de contactos.
  - Cada contacto debe tener un nombre y un número de teléfono.
  - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
    y a continuación los datos necesarios para llevarla a cabo.
  - El programa no puede dejar introducir números de teléfono no númericos y con más
    de 11 dígitos (o el número de dígitos que quieras).
  - También se debe proponer una operación de finalización del programa.
"""

#1 -------------------------------ESTRUCTURAS--------------------------------

# ----------------------------------LISTAS-----------------------------------

my_list: list = ['Santiago','Francesco','Cyntia','Kathy']
print(my_list)

#insercion
my_list.append('Lucy')
print(my_list)

#Eliminacion
my_list.remove('Kathy')
print(my_list)

#Actualizar
my_list[1] = 'Mirta'
print(my_list)

#Ordenar
my_list.sort()
print(my_list)

# ----------------------------------TUPLAS-----------------------------------

my_tupple = ('Santiago', 'Molina', '30' , 'Santiagotuc')

print(my_tupple[1])  # Acceso
print(my_tupple[3])
my_tupple = tuple(sorted(my_tupple))  # Ordenación
print(my_tupple)
print(type(my_tupple))

# ----------------------------------SET-----------------------------------

my_set = {'Santiago', 'Molina', '30' , 'Santiagotuc'}
print(type(my_set))

#insercion (LOS SET EVITAN DUPLICADOS, NO SE PUEDE DUPLICAR DATOS)
my_set.add('santiago@gmail.com')
print(my_set)

#Eliminacion
my_set.remove('Molina')
print(my_set)

my_set= set(sorted(my_set)) #NO SE PUEDE ORDENAR
print(my_set)

print(type(my_set))

# ----------------------------------DICCIONARIO-----------------------------------

my_dict = {'name':'Santiago', 'surname': 'Molina', 'Edad': 30}
print(type(my_dict))

#Insercion
my_dict['email'] = 'santiago@gmail.com'
print(my_dict)

# Eliminación
del my_dict["surname"]  
print(my_dict)

#Acceso
print(my_dict['name'])

#Actualizacion
my_dict['Edad'] = 32
print(my_dict)

#Ordenacion

my_dict= dict(sorted(my_dict.items()))
print(my_dict)

# 03 --------------------------------ESTRUCTURAS DE DATOS--------------------------------
"""
- DIFICULTAD EXTRA (opcional):
  Crea una agenda de contactos por terminal.
  - Debes implementar funcionalidades de búsqueda, inserción, actualización
    y eliminación de contactos.
  - Cada contacto debe tener un nombre y un número de teléfono.
  - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
    y a continuación los datos necesarios para llevarla a cabo.
  - El programa no puede dejar introducir números de teléfono no númericos y con más
    de 11 dígitos (o el número de dígitos que quieras).
  - También se debe proponer una operación de finalización del programa.
"""

def my_agenda():

    agenda= {}

    def insert_contact():
        phone= input('Introduce el numero del contacto:')
        if phone.isdigit() and len(phone)>0 and len(phone)<=11:
            agenda[name] = phone
        else:
            print('Coloca un numero de maximo 11 digitos')


    while True:
        print("")
        print("1.Buscar contacto")
        print("2.Insertar contacto")
        print("3.Actualizar contacto")
        print("4.Eliminar contacto")
        print("5.Salir")

        option = input('\nSelecciona una opcion:')  
        
        match option:
            case "1":
                name= input('Introduce el nombre a buscar:')
                if name in agenda:
                    print(f'El numero de telefono de {name} es {agenda[name]}.')
                else:
                    print(f'El contacto {name} no existe')    
                pass
            case "2":
                name= input('Introduce el nombre del contacto:')
                insert_contact()  
            case "3":
                name= input('Introduce el nombre de contacto a actualizar:')
                if name in agenda:
                     insert_contact()
                else:
                    print(f'El contacto {name} no existe')   
                pass    
            case "4":
                name= input('Introduce el nombre de contacto a eliminar:')
                if name in agenda:
                    del agenda[name]
                else:
                    print(f'El contacto {name} no existe')     
                pass
            case "5":
                print('Saliendo de la agenda')
                break
            case _:
                print('Opcion No Valida, elije una opcion del 1 al 5.')    

my_agenda()                