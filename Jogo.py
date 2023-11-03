import Player
import Labirinto

#Cria jogador
jogador = Player(1, 0)

#Cria Labirinto
labirinto = Labirinto()
matriz = labirinto.criar_labirinto()
labirinto.imprimir_labirinto(matriz)