class Jogador:
    def __init__(self, nome:str, posicao:str, numero:int, pontos:int, vida:int):
        self.nome = nome
        self.posicao = posicao
        self.numero = numero
        self.pontos = pontos
        self.vida = vida

    def info(self):
        print(f"Nome: {self.nome} \nPosição: {self.posicao} \nNúmero: {self.numero} \nPontos: {self.pontos}\n")

    def powerup(self):
        self.pontos += int(self.pontos * 0.50)
        print(f"{self.nome} agora tem {self.pontos} pontos!\n")

    def atacar (self, alvo):
        alvo.vida -= self.pontos
        print(f"{self.nome} está atacando {alvo.nome} que ficou com {alvo.vida} de pontos de vida!\n")

jogador1 = Jogador("Ronaldo", "Atacante", 7, 1, 10)
jogador2 = Jogador("Messi", "Atacante", 10, 2, 10)
jogador3 = Jogador("Mbappe", "Atacante", 9, 3, 10)

jogador1.info()
jogador2.info()
jogador3.info()

jogador3.powerup()
jogador2.atacar(jogador1)

