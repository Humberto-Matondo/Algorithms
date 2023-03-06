"""
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e polimorfismo - as subclasses que implementam o método sacar)
"""
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, numero_de_conta: int, saldo: float = 0):
        self.agencia = agencia
        self.numero_de_conta = numero_de_conta
        self.saldo = saldo

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhe(f'{valor:.2f}kz DEPOSITADO.')

    @abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def detalhe(self, mensagem: str = ''):
        return f'SEU SALDO: {self.saldo:.2f}kz. {mensagem}'

    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.agencia!r}, {self.numero_de_conta!r}, {self.saldo!r})'
        return f'{class_name}{atributos}'

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_depois_do_saque = self.saldo - valor

        if valor_depois_do_saque >= 0:
            self.saldo -= valor
            self.detalhe('SAQUE DE {valor:.2f}kz SUCEDIDO\n')
            return self.saldo

        self.detalhe('SAQUE DE {valor:.2f}kz NEGADO')
        print('ESSE VALOR DIGITADO N CONSTA NA SUA CONTA.\n')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_de_conta, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, numero_de_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_depois_do_saque = self.saldo - valor

        if (valor_depois_do_saque <= self.limite) and (valor_depois_do_saque >= 0):
            self.saldo -= valor
            self.detalhe('SAQUE DE {valor:.2f}kz SUCEDIDO\n')
            return self.saldo

        elif valor_depois_do_saque > self.limite:
            self.detalhe('SAQUE DE {valor:.2f}kz NEGADO')
            print(f'ESSE VALOR DIGITADO ATINGIU O LIMITE({self.limite:.2f}KZ) DA SUA CONTA.\n')

        self.detalhe('SAQUE DE {valor:.2f}KZ NEGADO')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.agencia!r}, {self.numero_de_conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{atributos}'
