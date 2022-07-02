from random import randint
from classes import Pessoa, Propriedade

print('Bem vindo ao Banco Imobiliario "Distrito Federal"')

casas = 0
propriedades = None


def criar_jogador():

    jogador_1 = Pessoa("Rafael", "Impulsivo")
    jogador_2 = Pessoa("Flavia", "Exigente")
    jogador_3 = Pessoa("Kleber", "Cauteloso")
    jogador_4 = Pessoa("Thays", "Aleatorio")
    lista_jogadores = [jogador_1, jogador_2, jogador_3, jogador_4]

    return lista_jogadores


def criar_propriedades():
    lista_valor_aluguel = [randint(30, 60) for x in range(0, 20)]
    lista_valor_compra = [randint(60, 100) for x in range(0, 20)]
    nomes_propriedades = ['Ceilandia', 'Aguas Claras', 'Asa Norte', 'Asa Sul', 'Samambaia', 'Vicente Pires', 'Nucleo Bandeirante', 'Candagolandia',
                          'taguatinga', 'Sobradinho', 'Planaltina', 'Lago Sul', 'Lago Norte', 'Cruzeiro', 'Brazlandia', 'Sol Nascente',
                          'paranoa', 'Itapuã', 'Jardim Botanico', 'Riacho Fundo']

    lista_propriedades = []
    id = 1
    for valor_aluguel, valor_compra, nome in zip(lista_valor_aluguel, lista_valor_compra, nomes_propriedades):

        imovel = Propriedade(id, nome, valor_aluguel, valor_compra)
        lista_propriedades.append(imovel)
        id += 1
    return lista_propriedades


def jogar_dado():
    return randint(1, 6)


def verifica_personalidade(personalidade, saldo=0, valor_aluguel=0, valor_compra=0):

    if personalidade == "Impulsivo":
        return True

    if personalidade == "Exigente":
        if valor_aluguel > 50:
            return True
        return False

    if personalidade == "Cauteloso":
        if saldo - valor_compra > 80:
            return True
        return False

    if personalidade == "Aleatorio":
        if randint(0, 1) == 1:
            return True
        return False


propriedades = criar_propriedades()


def tabuleiro(jogador, rodadas):

    if jogador.saldo <= 0:
        jogador.perdeu = True
        rodadas += 1
        return rodadas
    #print(jogador.nome, jogador.saldo)

    casas = jogador.posicao + jogar_dado()

    if casas > 20:
        casas = casas % 20
        jogador.saldo += 100

    propriedade = propriedades[casas - 1]

    if propriedade.proprietario != None:
        #print(f'o jogador {jogador.nome} pagou aluguel para o jogador {propriedade.proprietario.nome}')
        jogador.saldo -= propriedade.valor_aluguel
        propriedade.proprietario.saldo += propriedade.valor_aluguel
    else:
        if verifica_personalidade(jogador.personalidade, jogador.saldo, propriedade.valor_aluguel, propriedade.valor_compra):
            propriedade.efetuar_venda(jogador)
            jogador.comprar_imovel(propriedade)

    rodadas += 1

    return rodadas
