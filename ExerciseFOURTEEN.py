"""
Suponha que você esteja desenvolvendo um programa para uma loja de roupas que vende diferentes tipos de produtos, 
como camisetas, calças, sapatos etc. Cada produto tem um nome, um preço e um fornecedor. O fornecedor também tem um nome e um número de telefone.

Crie uma classe Produto com os atributos nome, preco e fornecedor. 
Em seguida, crie uma classe Fornecedor com os atributos nome e telefone. 
Por fim, crie uma classe Loja que contém uma lista de produtos. Para isso, siga os passos abaixo:

Crie a classe Fornecedor com os atributos nome e telefone.
Crie a classe Produto com os atributos nome, preco e fornecedor. Note que o atributo fornecedor será uma instância da classe Fornecedor.
Crie a classe Loja com o atributo produtos, que será uma lista de instâncias da classe Produto.

Implemente um método adicionar_produto na classe Loja que recebe um produto como parâmetro e adiciona-o à lista de produtos.
Implemente um método buscar_produto_por_fornecedor na classe Loja que recebe o nome de um fornecedor como parâmetro 
e retorna uma lista de todos os produtos fornecidos por esse fornecedor.

Crie instâncias das classes Fornecedor, Produto e Loja e teste os métodos implementados.
"""


class Fornecedor:
    def __init__(self, nome, telefone) -> None:
        self.nome = nome
        self.telefone = telefone


class Produto:
    def __init__(self, nome, preco: float, fornecedor: Fornecedor) -> None:
        self.nome = nome
        self.preco = preco
        self.fornecedor = fornecedor

    def __str__(self):
        return f"Fornecedor: {self.fornecedor.nome}, Telefone: {self.fornecedor.telefone}, Produto: {self.nome}, Preço: {self.preco:.2f}KZ, "

class Loja:
    def __init__(self) -> None:
        self.lista_de_produtos = []

    def adicionar_produto(self, nome, preco, fornecedor: Fornecedor):
        self.lista_de_produtos.append(Produto(nome, preco, fornecedor))

    def buscar_produto_por_fornecedor(self, fornecedor: Fornecedor):
        for produto in self.lista_de_produtos:
            if produto.fornecedor == fornecedor:
                print(produto)
        
    def listas_todos_produtos_e_fornecedor(self):
        for produto in self.lista_de_produtos:
            print(f'PRODUTO: {produto.nome}: {produto.preco}KZ. \nFOI FORNECIDO POR: {produto.fornecedor.nome}, TEL.: {produto.fornecedor.telefone}')
            print()


loja = Loja()

fornecedor1 = Fornecedor('Humberto Matondo', '+244 940 857 382')
fornecedor2 = Fornecedor('Leandra carvalho', '+244 ... ... ...')
fornecedor3 = Fornecedor('Gildo Jeremias', '+244 ... ... ...')

loja.adicionar_produto('Casos de Arroz', 200_000, fornecedor1)
loja.adicionar_produto('Sumos Compal', 5_000, fornecedor3)
loja.adicionar_produto('Sabonetes', 2_000, fornecedor3)
loja.adicionar_produto('Pastas de Dente', 4_000, fornecedor1)
loja.adicionar_produto('Bolachas Maria', 7_000, fornecedor2)
loja.adicionar_produto('Recargas Zap', 20_000, fornecedor1)

print()
loja.listas_todos_produtos_e_fornecedor()

print('BUSCANDO UM FORNECEDOR EXPECIFICO: ')
print()

loja.buscar_produto_por_fornecedor(fornecedor1)

