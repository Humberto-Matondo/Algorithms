"""
Crie uma classe Casa com os atributos endereco e numero_quartos. 
Em seguida, crie uma classe Condominio que possua uma lista de objetos do tipo Casa. 
A classe Condominio deve ter um método adicionar_casa que recebe um objeto Casa e o adiciona à lista de casas.
"""


class Casa:
    def __init__(self, endereco, numero_quartos: int):
        self.endereco = endereco
        self.numero_quartos = numero_quartos


class Condominio:
    def __init__(self):
        self.lista_de_casas: Casa()= []
        self.endereco = None
        self.numero_quartos: int = None

    def adicionar_casa(self, *casas):
        self.lista_de_casas += casas

    def listar_casa(self):
        for casa in self.lista_de_casas:
            print(casa.endereco, casa.numero_quartos)


casa, casa1 = Casa('Viana-Vila', 4), Casa('Zango 2', 2)
condominio = Condominio()

condominio.adicionar_casa(casa, casa1)
condominio.listar_casa()
