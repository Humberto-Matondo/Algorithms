"""
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
"""
import contas


class Pessoa():
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor
        return self._nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor: int):
        self._idade = valor
        return self._idade

    def __repr__(self):
        class_name = type(self).__nome__
        atributos = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{atributos}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None
