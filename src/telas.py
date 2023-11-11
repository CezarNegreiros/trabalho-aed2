import pygame
import sys

# Função para a tela inicial
def tela_inicial():
    pygame.init()

    tamanho_celula = 50
    WIDTH = 15 * tamanho_celula 
    HEIGHT = 15 * tamanho_celula
    
    tela = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption('Tela Inicial')

    grama = pygame.image.load('Imagens/grama.png')

    # TAMANHO DA FONTE
    fonte = pygame.font.Font('Fonte/super_mario_256/SuperMario256.ttf', 70)
    fonte2 = pygame.font.Font('Fonte/super_mario_256/SuperMario256.ttf', 35)

    # Títulos
    texto = fonte.render('H\' ESCAPE!', True, (0, 0, 0))
    posicao_texto = texto.get_rect(center=(WIDTH // 2, 150))

    # Textos informativos
    texto2 = fonte2.render('PRESSIONE \'S\' PARA A SOLUCAO', True, (0, 0, 0))
    posicao_texto2 = texto2.get_rect(center=(WIDTH // 2, 300))

    texto3 = fonte2.render('SETINHAS PARA CONTROLAR', True, (0, 0, 0))
    posicao_texto3 = texto3.get_rect(center=(WIDTH // 2, 350))

    texto4 = fonte2.render('PRESSIONE ESPACO PARA INICIAR JOGAR', True, (0, 0, 0))
    posicao_texto4 = texto4.get_rect(center=(WIDTH // 2, 500))

    # Redimensionar a imagem para o tamanho da tela
    grama = pygame.transform.scale(grama, (WIDTH, HEIGHT))

    while True:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return  True

        # Lógica da tela inicial

        # Preencher a tela com a imagem
        tela.blit(grama, (0, 0))
        tela.blit(texto, posicao_texto)
        tela.blit(texto2, posicao_texto2)
        tela.blit(texto3, posicao_texto3)
        tela.blit(texto4, posicao_texto4)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de atualização da tela
        pygame.time.Clock().tick(60)

def tela_final():
    pygame.init()

    WIDTH = 800
    HEIGHT = 800

    tela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tela Final - H\' ESCAPE')

    galinha_wins = pygame.image.load('Imagens/galinha_wins.jpeg')
    
    pygame.mixer.music.load('Musica/mario.mp3')

    # Inicia a música (reproduz em um loop infinito)
    pygame.mixer.music.play(-1)

    # TAMANHO DA FONTE
    fonte = pygame.font.Font('Fonte/super_mario_256/SuperMario256.ttf', 70)
    fonte2 = pygame.font.Font('Fonte/super_mario_256/SuperMario256.ttf', 35)

    # Títulos
    texto = fonte.render('H\' ESCAPE!', True, (0, 0, 0))
    posicao_texto = texto.get_rect(center=(WIDTH // 2, 150))

    # Textos informativos
    texto2 = fonte2.render('PARABENS, VOCE CONCLUIU LABIRINTO', True, (0, 0, 0))
    posicao_texto2 = texto2.get_rect(center=(WIDTH // 2, 400))

    texto3 = fonte2.render('APERTE SPACE PARA FECHAR O JOGO', True, (0, 0, 0))
    posicao_texto3 = texto3.get_rect(center=(WIDTH // 2, 450))


    # Redimensionar a imagem para o tamanho da tela
    galinha_wins = pygame.transform.scale(galinha_wins, (800, 800))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return  # Retornar para encerrar a função

        # Lógica da tela inicial

        # Preencher a tela com a imagem
        tela.blit(galinha_wins, (0, 0))
        tela.blit(texto, posicao_texto)
        tela.blit(texto2, posicao_texto2)
        tela.blit(texto3, posicao_texto3)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de atualização da tela
        pygame.time.Clock().tick(60)