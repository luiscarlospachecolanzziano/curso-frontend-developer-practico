'''
main de login
'''
import verificar_datos as ver_dat
import menu

while True:
    # Menu
    menu.mostrar_menu()
    opcion = input('ingrese su opcion: ')
    #opciones
    if opcion == '1':
        user = input('Ingrese su usuario: ')
        password = input('Ingrese su contraseña: ')
        #debo llamar la clase y el metodo que se necesita
        ver_dat.validar_usuario_password(user, password)
    elif opcion == '2':
        print('Registrar usuario:')
        user = input('Ingrese su nombre de usuario: ')
        password = input('Ingrese una contraseña: ')
        #TODO: modificar para que solo sea verificado con user - (nota: polimorfismo)
        estado = ver_dat.validar_usuario(user)
        if estado:
            print ('El usuario ya existe')
        else:
            ver_dat.insertar_usuario(user,password)
            print ('Usuario registrado!!!')
    elif opcion == '3':
        print('-------- lista de usuarios --------')
        ver_dat.listar_usuario()
    elif opcion == '4':
        #TODO:pendendiente para eliminar un usuario
        print('---- Usuaio ----')
        ver_dat.listar_usuario()
        print('---- ##### ----')
        
        dato_usuario = input('ingrese el usuario que desea eliminar: ').lower()
        estado_usuario = ver_dat.eliminar_usuario(dato_usuario)
        print(estado_usuario)
    elif opcion == '5':
        print('adios ...')
        break
    else: print('opcion no valida')
    
    