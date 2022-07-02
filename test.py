import main
# Importando o pandas para fazer a estatistica das vitorias de maneira organizada
import pandas as pd

# Criando o dataframe para ser preenchido com os resultados dos jogos
colunas = ['TimeOut', 'Turnos', 'Nome', 'Comportamento']
vitorias_df = pd.DataFrame([], columns=colunas)

# Loop para startar o jogo 300 vezes e armazenar os resultados
for i in range(300):
    lista = main.iniciar_jogo(vitorias_df)
    vitorias_df.loc[i] = lista


def calcular_maior_ganhador(dicionario: dict):
    ganhador = ''
    numero_de_vitorias = 0
    for chave, valor in dicionario.items():
        if valor > numero_de_vitorias:
            numero_de_vitorias = valor
            ganhador = chave

    return ganhador, numero_de_vitorias


# imprime as 5 primeiras linhas do dataframe
print(vitorias_df.head())

# Imprime as informações do dataframe
print(vitorias_df.describe())

# calcula quantas vetorias foram por timeout
timeout_total = vitorias_df['TimeOut'].sum()

# calcula a media de de numero de rodadas uma partida demora
media_rodadas = round(vitorias_df['Turnos'].mean())

# calculando qual é a personalidade que mais ganhou
vitorias_impulsivo = vitorias_df[vitorias_df.Comportamento ==
                                 "Impulsivo"]['Comportamento'].count().sum()
vitorias_exigente = vitorias_df[vitorias_df.Comportamento ==
                                "Exigente"]['Comportamento'].count().sum()
vitorias_cauteloso = vitorias_df[vitorias_df.Comportamento ==
                                 "Cauteloso"]['Comportamento'].count().sum()
vitorias_aleatorio = vitorias_df[vitorias_df.Comportamento ==
                                 "Aleatorio"]['Comportamento'].count().sum()
dicionario_personalidades = {
    'Impulsivo': vitorias_impulsivo,
    'Exigente': vitorias_exigente,
    'Cauteloso': vitorias_cauteloso,
    'Aleatorio': vitorias_aleatorio
}

personalidade_vencedora, numero_vitorias_personalidade = calcular_maior_ganhador(
    dicionario_personalidades)

# Calculando qual o jogador que mais ganhou
vitorias_rafael = vitorias_df[vitorias_df.Nome ==
                              "Rafael"]['Nome'].count().sum()
vitorias_flavia = vitorias_df[vitorias_df.Nome ==
                              "Flavia"]['Nome'].count().sum()
vitorias_kleber = vitorias_df[vitorias_df.Nome ==
                              "Kleber"]['Nome'].count().sum()
vitorias_thays = vitorias_df[vitorias_df.Nome == "Thays"]['Nome'].count().sum()

dicionario_vencedores = {
    'Rafael': vitorias_rafael,
    'Flavia': vitorias_flavia,
    'Kleber': vitorias_kleber,
    'Thays': vitorias_thays
}

nome_maior_ganhador, numero_vitorias_jogador = calcular_maior_ganhador(
    dicionario_vencedores)


print(
    f'O maior ganhador do jogo foi {nome_maior_ganhador}, que ganhou {numero_vitorias_jogador} vezes')
print(f'As partidas tiveram uma media de {media_rodadas} turnos para terminar')
print(
    f'Após as 300 simulações, {timeout_total} partidas terminaram por timeout')
print(
    f'O comportamento que mais foi vitorioso foi o {personalidade_vencedora}, com {numero_vitorias_personalidade} vitórias')
