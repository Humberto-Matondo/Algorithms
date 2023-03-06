import contas
import pessoas
from banco import Banco

cliente1 = pessoas.Cliente('Humberto Matondo', 24)
contaCorrente_cliente1 = contas.ContaCorrente(1, 222, 100, 100)
contapopanca_cliente1 = contas.ContaPoupanca(2, 223, 200)

cliente1.conta = contaCorrente_cliente1  # agregacao

cliente2 = pessoas.Cliente('Katharina Pinto', 20)

cliente2.conta = contapopanca_cliente1  # agregacao

banco = Banco()

banco.clientes.extend([cliente1, cliente2])
banco.grupo_conta.extend([contaCorrente_cliente1, contapopanca_cliente1])
banco.agencias.extend([1, 2])

if banco.autenticacao(cliente1, contaCorrente_cliente1):
    contaCorrente_cliente1.depositar(10)
    cliente1.conta.depositar(50)
    print(cliente1.conta)