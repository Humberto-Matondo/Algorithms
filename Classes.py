class Jogador:
    def __init__(self, nome, posicao, numero, pontos):
        self.nome = nome
        self.posicao = posicao
        self.numero = numero
        self.pontos = pontos

    def info(self):
        print(f"Nome: {self.nome} \nPosição: {self.posicao} \nNúmero: {self.numero} \nPontos: {self.pontos}\n")

    def powerup(self):
        self.pontos += int(self.pontos * 0.50)
        print(f"{self.nome} agora tem {self.pontos} pontos!\n")

jogador1 = Jogador("Ronaldo", "Atacante", 7, 1)
jogador2 = Jogador("Messi", "Atacante", 10, 2)
jogador3 = Jogador("Mbappe", "Atacante", 9, 3 )

jogador1.info()
jogador2.info()
jogador3.info()

jogador3.powerup()

