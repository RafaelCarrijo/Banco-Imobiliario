class Pessoa:

    # cria as classes para ser usada no app
    def __init__(self, nome, personalidade, posicao=0) -> None:

        self.nome = nome
        self.personalidade = personalidade
        self.saldo = 300.00
        self.posicao = posicao
        self.perdeu = False
        self.propriedades = []

    def desclassificar(self):

        self.perdeu = True

        if self.propriedades != []:

            for propriedade in self.propriedades:
                propriedade.proprietario = None

    def comprar_imovel(self, propriedade):

        self.propriedades.append(propriedade)


class Propriedade:

    def __init__(self, id: int, nome: str, valor_aluguel: int, valor_compra: int) -> None:

        self.id = id
        self.nome = nome
        self.valor_aluguel = valor_aluguel
        self.valor_compra = valor_compra
        self.proprietario = None

    def efetuar_venda(self, pessoa):

        self.proprietario = pessoa

    def devolver_imoveis(self):

        self.proprietario = None
