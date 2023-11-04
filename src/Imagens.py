
import pygame
from Labirinto import Labirinto

def abrir_imagens(labirinto, WIDTH, HEIGHT):

    tamanho_celula = 50
    tamanho_x = labirinto.x * tamanho_celula
    tamanho_y = labirinto.y * tamanho_celula
    
    inicio_x = (WIDTH - tamanho_x) // 2
    inicio_y = (HEIGHT - tamanho_y) // 2

    grama = pygame.image.load('Imagens/grama.png')
    arbusto = pygame.image.load('Imagens/arbusto.png')
    personagem = pygame.image.load('Imagens/hlinha.png')
    ovo = pygame.image.load('Imagens/ovo_branco.png')

    grama = pygame.transform.scale(grama, (tamanho_celula, tamanho_celula))  # Redimensiona a imagem para o tamanho da célula
    arbusto = pygame.transform.scale(arbusto, (tamanho_celula, tamanho_celula))  # Redimensiona a imagem para o tamanho da célula
    personagem = pygame.transform.scale(personagem, (tamanho_celula, tamanho_celula))  # Redimensiona a imagem para o tamanho da célula
    ovo = pygame.transform.scale(ovo, (tamanho_celula, tamanho_celula))  # Redimensiona a imagem para o tamanho da célula

    return grama,arbusto,personagem,ovo
