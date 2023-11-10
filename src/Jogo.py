from Labirinto import Labirinto
import pygame
import Imagens as im

# lista global que representa as posições já visitadas 
lista_visitados = []
resultado = []
heap_tam = -1


def menor_passo(posicao, jogador, labirinto):
    global heap_tam

    if posicao[0] == 13 and posicao[1] == 14:
        return posicao
    else:
        lista_aprovados = transicao(jogador,labirinto)
        lista_visitados.append(posicao)
        print(lista_visitados)
        heap = []
        for i in lista_aprovados:
            heap = insere_chave(heap,heap_tam,i)
            print(heap)
            elemento = heap[0]
            jogador.posicao_x = elemento[0]
            jogador.posicao_y = elemento[1]
            remove_heap(heap,heap_tam,0)

        return menor_passo(elemento,jogador, labirinto)

def insere_chave(heap,pos,chave):
    global heap_tam
	
    heap.append(None)
	
    heap[heap_tam] = chave
    heap_tam += 1
	
    heap = aumentar_chave(heap, heap_tam,chave)
    return heap  

def aumentar_chave(heap, pos, novo):
	
    heap[pos] = novo
    pai = (pos - 1) // 2
	
    while pos > 0 and heap[pai] > novo:
		
        heap[pai], heap[pos] = heap[pos], heap[pai]
        pos = pai
        pai = (pos - 1) //2

    return heap

def min_heapify(lista, i,tam):
	
	min = i
	filho_esquerdo = 2 * i + 1
	filho_direito = 2 * i + 2

	if filho_esquerdo < tam and lista[filho_esquerdo][2] < lista[min][2]:
		min = filho_esquerdo
		
	if filho_direito < tam and lista[filho_direito][2] < lista[min][2]:
		min = filho_direito
	
	if min != i:
		lista[i], lista[min] = lista[min], lista[i]
		min_heapify(lista, min, tam)

	return lista



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
TEMPO_ENTRE_MOVIMENTOS = 100

grama, arbusto, personagem, ovo = im.abrir_imagens(labirinto,WIDTH, HEIGHT)

run = True
heuristica = calculo_heuristica(labirinto.saida_x,labirinto.saida_y,jogador.posicao_x, jogador.posicao_y )

menor_passo((jogador.posicao_x, jogador.posicao_y,heuristica),jogador,labirinto)
first_click = True

run = True
#while run:
#
#   # Chama a função para atualizar o jogo
#    run = labirinto_in_game(labirinto, jogador, arbusto, grama, personagem, ovo)
#    if verifica_vitoria(labirinto, jogador):
#        break

    # Atualiza a tela
#   pygame.display.update()

    # Define a taxa de quadros por segundo
#    clock.tick(60)

# Finaliza o Pygame
pygame.quit()