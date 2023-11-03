import random

class Labirinto:
    def __init__(self):

        # Tamanho do labirinto
        self.x = 15
        self.y = 15
        # Cria o labirinto
        self.maze = self.criar_labirinto()
    
    def criar_labirinto(self):
         
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

        matriz[1][0] = '*'    
        return matriz
    
    def imprimir_labirinto(self):
        # Imprime o labirinto
        for i in range(self.x):
            for j in range(self.y):
                print(self.maze[i][j], end=' ')
            print()