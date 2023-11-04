from Jogador import Jogador
from Labirinto import Labirinto
import pygame
import Imagens as im
import Menu as menu



def labirinto_in_game(labirinto, jogador, arbusto, grama, personagem, ovo):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
    desenhar_labirinto(labirinto, arbusto, grama, personagem,ovo)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        andar_para_cima(labirinto, jogador)
    elif keys[pygame.K_DOWN]:
        andar_para_baixo(labirinto, jogador)
    elif keys[pygame.K_LEFT]:
        andar_para_esquerda(labirinto, jogador)
    elif keys[pygame.K_RIGHT]:
        andar_para_direita(labirinto, jogador)
    elif keys[pygame.K_ESCAPE]:
        return False 
    desenhar_labirinto(labirinto, arbusto, grama, personagem,ovo)
    
    return True

def mover_jogador(labirinto, jogador, new_x, new_y):
    if labirinto.maze[new_x][new_y] != 'X':
        labirinto.maze[new_x][new_y] = '*'
        labirinto.maze[jogador.posicao_x][jogador.posicao_y] = '0'
        jogador.posicao_x = new_x
        jogador.posicao_y = new_y

def andar_para_cima(labirinto, jogador):
    if jogador.posicao_x > 0:
        mover_jogador(labirinto, jogador, jogador.posicao_x - 1, jogador.posicao_y)

def andar_para_baixo(labirinto, jogador):
    if jogador.posicao_x < labirinto.x - 1:
        mover_jogador(labirinto, jogador, jogador.posicao_x + 1, jogador.posicao_y)

def andar_para_esquerda(labirinto, jogador):
    if jogador.posicao_y > 0:
        mover_jogador(labirinto, jogador, jogador.posicao_x, jogador.posicao_y - 1)

def andar_para_direita(labirinto, jogador):
    if jogador.posicao_y < labirinto.y - 1:
        mover_jogador(labirinto, jogador, jogador.posicao_x, jogador.posicao_y + 1)

def verifica_vitoria(labirinto, jogador):
    return labirinto.maze[labirinto.x - 2][labirinto.y - 1] == '*'

def desenhar_labirinto(labirinto, arbusto,grama,personagem, ovo):
    tamanho_celula = 50
    tamanho_x = labirinto.x * tamanho_celula
    tamanho_y = labirinto.y * tamanho_celula
    
    inicio_x = (WIDTH - tamanho_x) // 2
    inicio_y = (HEIGHT - tamanho_y) // 2

    for i in range(labirinto.x):
        for j in range(labirinto.y):
            
            win.blit(grama, (inicio_x + j * tamanho_celula, inicio_y + i * tamanho_celula))

            if labirinto.maze[i][j] =='X':
                win.blit(arbusto, (inicio_x + j * tamanho_celula, inicio_y + i * tamanho_celula))

                # Desenha a saída do labirinto
                win.blit(ovo, (inicio_x + (labirinto.x - 1) * tamanho_celula, inicio_y + (labirinto.y - 2) * tamanho_celula)) 

            if labirinto.maze[i][j] == '*':
                win.blit(personagem, (inicio_x + j * tamanho_celula, inicio_y + i * tamanho_celula))

jogador = Jogador(1, 0)
labirinto = Labirinto()

# Inicializa o Pygame
pygame.init()

# Configurações da janela do jogo
tamanho_celula = 50
WIDTH = labirinto.x * tamanho_celula
HEIGHT = labirinto.y * tamanho_celula
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Variáveis de controle de tempo
clock = pygame.time.Clock()
ultimo_movimento = pygame.time.get_ticks()
TEMPO_ENTRE_MOVIMENTOS = 200 

grama, arbusto, personagem, ovo = im.abrir_imagens(labirinto,WIDTH, HEIGHT)

run = True

first_click = True
# Loop principal do jogo
# Loop principal do jogo
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    labirinto_in_game(labirinto, jogador,arbusto,grama,personagem,ovo)
    
    if verifica_vitoria(labirinto, jogador):
        break

    pygame.display.update()

    clock.tick(15)

# Finaliza o Pygame
pygame.quit()