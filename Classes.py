class Jogador:
    def __init__(self, nome, posicao, numero):
        self.nome = nome
        self.posicao = posicao
        self.numero = numero

    def info(self):
        print(f"Nome: {self.nome} \nPosição: {self.posicao} \nNúmero: {self.numero}")

jogador1 = Jogador("Ronaldo", "Atacante", 9)
jogador1.info()