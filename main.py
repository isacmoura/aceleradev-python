# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

import csv
from itertools import islice
from collections import defaultdict

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?

def q_1():
    lista = []
    with open('data.csv', 'r') as planilha:
        reader = csv.DictReader(planilha)
        for linha in reader:
            if(linha['nationality']):
                if linha['nationality'] not in lista:
                    lista.append(linha['nationality'])
    return len(lista)

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    lista = []
    with open('data.csv') as planilha:
        reader = csv.DictReader(planilha)
        for linha in reader:
            if(linha['club']):
                if linha['club'] not in lista:
                    lista.append(linha['club'])
    return len(lista)+1

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    jogadores = []
    with open('data.csv', 'r') as planilha:
        reader = csv.DictReader(planilha)
        for linha in islice(reader, 20):
            jogadores.append(str(linha['full_name']))
    return jogadores

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    with open('data.csv', 'r') as planilha:
        reader = csv.DictReader(planilha)
        most_richies = [(linha['full_name'], float(linha['eur_wage'])) for linha in reader]
        most_richies = sorted(most_richies, reverse = True, key = lambda x: x[1])[:10]
    return [ jogador[0] for jogador in most_richies ]

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    with open('data.csv', 'r') as planilha:
        reader = csv.DictReader(planilha)
        oldest = [(linha['full_name'], linha['age']) for linha in reader]
        oldest = sorted(oldest, reverse= True, key = lambda x: x[1])[:10]
    return [ jogador[0] for jogador in oldest]
print(q_5())

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    counter = defaultdict(int)
    with open('data.csv', 'r') as planilha:
        reader = csv.DictReader(planilha)
        for item in reader:
            if item['age']:
                counter[int(item['age'])] += 1
            
    sorted_dict = dict(sorted((key, value) for (key, value) in counter.items()))
    return sorted_dict