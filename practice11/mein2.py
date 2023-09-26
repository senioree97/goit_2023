class KeyStore:
    def __init__(self, name, password) -> None:
        self.__password = None
        self.__secret = None
        self.name = name
        self.password = password
        


    @property
    def password(self):
        return ("no way to get password back")

    @password.setter
    def password(self, value):
        if self.__password is None:
            self.__password = value
        else:
            if self.validate():
                print("password correct")
                self.__password = value
            else:
                print("incorrect ")

    @property
    def secret(self):
        if self.validate():
            return self.__secret
        
    @secret.setter
    def secret(self, value):
        if self.validate():
            self.__secret = value
        

    
    def validate(self):
        value = input("password: ")
        if self.__password == value:
            print("ok")
            return True
        print("Wrond pass")
        return False
    

k_srote = KeyStore("Krab", "1234456")
k_srote.password = "111"
print(k_srote.password)
k_srote.password = "1234456"
k_srote.secret = "aboba"
print(k_srote.secret)