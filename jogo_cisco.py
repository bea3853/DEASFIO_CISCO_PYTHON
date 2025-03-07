import random
import time

def interfacetabuleiro(tabuleiro):
    print("+" + ("+" * 3))
    for linha in tabuleiro:
        print("|" + "|".join(f" {c} " for c in linha) + "|")
        print("+" + ("+" * 3))

def verifica_movimento(movimento, numeros):
    if movimento in numeros:
        return False
    else:
        numeros.append(movimento)
        return True

def movimentacao(tabuleiro, movimento, tip):
    l, c = (int(movimento) - 1) // 3, (int(movimento) - 1) % 3
    tabuleiro[l][c] = tip
    return tabuleiro

def verifica_vitoria(tabuleiro, t):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == t:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == t:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == t:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == t:
        return True
    return False

def menu_inicial():
    while True:
        a = input("1 - contra a maquina, 2 para jogar com algum, ou 3 para IA x IA: ")
        if a in {"1", "2", "3"}:
            return int(a)

def user(tabuleiro, numeros, tip):
    while True:
        move = input(f"Digite seu movimento({tip}): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            if verifica_movimento(move, numeros):
                return movimentacao(tabuleiro, move, tip)
            else:
                print("Movimento inválido")
        else:
            print("Entrada inválida")

def jogada_pc(tabuleiro, numeros, tip):
    while True:
        move = str(random.randint(1, 9))
        if verifica_movimento(move, numeros):
            print(f"Aguardando jogada do jogador '{tip}' ...")
            time.sleep(2)
            return movimentacao(tabuleiro, move, tip)

def jogo():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    numeros = []
    jogador = "X"
    interfacetabuleiro(tabuleiro)

    for i in range(9):
        if jogador == "X":
            if r_menu == 1 or r_menu == 2:
                tabuleiro = user(tabuleiro, numeros, jogador)
            else:
                tabuleiro = jogada_pc(tabuleiro, numeros, jogador)
        else:
            if r_menu == 2:
                tabuleiro = user(tabuleiro, numeros, jogador)
            else:
                tabuleiro = jogada_pc(tabuleiro, numeros, jogador)

        interfacetabuleiro(tabuleiro)

        if verifica_vitoria(tabuleiro, jogador):
            jogador = input('digite seu nome')
            print(f"Jogador '{jogador}' venceu!")
            break
        elif i == 8:
            print("Empate.")
            break

        jogador = "O" if jogador == "X" else "X"

r_menu = menu_inicial()
if r_menu:
    jogo()
