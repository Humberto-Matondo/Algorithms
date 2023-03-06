"""
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência(agencia pode ser um numero) é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco

Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.

"""
import contas
import pessoas


class Banco():
    def __init__(self, agencias: list[int] | None = None, clientes: list[pessoas.Pessoa] | None = None, grupo_conta: list[contas.Conta] | None = None):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.grupo_conta = grupo_conta or []

    def _verifica_agencia_(self, conta):
        if conta.agencia in self.agencias:
            print('AGENCIA EXISTE')
            return True
        print('AGENCIA N EXISTE')
        return False

    def _verifica_conta_(self, conta):
        if conta in self.grupo_conta:
            print('CONTA EXISTE NO BANCO')
            return True
        print('CONTA N EXISTE NO BANCO')
        return False

    def _verifica_cliente_(self, clientes):

        if clientes in self.clientes:
            print('CLIENTE EXISTE NO BANCO')
            return True
        print('CLIENTE N EXISTE NO BANCO')
        return False

    def _verifica_se_conta_e_do_cliente(self, clientes, conta):
        if conta is clientes.conta:
            print('A CONTA E DO CLIENTE DO BANCO.')
            return True
        print('A CONTA N E DO CLIENTE DO BANCO.')
        return False

    def autenticacao(self, clientes: pessoas.Pessoa, conta: contas.Conta):
        return self._verifica_agencia_(conta) and self._verifica_cliente_(clientes) \
            and self._verifica_conta_(conta) and self._verifica_se_conta_e_do_cliente(clientes, conta)

    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.agencias!r}, {self.clientes!r}, {self.grupo_conta!r})'
        return f'{class_name} {atributos}'
