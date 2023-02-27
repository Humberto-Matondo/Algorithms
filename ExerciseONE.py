
#Contabilizar a quantidade de vezes uma letra aparece.

frase = 'O python é uma linguagem de programação Multiparadigma. Python e foi criada por Guido Van Rossum.'.lower()
    
i = 0   
letra_que_apareceu_mais = ''
qtd_da_letra_que_apareceu_mais = 0

while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    else: 
        qtd_de_vezes_apareceu_a_letra_atual = frase.count(letra_atual)
        if qtd_da_letra_que_apareceu_mais <= qtd_de_vezes_apareceu_a_letra_atual:
            qtd_da_letra_que_apareceu_mais = qtd_de_vezes_apareceu_a_letra_atual
            letra_que_apareceu_mais = letra_atual
        i += 1
print(f'A letra "{letra_que_apareceu_mais}" apareceu mais vezes, com {qtd_da_letra_que_apareceu_mais} aparições.')