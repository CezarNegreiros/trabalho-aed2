from Ponto import Ponto
from Labirinto import Labirinto

#variaveis globais
lista_visitados = []
heap_tam = 0
heap = []

def min_heapify(lista, i, tam):
	
	min = i
	
	filho_esquerdo = 2 * i + 1
	if filho_esquerdo < tam and lista[filho_esquerdo] < lista[min]:
		min = filho_esquerdo
		
	filho_direito = 2 * i + 2
	if filho_direito < tam and lista[filho_direito] < lista[min]:
		min = filho_direito
	
	if min != i:
		lista[i], lista[min] = lista[min], lista[i]
		min_heapify(lista, min, tam)

	return lista

def insere_chave(heap, tam, chave):
	global heap_tam
     
	heap.append(None)
	heap[heap_tam] = chave
	heap_tam += 1

	heap = aumentar_chave(heap, tam, chave)
	
	return heap

def aumentar_chave(heap, pos, novo):
	
	heap[pos] = novo
	pai = (pos - 1) // 2
	
	while pos > 0 and heap[pai] > novo:
		
		heap[pai], heap[pos] = heap[pos], heap[pai]
		pos = pai
		pai = (pos - 1) // 2

	return heap

def remove_heap(heap, tam, pos):
    global heap_tam
    heap[pos], heap[heap_tam - 1] = heap[heap_tam - 1], heap[pos]
    heap_tam -= 1
    min_heapify(heap, tam - 1, pos)

    return heap[tam - 1] 

class Estado:
    def __init__ (self, passos,ponto, caminho):
		
        self.ponto = ponto
        self.labirinto = Labirinto().get_labirinto()

        self.caminho = caminho

        self.g = passos
        self.h = self.calcula_heuristica(13,14)
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f 

    def __repr__(self):
        return str((ponto.x,ponto.y))
    
    def calcula_heuristica(self, x, y):
        return abs(self.ponto.x - x) + abs(self.ponto.y - y)

    def transicoes(self):

        saida = []

        # checa para cima
        if self.ponto.x > 0 and self.labirinto[self.ponto.x - 1][self.ponto.y] != 'X':
            ponto = Ponto(self.ponto.x - 1, self.ponto.y)

            if ponto not in lista_visitados:
                print('cima')
                saida.append(Estado(self.g + 1, ponto,  self.caminho + [(self.ponto.x - 1, self.ponto.y)]))

        # checa para baixo
        if self.ponto.x < 14 and self.labirinto[self.ponto.x + 1][self.ponto.y] != 'X':
            ponto = Ponto(self.ponto.x + 1, self.ponto.y)
            
            if ponto not in lista_visitados:
                print('baixo')
                saida.append(Estado(self.g + 1, ponto, self.caminho + [(self.ponto.x + 1, self.ponto.y)]))

        # checa para direita
        if self.ponto.y < 14 and self.labirinto[self.ponto.x][self.ponto.y + 1] != 'X':
            ponto = Ponto(self.ponto.x, self.ponto.y + 1)

            if ponto not in lista_visitados:
                print('direita')
                saida.append(Estado(self.g + 1, ponto, self.caminho + [(self.ponto.x, self.ponto.y+1)]))

        # checa para esquerda
        if self.ponto.y > 0 and self.labirinto[self.ponto.x][self.ponto.y - 1] != 'X':
            ponto = Ponto(self.ponto.x, self.ponto.y - 1)

            if ponto not in lista_visitados:
                print('esqueda')
                saida.append(Estado(self.g + 1, ponto, self.caminho + [(self.ponto.x, self.ponto.y-1)]))

        return saida

def menor_passo(estado):
    global heap

    while(len(heap) > 0):

        if estado.ponto == Ponto(13,14):
            return estado.caminho
        
        else:
            lista_aprovados = estado.transicoes()
            lista_visitados.append(estado.ponto)

            remove_heap(heap, heap_tam, 0)

            for i in lista_aprovados:
                heap = insere_chave(heap, len(heap), i)
            
            estado = heap[0]


ponto = Ponto(1,0)
estado = Estado(0, ponto, [(ponto.x,ponto.y)])
heap.append(estado)
#obj_f = menor_passo(estado)
print(estado.transicoes())
print(estado.labirinto[1][0])
print(estado.labirinto[0][1])
print(estado.labirinto[2][1])