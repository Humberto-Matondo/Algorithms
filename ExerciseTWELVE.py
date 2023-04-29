"""
Crie uma classe "Pessoa" que possua um atributo "nome" e um método "falar",
que simplesmente imprime na tela a frase "Olá, meu nome é <nome>". 

Crie uma classe "Carro" que possua um atributo "marca" e um método "dirigir", 
que imprime na tela a frase "Estou dirigindo um carro da marca <marca>". Agora, 

crie uma classe "Dono" que associa uma pessoa a um carro. Essa classe deve possuir dois atributos: 
uma instância da classe "Pessoa" e uma instância da classe "Carro". Crie um método na classe "Dono" chamado "se_apresentar",
que imprime na tela a frase "Olá, meu nome é <nome> e estou dirigindo um carro da marca <marca>".
"""

class Pessoa:
    def __init__(self, nome)->None:
        self.nome = nome
    
    def falar(self):
        return f'Ola, sou o <{self.nome}>'


class Carro:
    def __init__(self, marca) -> None:
        self.marca = marca
    
    def dirigir(self):
        return f'Estou dirigindo um carro de marca <{self.marca}>'
    
class Dono:
    def __init__(self)-> None:
        self.pessoa = None
        self.carro = None

    def se_apresentar(self):
        return f'{self.pessoa} {self.carro}'

dono = Dono()
p = Pessoa('Humberto Matondo')
c = Carro('Range Rover')

dono.pessoa = p.falar()
dono.carro = c.dirigir()

print(dono.se_apresentar())