import json

#asi escribo
usuarios = {
        'id' : 4,
        'usuario' : 'Nadia',
        'password' : '8888' 
    }
# with open('holamundo.txt', 'a') as f:
#     #armando bd con listas
#     #[int, 'str', 'str']
#     # f.write('1,'+"'admin',"+"'1234'")
    
    
#     f.write(json.dumps(usuarios)+",\n")

#(r)read se lee el documento json
with open('holamundo.json', 'r', encoding='utf-8') as f:
    listUser = f.read()
    listaUsuarios = json.loads(listUser)
    listaUsuarios.append(usuarios)
#se escribe en el json
with open('holamundo.json', 'w', encoding='utf-8') as f:
    listaFinal = json.dumps(listaUsuarios)
    f.write(listaFinal)


# #asi escribo
# lista = ['manzana', 'pera', 100, 200]
# with open('holamundo.txt', 'w') as f:
#     # f.write('este metodo me gusta mas')
#     for fruta in lista:
#         f.write("'"+str(fruta)+"',")
# # f = open('holamundo.txt', 'w')
# # f.write('hola mundo 2')
# # f.close()
# #asi leo 
# with open('holamundo.txt', 'r') as f:
#     mensaje = f.read()
#     print(mensaje)
# # f.close()