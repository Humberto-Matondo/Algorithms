# sistema de perguntas e respostas(AJUDA NA PERCEPÇÃO DE COMO USAR LISTAS DENTRO DE DISCIONARIO E VISE-VERSA):

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


for pergunta in perguntas:
    print()
    print('PERGUNTA: ', pergunta['Pergunta'])
    print('\nOPÇÕES: ')
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):  # Para gerar o numero de indice e tmbm o item que contem dentro do pergunta['x']
        print(i, '). ', opcao)

    print()
    resposta_do_utilizador = input('Escolhe uma das opções: ')

    acertou = False
    qtd_acertos = 0
    escolha = None
    qtd_opcoes = len(opcoes)  

    # Essa parte abaixo é para ver se a pessoa digitou numero e ele foi convertido para inteiro, sei de um jeito mais facil
    if resposta_do_utilizador.isdigit():
        escolha = int(resposta_do_utilizador)
    if escolha is not None:
        if escolha >= 0 and escolha < qtd_opcoes:
            if opcoes[escolha] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('ACERTOU. ✅')
    else:
        print('ERROU. ❌😒')

print('\nACERTOU ', qtd_acertos, 'VEZES DE ', len(perguntas), 'PERGUNTAS.')
