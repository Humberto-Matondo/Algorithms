class Pessoa:
    def __init__(self, nome, idade, sexo):
        self._nome = nome
        self.__idade = idade
        self.__sexo = sexo

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self.__idade

    @property
    def sexo(self):
        return self.__sexo
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

