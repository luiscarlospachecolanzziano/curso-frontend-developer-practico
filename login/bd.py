'''
Manejo de datos
'''
import json
def obtener_usuarios():
    '''
    obtener el listado de usuarios
    '''
    with open('holamundo.json', 'r', encoding='utf-8') as file:
        list_user = file.read()
        lista_usarios = json.loads(list_user)
        return lista_usarios

