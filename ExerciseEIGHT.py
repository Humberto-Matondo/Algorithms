# Calculando as datas e parcelas de um empréstimo:

# Maria pegou um empréstimo de 1.000.000 para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi 20/12/2020 e o vencimento de cada parcela é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime

from dateutil.relativedelta import relativedelta

data_inicial = datetime(2020, 12, 20)
data_final = datetime(2025, 12, 20)

valores_emprestado = 1_000_000
parcela_a_pagar_por_mes = valores_emprestado / 60

print()
while data_inicial < data_final:
    print('Em ', data_inicial.strftime('%d-%m-%Y'), f', foi pago {parcela_a_pagar_por_mes:,.2f} Kwanzas.')
    data_inicial += relativedelta(months=+1)
print(f'\n{valores_emprestado:.2f} KWANZAS FORAM PAGOS EM 60 MESES.')
