import random
import msvcrt

"""
Módulo de Geração de Labirinto

Este módulo define a classe Labirinto, que permite criar e imprimir um labirinto aleatório
usando o algoritmo de Prim's.

Classe:
    Labirinto: Representa um labirinto com métodos para criar e imprimir o labirinto.

Uso:
    maze = Labirinto()       # Cria uma instância do Labirinto
    maze.imprimir_labirinto()  # Imprime o labirinto gerado

Autor:
    Gabriel Takeda
    Carlos Cezar
    Jose Getulio
"""

class Labirinto:
    def _init_(self):

        """
        Inicializa um objeto Labirinto com um tamanho predefinido.

        O tamanho padrão do labirinto é 31x31.

        Atributos:
            self.x (int): Largura do labirinto.
            self.y (int): Altura do labirinto.
            self.labirinto (list): Representação do labirinto como uma matriz.
        """

        # Tamanho do labirinto
        self.x = 15
        self.y = 15
        self.posicaoX = 1
        self.posicaoY = 0

        #Cria jogador

        
        # Cria o labirinto
        self.labirinto = self.criar_labirinto()
        self.jogador ='*'
        self.labirinto[self.posicaoX][self.posicaoY] = self.jogador
    
    def verifica_vitoria(self):
        return maze.x - 2 == maze.posicaoX and maze.y - 1 == maze.posicaoY
    
    def criar_labirinto(self):

        """
        Cria um labirinto aleatório usando o algoritmo de Prim's.

        Retorna:
            list: Uma matriz representando o labirinto com caminhos e paredes.
        """
         
        # Inicializa uma matriz preenchida com paredes ('W')
        matriz = [['X' for _ in range(self.x)] for _ in range(self.y)]

        def verifica_validade(x, y):
            # Verifica se as coordenadas estão dentro dos limites do labirinto
            return 0 <= x < self.x and 0 <= y < self.y

        def marca_visita(x, y):
            # Marca a célula como marca_visitaada ('0')
            matriz[x][y] = '0'

        def adicionar_muro(x, y):
            # Embaralha a ordem das direções
            direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(direcoes)
            
            # Tenta criar caminhos a partir da célula atual
            for dx, dy in direcoes:
                new_x, new_y = x + 2 * dx, y + 2 * dy
                if verifica_validade(new_x, new_y) and matriz[new_x][new_y] == 'X':
                    # Marca as células envolvidas como marca_visitaadas
                    marca_visita(new_x, new_y)
                    marca_visita(x + dx, y + dy)
                    # Recursivamente continua a criação do caminho
                    adicionar_muro(new_x, new_y)

        start_x, start_y = 1, 0
        end_x, end_y = self.x - 2, self.y - 1
        
        # Marca a célula de início e cria caminhos
        marca_visita(start_x, start_y)
        adicionar_muro(start_x, start_y)
        
        # Marca a célula de fim
        marca_visita(end_x, end_y)
    
        return matriz
    
    def imprimir_labirinto(self):
        # Imprime o labirinto
        for i in range(self.x):
            for j in range(self.y):
                print(self.labirinto[i][j], end=' ')
            print()
    
    def mover_jogador(self, new_x, new_y):
        try:
            if self.labirinto[new_x][new_y] != 'X' and new_x > -1 and new_x < maze.x +1 and new_y > -1 and new_y < maze.y +1:
                self.labirinto[new_x][new_y] = '*'
                self.labirinto[self.posicaoX][self.posicaoY] = '0'
                if self.y != new_y:
                    self.posicaoY = new_y
                if self.x != new_x:
                    self.posicaoX = new_x
            else:
                print('MOVIMENTO INVALIDO')
        except:
            print('movimento invalido')
    
    def andar_para_cima(self):
        self.mover_jogador(self.posicaoX - 1, self.posicaoY)

    def andar_para_baixo(self):
        self.mover_jogador(self.posicaoX + 1, self.posicaoY)

    def andar_para_esquerda(self):
        self.mover_jogador(self.posicaoX, self.posicaoY - 1)

    def andar_para_direita(self):
        self.mover_jogador(self.posicaoX, self.posicaoY + 1)


def labirinto_in_game(maze):
    while True:

        key = msvcrt.getch()

        
        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'H':
                maze.andar_para_cima()
            elif key == b'P':
                maze.andar_para_baixo()
            elif key == b'K':
                maze.andar_para_esquerda()
            elif key == b'M':
                maze.andar_para_direita()
        elif key == b'w':
            maze.andar_para_cima()
        elif key == b'a':
            maze.andar_para_esquerda()
        elif key == b's':
            maze.andar_para_baixo()
        elif key == b'd':
            maze.andar_para_direita()
        elif key == b'q':
            break

        if maze.verifica_vitoria():
            maze.imprimir_labirinto()
            print('VITORIAA (/^▽^)/')
            break
        else:
            print('+-'*15)
            maze.imprimir_labirinto()

        

# Cria uma instância da classe Labirinto
maze = Labirinto()
# Imprime o labirinto
maze.imprimir_labirinto()
labirinto_in_game(maze)