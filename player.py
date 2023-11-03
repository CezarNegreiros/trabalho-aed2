class Player:
    def __init__(self, posicao_x, posicao_y):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
    
    def mover_cima(self):
        self.posicao_y -= 1
    
    def mover_baixo(self):
        self.posicao_y += 1
    
    def mover_direita(self):
        self.posicao_x += 1

    def mover_esquerda(self):
        self.posicao_x -= 1