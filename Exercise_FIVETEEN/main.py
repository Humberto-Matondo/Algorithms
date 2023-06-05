"""
1.  escreva uma consulta SQL que recupere o nome do cliente, número da conta e
saldo da tabela "clientes" e "contas", fazendo a junção das duas tabelas. Exiba os resultados na tela.

2. Em seguida, solicite ao usuário que digite o ID da conta de origem, ID da conta de destino e o valor da transação.
O programa deve verificar se a conta de origem tem saldo suficiente para a transação e, se sim, realizar a transação subtraindo
o valor da conta de origem e adicionando-o à conta de destino.
Certifique-se de executar a transação dentro de uma transação do banco de dados para garantir a consistência dos dados.

3. Em seguida, escreva uma consulta SQL que recupere o nome do cliente, número da conta,
valor e data da tabela "clientes", "contas" e "transações", fazendo a junção das três tabelas.
O relatório deve exibir todas as transações realizadas por cada cliente, incluindo a origem e o destino da transação.

"""

import datetime
import os
import random

import dotenv
import prettytable
import pymysql
from dateutil.relativedelta import relativedelta

dotenv.load_dotenv()

TABLE_CLIENTE = 'clientes'
TABLE_CONTAS = 'contas'
TABLE_TRANSACAO = 'transacoes'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    passwd=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:

        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_CONTAS} ('
            'idcontas INT NOT NULL AUTO_INCREMENT, '
            'numero_conta INT NOT NULL, '
            'saldo FLOAT NOT NULL, '
            'data_emi DATETIME NOT NULL, '
            'data_exp DATETIME NOT NULL, '
            'PRIMARY KEY (idcontas) '
            ') '
        )
        connection.commit()

        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_CLIENTE} ('
            'idclientes INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idconta INT NOT NULL, '
            'PRIMARY KEY(idclientes), '
            f'FOREIGN KEY(idconta) REFERENCES {TABLE_CONTAS}(idcontas) '
            ') '
        )

        cod_sql = f'INSERT INTO {TABLE_CONTAS} (numero_conta, saldo, data_emi, data_exp) VALUES (%s, %s, %s, %s)'
        cursor.execute(cod_sql, (1111111111, 1_000_000.00, datetime.datetime.now(), (datetime.datetime.now() + relativedelta(years=5))))

        cursor.execute(f'INSERT INTO {TABLE_CLIENTE} (nome, idconta) VALUES (%s, %s)', ('Humberto Matondo', 1))

        while True:
            nome = input('INFORME O NOME DO CLIENTE: ')
            saldo = float(input('INFORME O SALDO DO CLIENTE: '))
            numero_conta = float(input('INFORME O NUMERO DA CONTA DO CLIENTE: '))

            cod_sql = f'INSERT INTO {TABLE_CONTAS} (numero_conta, saldo, data_emi, data_exp) VALUES (%s, %s, %s, %s)'
            cursor.execute(cod_sql, (numero_conta, saldo, datetime.datetime.now(), (datetime.datetime.now() + relativedelta(years=5))))
            id_conta = cursor.lastrowid

            cursor.execute(f'INSERT INTO {TABLE_CLIENTE} (nome, idconta) VALUES (%s, %s)', (nome, id_conta))

            print(f'\nCliente {nome} cadastrado(a) no BANCO BAI.')
            connection.commit()
            resposta = int(input('Cadastrar novo cliente? \n1 - SIM \t 0 - NÃO \nR: '))
            if resposta != 1:
                break

        cursor.execute(
            f'SELECT {TABLE_CLIENTE}.idclientes, {TABLE_CLIENTE}.nome, '
            f'{TABLE_CONTAS}.idcontas, {TABLE_CONTAS}.numero_conta, {TABLE_CONTAS}.saldo '
            f'FROM {TABLE_CLIENTE} '
            f'INNER JOIN {TABLE_CONTAS} ON {TABLE_CLIENTE}.idconta = {TABLE_CONTAS}.idcontas'
        )

        table = prettytable.PrettyTable(['ID Cliente', 'Nome', 'ID Conta', 'Número da Conta', 'Saldo'])

        for row in cursor.fetchall():
            table.add_row(row)

        print(table)

        print()
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_TRANSACAO} ('
            'idtransacao INT NOT NULL AUTO_INCREMENT, '
            'valor FLOAT NOT NULL, '
            'data DATETIME NOT NULL, '
            'idconta_Origem INT NOT NULL, '
            'idconta_Destino INT NOT NULL, '
            'PRIMARY KEY(idtransacao), '
            f'FOREIGN KEY(idconta_Origem) REFERENCES {TABLE_CONTAS}(idcontas), '
            f'FOREIGN KEY(idconta_Destino) REFERENCES {TABLE_CONTAS}(idcontas) '
            ') '
        )
        connection.commit()

        idconta_origem = int(input('INFORME O ID DA CONTA ORIGEM: '))
        idconta_destino = int(input('INFORME O ID DA CONTA DESTINO: '))
        dinheiro_para_transferir = float(input('INFORME O VALOR QUE DESEJA TRANSFERIR: '))

        sql = f'INSERT INTO {TABLE_TRANSACAO} (valor, idconta_Origem, idconta_Destino, data) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, (dinheiro_para_transferir, idconta_origem, idconta_destino, datetime.datetime.now()))
        connection.commit()

        # ESSA PARTE DE BAIXO PRECISA-SE REVER, TEM UM ERRO:
        cursor.execute(
            f'SELECT {TABLE_TRANSACAO}.idtransacao, {TABLE_TRANSACAO}.valor, {TABLE_TRANSACAO}.data, '
            f'{TABLE_CONTAS}.idcontas AS idconta_origem, {TABLE_CONTAS}.numero_conta AS numero_conta_origem, '
            f'{TABLE_CONTAS}.saldo AS saldo_origem, '
            f'{TABLE_CONTAS}.idcontas AS idconta_destino, {TABLE_CONTAS}.numero_conta AS numero_conta_destino, '
            f'{TABLE_CONTAS}.saldo AS saldo_destino, '
            f'{TABLE_CLIENTE}.nome AS nome_cliente_origem, '
            f'(SELECT {TABLE_CLIENTE}.nome FROM {TABLE_CLIENTE} '
            f'INNER JOIN {TABLE_CONTAS} ON {TABLE_CLIENTE}.idconta = {TABLE_CONTAS}.idcontas '
            f'WHERE {TABLE_CONTAS}.idcontas = {TABLE_TRANSACAO}.idconta_Destino) AS nome_cliente_destino '
            f'FROM {TABLE_TRANSACAO} '
            f'INNER JOIN {TABLE_CONTAS} ON {TABLE_TRANSACAO}.idconta_Origem = {TABLE_CONTAS}.idcontas '
            f'INNER JOIN {TABLE_CLIENTE} ON {TABLE_CONTAS}.idcontas = {TABLE_CLIENTE}.idcontas'
        )

        table = prettytable.PrettyTable(['ID Transação', 'Valor', 'Data', 'Conta Origem', 'Número Conta Origem',
                                         'Saldo Origem', 'Conta Destino', 'Número Conta Destino', 'Saldo Destino',
                                         'Cliente Origem', 'Cliente Destino'])

        for row in cursor.fetchall():
            table.add_row(row)

        print(table)


# OBS AINDA N TERMINEI ESTE CODIGO, VOLTAREI OUTRO DIA PARA MELHORAR E TERMINAR POIS TEM COISAS FALTANDO
