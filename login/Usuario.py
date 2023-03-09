class Usuario:
    id = 0
    user = ""
    password = ""
    
    def __init__(self, id:int, user:str, password:str):
        self.__id = id
        self.__user = user
        self.__password = password
        
    # Getter   
    @property
    def user_id(self):
        return self.__id
    @property
    def user_name(self):
        return self.__user
    @property
    def user_password(self):
        return self.__password
    
    # Setter
    @user_id.setter
    def user_id(self, value):
        assert value == 0, 'El campo id esta vacio'
        self.__id = value
        
    @user_name.setter
    def user_name(self, value):
        assert value != '', 'El campo usuario esta vacio, pedazo de maricon'
        self.__user = value
        
    @user_password.setter
    def user_password(self, value):
        assert value != '', 'El campo contraseña esta vacio, pedazo de maricon'
        self.__password = value


user = Usuario( 0, 'luis', '123')
print(user.user_name)
user.user_name = 'andres'
print(user.user_name)