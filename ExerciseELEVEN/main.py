import os

from accoesVideo import AccoesVideo
from estudante import Aluno
from visualizacao import Visualizacao
from youtubeVideo import Video

# prencher com inf. do estrudante
while True:
    print('+'*10)
    print('+'*5, end='')
    print('|ESTUDANTE|', end='')
    print('+'*5)
    print('+'*10)
    print()
    estudante = Aluno()

    if bool(input('DESEJA FAZER LOGIN:[True - Sim, False - Nao].\nR: ')) == True:
        estudante.login()
        # os dados de entrada podem ser modificados com inputers
        estudante.nome = input('Nome do aluno(a): ')
        estudante.sexo = 'M'
        estudante.idade = 25

# prencher com inf. do video
        print()
        print('+'*10)
        print('+'*5, end='')
        print('|YOUTUBE VIDEO|', end='')
        print('+'*5)
        print('+'*10)
        print()
        video = Video()

        video.titulo = input('TITULO DO VIDEO: ')  # 'POO como aprender CURSO COMPLETO'  # posso usar input para receber esse dados
        video.reproduzir()  # para comecar a reproduzir

        while True:
            visualiza = Visualizacao(estudante.nome, video.titulo)  # agregacao
            estudante.viuMaisUm()  # para aumentar a quantidade de video que o estudante assistiu

            video.metodo_views()  # para aumentar visualizacao do videos
            print()
        # prencher com inf. do video e accoes
            if bool(input('PAUSAR O VIDEO?[Y- True, No- False]. \nR:')) == True:
                video.acoes.pause()  # Estudante deu pause
                print()
            if bool(input('DAR O PLAY NO VIDEO?[Y- True, No- False]. \nR:')) == True:
                video.acoes.play()  # Estudante deu play
                print()
            if bool(input('Dar Like?[Y- True, No- False]. \nR:')) == True:
                video.acoes.like()  # Estudante deixou like
                video.metodo_likes()  # quant. de likes dados nos videos
                print()
            elif bool(input('Dar unLike?[Y- True, No- False]. \nR:')) == True:
                video.acoes.unLike()  # Estudante deixou um unlike
                video.metodo_unlikes()  # quant de unlikes dados nos videos
                print()

            if bool(input('PARAR DE REPRODUZIR. [Y- True, No- False]. \nR:')) == True:
                video.parar_Reproducao()
                print('O VIDEO N ESTA SENDO REPRODUZIDO.')
                break

        print()
        if bool(input('DESEJA FAZER LOGOUT?[True- SAIR e False - CONTINUAR].\nR: ')) == True:
            print()
            print(f'Estudante {visualiza.espectador} viu {estudante.viuMaisUm()}x o video {visualiza.video}\n'
                  f'Deixou {video.metodo_likes()} e {video.metodo_unlikes()}')
            estudante.Login_OFF()
            break

    os.system('cls')
