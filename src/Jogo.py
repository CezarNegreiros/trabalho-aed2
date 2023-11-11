from Labirinto import Labirinto
from Ponto import Ponto
from Estado import Estado,menor_passo, lista_visitados, heap, heap_tam, labirinto
from telas import tela_inicial,tela_final
import pygame
import Imagens as im
import time

#variaveis globais
ponto_inicial = Ponto(1,0)
caminho_certo = []
abriu = False

def solucao():
    global ponto_inicial

    estado_inicial = Estado(0, ponto_inicial, [(ponto_inicial.x,ponto_inicial.y)])
    heap.append(estado_inicial)
    lista_visitados = [ponto_inicial]
    solucao = menor_passo(estado_inicial)
    
    return solucao

def labirinto_in_game(labirinto, ponto, arbusto, grama, personagem, ovo):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
    desenhar_labirinto(labirinto, ponto,arbusto, grama, personagem,ovo)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        andar_para_cima(labirinto, ponto)
    elif keys[pygame.K_DOWN]:
        andar_para_baixo(labirinto, ponto)
    elif keys[pygame.K_LEFT]:
        andar_para_esquerda(labirinto, ponto)
    elif keys[pygame.K_RIGHT]:
        andar_para_direita(labirinto, ponto)
    elif keys[pygame.K_ESCAPE]:
        return False
    elif keys[pygame.K_s]:  # Adiciona esta parte para a tecla Enter
        caminho_certo = solucao()
        print(caminho_certo)
        if caminho_certo is not None:
            for passo in caminho_certo:
                novo_ponto = Ponto(passo[0],passo[1])
                desenhar_labirinto(labirinto, novo_ponto,arbusto, grama, personagem, ovo)
                pygame.display.update()
                time.sleep(0.2)
            tela_final()
            return False
        
    desenhar_labirinto(labirinto, ponto,arbusto, grama, personagem, ovo)
    
    return True

def atualizar_ponto(labirinto, ponto, new_x, new_y):
    if labirinto[new_x][new_y] != 'X':
        ponto.x = new_x
        ponto.y = new_y

def andar_para_cima(labirinto, ponto):
    if ponto.x > 0:
        atualizar_ponto(labirinto, ponto, ponto.x - 1, ponto.y)

def andar_para_baixo(labirinto, ponto):
    if ponto.x < 14:
        atualizar_ponto(labirinto, ponto, ponto.x + 1,ponto.y)

def andar_para_esquerda(labirinto, ponto):
    if ponto.y > 0:
        atualizar_ponto(labirinto, ponto, ponto.x,ponto.y - 1)

def andar_para_direita(labirinto, ponto):
    if ponto.y < 14:
        atualizar_ponto(labirinto, ponto, ponto.x,ponto.y + 1)

def verifica_vitoria(ponto):
    return ponto.x == 13 and ponto.y == 14 

def desenhar_labirinto(labirinto, ponto,arbusto,grama,personagem, ovo):
    tamanho_celula = 50
    tamanho_x = 15 * tamanho_celula 
    tamanho_y = 15 * tamanho_celula
    
    inicio_x = (WIDTH - tamanho_x) // 2
    inicio_y = (HEIGHT - tamanho_y) // 2

    for i in range(15):
        for j in range(15):
            
            win.blit(grama, (inicio_x + j * tamanho_celula, inicio_y + i * tamanho_celula))

            if labirinto[i][j] =='X':
                win.blit(arbusto, (inicio_x + j * tamanho_celula, inicio_y + i * tamanho_celula))

                # Desenha a saída do labirinto
                win.blit(ovo, (inicio_x + (15 - 1) * tamanho_celula, inicio_y + (15 - 2) * tamanho_celula)) 

            if i == ponto.x and j == ponto.y:
                win.blit(personagem, (inicio_x + j * tamanho_celula, inicio_y + i * tamanho_celula))            

labirinto = labirinto
pygame.init()

# Configurações da janela do jogo
tamanho_celula = 50
WIDTH = 15 * tamanho_celula 
HEIGHT = 15 * tamanho_celula
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Variáveis de controle de tempo
clock = pygame.time.Clock()
ultimo_movimento = pygame.time.get_ticks()
TEMPO_ENTRE_MOVIMENTOS = 1000

pygame.mixer.music.load('Musica/dragonball.mp3')

# Inicia a música (reproduz em um loop infinito)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

grama, arbusto, personagem, ovo = im.abrir_imagens(labirinto,WIDTH, HEIGHT)

run = True
def jogo(run):
    while run:
        
        global abriu
        if not abriu:  # Verifique se a tela inicial ainda não foi aberta
            abriu = tela_inicial()  

        # Chama a função para atualizar o jogo
        run = labirinto_in_game(labirinto, ponto_inicial, arbusto, grama, personagem, ovo)
        if verifica_vitoria(ponto_inicial):
            tela_final()
            break

        # Atualiza a tela
        pygame.display.update()

        # Define a taxa de quadros por segundo
        clock.tick(20)

    pygame.quit()

jogo(run)