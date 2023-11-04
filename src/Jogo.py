from Jogador import Jogador
from Labirinto import Labirinto
import pygame
from pygame import mixer

def labirinto_in_game(labirinto, jogador):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        andar_para_cima(labirinto, jogador)
    elif keys[pygame.K_DOWN]:
        andar_para_baixo(labirinto, jogador)
    elif keys[pygame.K_LEFT]:
        andar_para_esquerda(labirinto, jogador)
    elif keys[pygame.K_RIGHT]:
        andar_para_direita(labirinto, jogador)

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

    grama = pygame.transform.scale(grama, (tamanho_celula, tamanho_celula))  # Redimensiona a imagem para o tamanho da célula
    arbusto = pygame.transform.scale(arbusto, (tamanho_celula, tamanho_celula))  # Redimensiona a imagem para o tamanho da célula
    personagem = pygame.transform.scale(personagem, (tamanho_celula, tamanho_celula))  # Redimensiona a imagem para o tamanho da célula
    ovo = pygame.transform.scale(ovo, (tamanho_celula, tamanho_celula))  # Redimensiona a imagem para o tamanho da célula

    for i in range(labirinto.x):
        for j in range(labirinto.y):
            
            win.blit(grama, (inicio_x + j * tamanho_celula, inicio_y + i * tamanho_celula))

            if labirinto.maze[i][j] =='X':
                win.blit(arbusto, (inicio_x + j * tamanho_celula, inicio_y + i * tamanho_celula))
            if labirinto.maze[i][j] == '*':
                win.blit(personagem, (inicio_x + j * tamanho_celula, inicio_y + i * tamanho_celula))

    # Desenha a saída do labirinto
    win.blit(ovo, (inicio_x + (labirinto.x - 1) * tamanho_celula, inicio_y + (labirinto.y - 2) * tamanho_celula))


# Cria jogador
jogador = Jogador(1, 0)
# Cria Labirinto
labirinto = Labirinto()

# Inicializa o Pygame
pygame.init()
pygame.mixer.init()

# Configurações da janela do jogo
tamanho_celula = 50
WIDTH = labirinto.x * tamanho_celula
HEIGHT = labirinto.y * tamanho_celula
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Cria um relógio para controlar a taxa de quadros por segundo
clock = pygame.time.Clock()
FPS = 10  # Defina a taxa de quadros por segundo desejada

# Cria uma fonte
font = pygame.font.Font(None, 36)

# Variáveis de controle de tempo
ultimo_movimento = pygame.time.get_ticks()
TEMPO_ENTRE_MOVIMENTOS = 200  # 500 milissegundos (0.5 segundos)

imagem_grama = pygame.image.load('Imagens/grama.png')
imagem_arbusto = pygame.image.load('Imagens/arbusto.png')
imagem_personagem = pygame.image.load('Imagens/hlinha.png')
imagem_ovo = pygame.image.load("Imagens/ovo_branco.png")

# Loop principal do jogo
run = True
while run:
    run = labirinto_in_game(labirinto, jogador)
    # Preenche a janela de branco
    win.fill((112, 165, 49))

    # Desenha o labirinto diretamente na janela
    desenhar_labirinto(labirinto, imagem_arbusto, imagem_grama, imagem_personagem, imagem_ovo)

    if verifica_vitoria(labirinto, jogador):
        print('VITÓRIA (/^▽^)/')
        break

    # Atualiza a tela
    pygame.display.update()

    # Limita a taxa de quadros por segundo
    clock.tick(FPS)

# Finaliza o Pygame
pygame.quit()
