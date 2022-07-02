from pandas import DataFrame
import engine
from random import shuffle


def calcula_vencedor_timeout(lista_jogdores: list):

    saldo = 0
    vencedor = ''
    comportamento = ''

    for jogador in lista_jogdores:
        if jogador.saldo > saldo:
            saldo = jogador.saldo
            vencedor = jogador.nome
            comportamento = jogador.personalidade

    return vencedor, comportamento


def iniciar_jogo(df: DataFrame):
    # criando os jogadores
    jogadores = engine.criar_jogador()

    # sorteando jogadores aleatoreamente na primeira rodada.
    shuffle(jogadores)

    rodadas = 1

    while (rodadas < 1000):

        # reconhecendo o jogador vitorioso nos casos que não deram timeout
        if len(jogadores) == 1:
            jogador = jogadores[0]
            df = [0, rodadas, jogador.nome, jogador.personalidade]
            return df

        if len(jogadores) > 1:

            for jogador in jogadores:

                if jogador.perdeu == False:
                    rodadas = engine.tabuleiro(jogador, rodadas)

                # remove os jogadores que perderam e retira todas as propriedades de seu dominio.
                else:
                    if len(jogador.propriedades) > 0:
                        for propriedade in jogador.propriedades:
                            propriedade.proprietario = None

                        jogador.propriedades = []

                    jogadores.remove(jogador)

    # montando lista de retorno em caso de timeout
    vencedor, comportamento = calcula_vencedor_timeout(jogadores)
    df = [1, 1000, vencedor, comportamento]
    return df
