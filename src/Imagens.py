
import pygame
from Labirinto import Labirinto

def abrir_imagens(labirinto, WIDTH, HEIGHT):

    tamanho_celula = 50
    tamanho_x = 15 * tamanho_celula
    tamanho_y = 15 * tamanho_celula
    
    inicio_x = (WIDTH - tamanho_x) // 2
    inicio_y = (HEIGHT - tamanho_y) // 2

    grama = pygame.image.load('src/Imagens/grama.png')
    arbusto = pygame.image.load('src/Imagens/arbusto.png')
    personagem = pygame.image.load('src/Imagens/hlinha.png')
    ovo = pygame.image.load('src/Imagens/ovo_branco.png')

    grama = pygame.transform.scale(grama, (tamanho_celula, tamanho_celula))  
    arbusto = pygame.transform.scale(arbusto, (tamanho_celula, tamanho_celula))  
    personagem = pygame.transform.scale(personagem, (tamanho_celula, tamanho_celula))  
    ovo = pygame.transform.scale(ovo, (tamanho_celula, tamanho_celula))  

    return grama,arbusto,personagem,ovo

def menu_principal(labirinto, WIDTH, HEIGHT):

    tamanho_celula = 50
    tamanho_x = 15 * tamanho_celula
    tamanho_y = 15 * tamanho_celula
    
    inicio_x = (WIDTH - tamanho_x) // 2
    inicio_y = (HEIGHT - tamanho_y) // 2

    grama = pygame.image.load('src/Imagens/grama.png')
    arbusto = pygame.image.load('src/Imagens/arbusto.png')
    personagem = pygame.image.load('/srcImagens/hlinha.png')
    ovo = pygame.image.load('src/Imagens/ovo_branco.png')

    grama = pygame.transform.scale(grama, (tamanho_celula, tamanho_celula))  
    arbusto = pygame.transform.scale(arbusto, (tamanho_celula, tamanho_celula))  
    personagem = pygame.transform.scale(personagem, (tamanho_celula, tamanho_celula))  
    ovo = pygame.transform.scale(ovo, (tamanho_celula, tamanho_celula))  

    return grama,arbusto,personagem,ovo