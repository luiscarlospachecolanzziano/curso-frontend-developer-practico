'''
Verificacion de datos
'''
#TODO: llevar el consecutivo de id para seguir creciendo la lista aun que se eliminen usuarios.
#otra opcion es guardar los id en una lista para rellenarlos con los usuarios nuevos con list[]
import json
import bd
lista_usuario = bd.obtener_usuarios()
#verifica los datos
def listar_usuario():
  '''
  Muestra los usuarios registrados
  '''
  for usuario in lista_usuario:
    print(usuario['usuario'].upper())

def validar_usuario( user):
  '''
  user = str
  return = estado_usuario (True or False)
  '''
  estado_usuario = False
  for usuario in lista_usuario:
    if (usuario['usuario'] == user):
      estado_usuario = True
  
  return estado_usuario

def validar_usuario_password( user, password):
  '''
  user = str
  password = str
  return = estado_usuario (True or False)
  '''
  estado_usuario = False
  for usuario in lista_usuario:
    if (usuario['usuario'] == user) and (usuario['password'] == password):
      estado_usuario = True
      
  if (estado_usuario):
    print('Bienvenido, login correcto')
  else:
    print('error en los datos ingresados')
  
  return estado_usuario

def insertar_usuario(user, password):
  '''
  user = str
  password = str
  '''
  #la cant la uso para determinar el id del proximo usuario a registrar
  cant = len(lista_usuario)+1
  lista_usuario.append({"id": cant,
                        "usuario": user,
                        "password": password})
  escribir_json()
  
def eliminar_usuario(user):
  '''
  user = user
  return = true or false
  '''
  cont = 0
  rta_val_usu = validar_usuario(user)  
  if rta_val_usu:
    rta_opc = input(f'desea eliminar este usuario: {user}? S/N: ')
    if rta_opc.lower() == 's':
      for usuario in lista_usuario:
        if usuario['usuario'] == user:
          usuario_eliminado = lista_usuario.pop(cont)
          escribir_json()
          return usuario_eliminado
        else: cont += 1
    else: return(f'No fue eliminado el usuario: {user}')
    return False
  else: return(f'no existe ese usuario: {user}')
  
def escribir_json():
  '''
  actualiza el archivo json
  '''
  with open('holamundo.json', 'w', encoding='utf-8') as file:
            lista_final = json.dumps(lista_usuario)
            file.write(lista_final)