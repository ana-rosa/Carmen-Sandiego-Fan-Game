from datetime import datetime, timedelta

import os
import random
import unicodedata

import dados
from dados import suspeitos
from dados import paises


def data_jogo():
    data_jogo = datetime(2019, 1, 1, 6, 0, 0)  # 2019-01-01 06:00:00  data formato ISO
    return data_jogo


def escolhe_suspeito():
    suspeitinhos = suspeitos.copy()
    random.shuffle(suspeitinhos)
    return suspeitinhos.pop()


def escolhe_pais():
    nacoes = paises.copy()
    random.shuffle(nacoes)
    return nacoes.pop()


def gera_prox_pais(pais_atual):
    prox_pais = escolhe_pais()
    while prox_pais == pais_atual:
        prox_pais = escolhe_pais()
    return prox_pais


def menu_principal(pais_atual, data_atual):
    print(pais_atual.nome)
    print(data_atual.strftime("%A %d/%m/%Y %H:%M"))
    print(pais_atual.texto)
    print("1 - Lista de Suspeitos")
    print("2 - Gerar Mandado")
    print("3 - Viajar")
    print("4 - Investigar")


def identifica_usuario(id):
    nome_arquivo = id + ".txt"
    if os.path.isfile(nome_arquivo) is True:
        print("\n")
        print("Seu cadastro foi encontrado, ", id)
        print("\n")
        with open(nome_arquivo) as save:
            return int(save.readline())
    else:
        print("Não encontramos seu id em nossa base de dados. Você deve ser novo(a) por aqui.")
        id = input("Por favor, identifique-se novamente para que possamos realizar seu cadastro: ")
        with open(id + ".txt", "w") as save:
            save.write("0")
        print("Você foi cadastrado(a), ", id)
        print("Gostaria de começar um jogo?")
        resposta = input("Sim / Não ")
        if normaliza_string(resposta) == normaliza_string("não"):
            exit()
        return 0


def salva_jogo(casos_resolvidos, id):
    with open(id + ".txt", "w") as save:
        save.write(str(casos_resolvidos))


def verifica_cargo(casos_resolvidos):
    if casos_resolvidos == 0:
        cargo_atual = "Estagiário(a)"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual
    elif casos_resolvidos >= 1 and casos_resolvidos < 4:
        cargo_atual = "Investigador(a) Jr"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual
    elif casos_resolvidos >= 4 and casos_resolvidos < 7:
        cargo_atual = "Investigador(a)"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual
    elif casos_resolvidos >= 7 and casos_resolvidos < 10:
        cargo_atual = "Investigador(a) Sênior"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual
    elif casos_resolvidos >= 10 and casos_resolvidos < 14:
        cargo_atual = "Inspetor(a) Jr"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual
    elif casos_resolvidos >= 14 and casos_resolvidos < 18:
        cargo_atual = "Inspetor(a)"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
    elif casos_resolvidos >= 18 and casos_resolvidos < 23:
        cargo_atual = "Inspetor(a) Sênior"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual
    elif casos_resolvidos >= 23 and casos_resolvidos < 28:
        cargo_atual = "Detetive Jr"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual
    elif casos_resolvidos >= 28 and casos_resolvidos < 33:
        cargo_atual = "Detetive"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual
    elif casos_resolvidos == 33:
        cargo_atual = "Detetive Sênior"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual
    elif casos_resolvidos == 34:  # o 34 tem que ser a captura da Carmen
        cargo_atual = "Super Detetive"
        print("Seu cargo atual é:", cargo_atual, ".")
        print("\n ")
        return cargo_atual


def verifica_promocao(cargo_atual, casos_resolvidos):
    if cargo_atual == "Estagiário(a)":
        print("Bom trabalho! Você foi promovido(a) a Investigador(a) Jr.")
    elif cargo_atual == "Investigador(a) Jr.":
        casos_promocao = 4 - casos_resolvidos
        if casos_promocao != 0:
            print("Resolva mais", casos_promocao, "caso(s) até a próxima promoção.")
        else:
            print("Bom trabalho! Você foi promovido(a) a Investigador(a)")
    elif cargo_atual == "Investigador(a)":
        casos_promocao = 7 - casos_resolvidos
        if casos_promocao != 0:
            print("Resolva mais", casos_promocao, "caso(s) até a próxima promoção.")
        else:
            print("Bom trabalho! Você foi promovido(a) a Investigador(a) Sênior.")
    elif cargo_atual == "Investigador(a) Sênior":
        casos_promocao = 10 - casos_resolvidos
        if casos_promocao != 0:
            print("Resolva mais", casos_promocao, "caso(s) até a próxima promoção.")
        else:
            print("Bom trabalho! Você foi promovido(a) a Inspetor(a) Jr.")
    elif cargo_atual == "Inspetor(a) Jr":
        casos_promocao = 14 - casos_resolvidos
        if casos_promocao != 0:
            print("Resolva mais", casos_promocao, "caso(s) até a próxima promoção.")
        else:
            print("Bom trabalho! Você foi promovido(a) a Inspetor(a).")
    elif cargo_atual == "Inspetor(a)":
        casos_promocao = 18 - casos_resolvidos
        if casos_promocao != 0:
            print("Resolva mais", casos_promocao, "caso(s) até a próxima promoção.")
        else:
            print("Bom trabalho! Você foi promovido(a) a Inspetor(a) Sênior.")
    elif cargo_atual == "Inspetor(a) Sênior":
        casos_promocao = 23 - casos_resolvidos
        if casos_promocao != 0:
            print("Resolva mais", casos_promocao, "caso(s) até a próxima promoção.")
        else:
            print("Bom trabalho! Você foi promovido(a) a Detetive Jr.")
    elif cargo_atual == "Detetive Jr":
        casos_promocao = 28 - casos_resolvidos
        if casos_promocao != 0:
            print("Resolva mais", casos_promocao, "caso(s) até a próxima promoção.")
        else:
            print("Bom trabalho! Você foi promovido(a) a Detetive.")
    elif cargo_atual == "Detetive":
        casos_promocao = 33 - casos_resolvidos
        if casos_promocao != 0:
            print("Resolva mais", casos_promocao, "caso(s) até a próxima promoção.")
        else:
            print("Bom trabalho! Você foi promovido(a) a Detetive Sênior.")
    if cargo_atual == "Detetive Sênior":
        print("Bom trabalho! Você foi promovido(a) a Super Detetive.")
    if cargo_atual == "Super Detetive":
        print("Parabéns! Você chegou ao hall da fama! Já pode se aposentar.")


def gera_caso(cena_crime, culpado, data_inicio, data_fim, cargo_atual):
    print("***URGENTE!***")
    print("Quartel General: ", data_inicio.strftime("%A %d/%m/%Y %H:%M"))
    print("Tesouro Nacional roubado do seguinte país:", cena_crime.nome)
    print("O tesouro foi identificado como", cena_crime.tesouro)
    print("Pessoa vista na cena do crime:", culpado.genero)
    print("Sua missão: siga a pessoa suspeita e preenda-a.")
    print("Prazo da captura: ", data_fim.strftime("%A %d/%m/%Y %H:%M"))
    print("Boa sorte,", cargo_atual, ".")


def viaja_exterior(pais_origem, pais_destino):
    pais_errado1 = random.choice(paises)
    while pais_errado1 == pais_destino or pais_errado1 == pais_origem:
        pais_errado1 = random.choice(paises)
    pais_errado2 = random.choice(paises)
    while pais_errado2 == pais_origem or pais_errado2 == pais_destino or pais_errado2 == pais_errado1:
        pais_errado2 = random.choice(paises)
    print("a -", pais_destino.nome)
    print("b -", pais_errado1.nome)
    print("c -", pais_errado2.nome)
    escolha = input("Aperte a tecla que corresponde ao país que deseja viajar.")
    os.system("clear")
    if escolha != "a":
        print("O suspeito fugiu!")
        print("\n")
        print("Pronto(a) para o próximo caso?")
        resposta = input("Sim / Não: ")
        le_escolha_ir_prox_caso(resposta, dados.OPCOES)
    else:
        pais_origem = pais_destino
        return pais_origem
        menu_principal(pais_origem)


def lista_suspeitos():
    print("lista de suspeitos")
    for suspeito in suspeitos:
        print(suspeito.nome)
        print("Gênero:", suspeito.genero)
        print("Cabelo:", suspeito.cabelo)
        print("Comida:", suspeito.comida)
        print("Esporte:", suspeito.esporte)
        print("Hobby:", suspeito.hobby)
        print("Música:", suspeito.musica)
        print("\n ")


def processa_mandado():
    suspeitos = busca_suspeito()
    if len(suspeitos) == 1:
        nomes = []
        for suspeito in suspeitos:
            nomes.append(suspeito.nome)

        print("\n")
        print("Você tem um mandado de prisão para:")
        print(", ".join(nomes))
        print("\n")
        mandado = suspeitos
        return mandado
    elif len(suspeitos) == 0:
        print(
            "Não há suspeitos compatíveis com as características fornecidas. Volte aqui quando tiver mais informações."
        )
        mandado = None
        return mandado
    elif len(suspeitos) > 1:
        nomes = []
        for suspeito in suspeitos:
            nomes.append(suspeito.nome)

        print("Os suspeitos são:\n")
        print(", ".join(nomes))
        print("\nVolte aqui quando tiver mais informações.\n")
        mandado = None
        return mandado


def le_caracteristica(nome_caracteristica, opcoes):
    nome_caracteristica = nome_caracteristica.title()
    valor = input(f"{nome_caracteristica}: ")
    while valor != "" and normaliza_string(valor) not in opcoes:
        print(f"{nome_caracteristica} inválido '{valor}'. Esperava {opcoes} ou Enter.")
        valor = input(f"{nome_caracteristica}: ")
    return valor


def busca_suspeito():
    suspeitinhos = suspeitos.copy()

    genero = le_caracteristica("Gênero", dados.GENEROS)
    if genero != "":
        suspeitinhos = busca_genero(suspeitinhos, genero)

    cabelo = le_caracteristica("Cabelo", dados.CABELOS)
    if cabelo != "":
        suspeitinhos = busca_cabelo(suspeitinhos, cabelo)

    comida = le_caracteristica("Comida", dados.COMIDAS)
    if comida != "":
        suspeitinhos = busca_comida(suspeitinhos, comida)

    esporte = le_caracteristica("Esporte", dados.ESPORTES)
    if esporte != "":
        suspeitinhos = busca_esporte(suspeitinhos, esporte)

    hobby = le_caracteristica("Hobby", dados.HOBBIES)
    if hobby != "":
        suspeitinhos = busca_hobby(suspeitinhos, hobby)

    musica = le_caracteristica("Música", dados.MUSICAS)
    if musica != "":
        suspeitinhos = busca_musica(suspeitinhos, musica)

    if debug:
        print(suspeitinhos)
    return suspeitinhos


def normaliza_string(string):
    return unicodedata.normalize("NFKD", string).encode("ASCII", "ignore").decode("ASCII").lower()


def busca_genero(suspeitinhos, genero):
    resultado = []
    for suspeito in suspeitinhos:
        if normaliza_string(genero) == normaliza_string(suspeito.genero):
            resultado.append(suspeito)
    return resultado


def busca_cabelo(suspeitinhos, cabelo):
    resultado = []
    for suspeito in suspeitinhos:
        if normaliza_string(cabelo) == normaliza_string(suspeito.cabelo):
            resultado.append(suspeito)
    return resultado


def busca_comida(suspeitinhos, comida):
    resultado = []
    for suspeito in suspeitinhos:
        if normaliza_string(comida) == normaliza_string(suspeito.comida):
            resultado.append(suspeito)
    return resultado


def busca_esporte(suspeitinhos, esporte):
    resultado = []
    for suspeito in suspeitinhos:
        if normaliza_string(esporte) == normaliza_string(suspeito.esporte):
            resultado.append(suspeito)
    return resultado


def busca_hobby(suspeitinhos, hobby):
    resultado = []
    for suspeito in suspeitinhos:
        if normaliza_string(hobby) == normaliza_string(suspeito.hobby):
            resultado.append(suspeito)
    return resultado


def busca_musica(suspeitinhos, musica):
    resultado = []
    for suspeito in suspeitinhos:
        if normaliza_string(musica) == normaliza_string(suspeito.musica):
            resultado.append(suspeito)
    return resultado


def sorteia_caracteristica(culpado):
    sorteada = random.randint(0, 4)
    if sorteada == 0:
        if culpado.genero == "Homem":
            return "Ele tinha cabelo " + culpado.cabelo + "."
        else:
            return "Ela tinha cabelo " + culpado.cabelo + "."
    if sorteada == 1:
        if culpado.genero == "Homem":
            if culpado.comida == "Frutos do mar":
                return "Vi que ele comeu em um restaurante de " + culpado.comida + "."
            else:
                return "Vi que ele comeu em um restaurante de comida " + culpado.comida + "."
        else:
            if culpado.comida == "Frutos do mar":
                return "Vi que ela comeu em um restaurante de " + culpado.comida + "."
            else:
                return "Vi que ela comeu em um restaurante de comida " + culpado.comida + "."
    if sorteada == 2:
        if culpado.genero == "Homem":
            return "Ele vestia uma camiseta de um time de " + culpado.esporte + "."
        else:
            return "Ela vestia uma camiseta de um time de " + culpado.esporte + "."
    if sorteada == 3:
        if culpado.genero == "Homem":
            return (
                "Ouvi partes de sua conversa no celular e ele parecia gostar de ser "
                + culpado.hobby
                + " nas horas vagas."
            )
        else:
            return (
                "Ouvi partes de sua conversa no celular e ela parecia gostar de ser "
                + culpado.hobby
                + " nas horas vagas."
            )
    if sorteada == 4:
        if culpado.genero == "Homem":
            if culpado.musica == "Classica":
                return "Ele tinha uma playlist de música " + culpado.musica + " em seu celular."
            else:
                return "Ele tinha uma playlist de " + culpado.musica + " em seu celular."
        else:
            if culpado.musica == "Classica":
                return "Ela tinha uma playlist de música " + culpado.musica + " em seu celular."
            else:
                return "Ela tinha uma playlist de " + culpado.musica + " em seu celular."


def sorteia_caracteristicas(culpado):
    return {
        "banco": sorteia_caracteristica(culpado),
        "aeroporto": sorteia_caracteristica(culpado),
        "biblioteca": sorteia_caracteristica(culpado),
    }


def investigar(culpado, prox_pais, caracteristicas):
    print("a - Banco")
    print("b - Aeroporto")
    print("c - Biblioteca")
    escolha = input("Aperte a tecla que corresponde ao que deseja fazer.")
    os.system("clear")
    if escolha == "a":
        print(
            "Gerente: A pessoa que você procura esteve aqui e trocou seu dinheiro por",
            prox_pais.moeda,
        )
        print(caracteristicas["banco"])
    elif escolha == "b":
        print(
            "Comissário de Bordo: A pessoa que você procura esteve aqui e partiu em um avião com uma bandeira",
            prox_pais.bandeira,
            "na asa.",
        )
        print(caracteristicas["aeroporto"])
    elif escolha == "c":
        print(
            "Bibliotecária: A pessoa que você procura esteve aqui e procurava informações sobre",
            prox_pais.cultura,
        )
        print(caracteristicas["biblioteca"])


debug = False


def le_escolha_ir_prox_caso(resposta, opcoes):
    resposta = normaliza_string(resposta)
    valor = resposta
    while valor not in opcoes:
        print("Resposta inválida: ", valor, "Esperava:", opcoes)
        valor = input("Digite novamente:")
        valor = normaliza_string(valor)
        resposta = valor
    if normaliza_string(resposta) == normaliza_string("não"):
        exit()
    elif normaliza_string(resposta) == normaliza_string("sim"):
        print("\n")
        principal()


def principal():
    id = input("Por favor, identifique-se: ")
    casos_resolvidos = identifica_usuario(id)
    cargo_atual = verifica_cargo(casos_resolvidos)
    data_atual = data_jogo()
    data_fim = datetime(2019, 1, 2, 12, 0, 0)
    culpado = escolhe_suspeito()
    pais_atual = escolhe_pais()
    cena_crime = pais_atual
    caso_atual = gera_caso(cena_crime, culpado, data_atual, data_fim, cargo_atual)
    prox_pais = gera_prox_pais(pais_atual)
    mandado = None

    caracteristicas = sorteia_caracteristicas(culpado)
    print("\n ")
    while True:
        menu_principal(pais_atual, data_atual)
        escolha = input("Aperte a tecla que corresponde ao que deseja fazer.")
        os.system("clear")
        if escolha == "1":
            lista_suspeitos()
            escolha = input("Aperte qualquer tecla para voltar ao menu.")
            os.system("clear")
        elif escolha == "2":
            mandado = processa_mandado()
            data_atual = data_atual + timedelta(hours=1)
            print(data_atual.strftime("%A %d/%m/%Y %H:%M"))
            print("\n")
            escolha = input("Aperte qualquer tecla para voltar ao menu")
            os.system("clear")
            # if escolha == "0" or escolha != "0":
            # pass
            # menu_principal(pais_atual)
            # os.system('clear')
        elif escolha == "3":
            pais_atual = viaja_exterior(pais_atual, prox_pais)
            prox_pais = gera_prox_pais(pais_atual)
            data_atual = data_atual + timedelta(hours=5)
            print(data_atual.strftime("%A %d/%m/%Y %H:%M"))
            print("\n")
            escolha = input("Aperte qualquer tecla para ir para o menu do próximo país.")
            caracteristicas = sorteia_caracteristicas(culpado)
            os.system("clear")
        elif escolha == "4":
            investigar(culpado, prox_pais, caracteristicas)
            data_atual = data_atual + timedelta(hours=2)
            print(data_atual.strftime("%A %d/%m/%Y %H:%M"))
            print("\n")
            escolha = input("Aperte qualquer tecla para voltar ao menu.")
            os.system("clear")
        elif escolha == "69":
            global debug
            print("EITA! Você é um churrascker e ativou o modo de debug!")
            print("O culpado é ", culpado.nome)
            debug = True
        if data_atual >= data_fim:
            if mandado is None:
                print(
                    "Você não expediu um mandado para",
                    culpado.nome,
                    ". Mais sorte da próxima vez!",
                )
                print("\n")
                print("Pronto(a) para o próximo caso?")
                resposta = input("Sim / Não: ")
                le_escolha_ir_prox_caso(resposta, dados.OPCOES)

            elif culpado not in mandado:
                print("Mandado =", mandado)
                print("Culpado =", culpado)
                print(
                    "Você expediu um mandado para a pessoa errada!",
                    culpado,
                    "escapou. Mais sorte da próxima vez!",
                )
                print("\n")
                print("Pronto(a) para o próximo caso?")
                resposta = input("Sim / Não:")
                le_escolha_ir_prox_caso(resposta, dados.OPCOES)
            elif culpado in mandado:
                print(
                    "Você prendeu",
                    culpado.nome,
                    ".",
                    culpado.nome,
                    "estava com o tesouro nacional que será devolvido a seus habitantes. Parabéns, Detetive!",
                )
                casos_resolvidos = casos_resolvidos + 1
                salva_jogo(casos_resolvidos, id)
                casos_promocao = verifica_promocao(cargo_atual, casos_resolvidos)
                print("\n")
                print("Pronto(a) para o próximo caso?")
                resposta = input("Sim / Não: ")
                le_escolha_ir_prox_caso(resposta, dados.OPCOES)


if __name__ == "__main__":
    principal()
