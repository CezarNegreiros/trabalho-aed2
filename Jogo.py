from Jogador import Jogador
from Labirinto import Labirinto
import msvcrt

def labirinto_in_game(labirinto, jogador):
    while True:

        imprimir_labirinto(labirinto)
        key = msvcrt.getch()

        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'H':
                andar_para_cima(labirinto, jogador)
            elif key == b'P':
                andar_para_baixo(labirinto, jogador)
            elif key == b'K':
                andar_para_esquerda(labirinto,jogador)
            elif key == b'M':
                andar_para_direita(labirinto, jogador)
        elif key == b'w':
            andar_para_cima(labirinto, jogador)
        elif key == b'a':
            andar_para_esquerda(labirinto, jogador)
        elif key == b's':
            andar_para_baixo(labirinto, jogador)
        elif key == b'd':
            andar_para_direita(labirinto, jogador)
        elif key == b'q':
            break

        if verifica_vitoria(labirinto, jogador):
            print('VITORIAA (/^▽^)/')
            break
        else:
            print('+-'*15)

def mover_jogador(labirinto,  jogador,new_x, new_y):
        if labirinto.maze[new_x][new_y] != 'X' and new_x > -1 and new_x < labirinto.x + 1 and new_y > -1 and new_y < labirinto.y +1:
            labirinto.maze[new_x][new_y] = '*'
            labirinto.maze[jogador.posicao_x][jogador.posicao_y] = '0'
            if jogador.posicao_y != new_y:
                jogador.posicao_y = new_y
            if jogador.posicao_x != new_x:
                jogador.posicao_x = new_x
        else:
            print('MOVIMENTO INVALIDO')

def andar_para_cima(labirinto, jogador):
    mover_jogador(labirinto, jogador ,jogador.posicao_x - 1, jogador.posicao_y)

def andar_para_baixo(labirinto, jogador):
    mover_jogador(labirinto, jogador ,jogador.posicao_x + 1, jogador.posicao_y)

def andar_para_esquerda(labirinto,jogador):
    mover_jogador(labirinto, jogador ,jogador.posicao_x, jogador.posicao_y - 1)

def andar_para_direita(labirinto,jogador):
    mover_jogador(labirinto, jogador ,jogador.posicao_x, jogador.posicao_y + 1)

    
def verifica_vitoria(labirinto, jogaor):
    return labirinto.x - 2 == jogador.posicao_x and labirinto.y - 1 == jogador.posicao_y

def imprimir_labirinto(labirinto):
    for i in range(labirinto.x):
        for j in range(labirinto.y):
            print(labirinto.maze[i][j], end='')
        print()

#Cria jogador
jogador = Jogador(1, 0)
#Cria Labirinto
labirinto =  Labirinto()
#jogo
labirinto_in_game(labirinto,jogador)