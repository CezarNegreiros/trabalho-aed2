# trabalho-aed2

## Como Jogar ?

Execute o arquivo “Jogo.py”. Em seguida, será aberto um menu principal com instruções de qual modo de jogo estão disponíveis. O usuário deve apertar a tecla “ESPAÇO” para inicializar o labirinto, para  jogar o labirinto por conta própria, basta mover o personagem(H´) utilizando as setas: para cima (↑), para baixo (↓), para esquerda (←) ou para a direita (→); para ter acesso à solução automática, o usuário deve selecionar a tecla “S”. Por fim, se o usuário escolher a tecla “ESC” a aplicação será encerrada.

## Arquivo Estado.py

Este arquivo contém implementações relacionadas à busca de menor caminho em um labirinto usando um algoritmo baseado em A* com uma fila de prioridade implementada como um heap mínimo.

Funções Principais:
1. min_heapify(lista, i, tam)
Função para manter a propriedade de heap mínimo. Recebe uma lista, um índice i e o tamanho da lista (tam). Retorna a lista após realizar as operações de heap mínimo.
2. insere_chave(heap, tam, chave)
Adiciona uma chave ao heap e chama a função aumentar_chave para garantir que a propriedade de heap seja mantida. Retorna o heap atualizado.
3. aumentar_chave(heap, pos, novo)
Atualiza a chave em uma posição específica do heap e ajusta a posição da chave conforme necessário para manter a propriedade de heap mínimo. Retorna o heap atualizado.
4. remove_heap(heap, tam, pos)
Remove um elemento do heap em uma posição específica e ajusta a posição da chave conforme necessário para manter a propriedade de heap mínimo. Retorna o elemento removido.

## Classe Estado:

### Atributos:
- ponto: Um objeto da classe Ponto que representa a posição no labirinto.
- caminho: Uma lista de coordenadas representando o caminho percorrido até o estado atual.
- g: O custo real do caminho do estado inicial até o estado atual.
- h: O custo estimado do caminho do estado atual até o objetivo (heurística).
- f: A soma de g e h, representando a função de avaliação.


### Métodos:

**__init__(self, passos, ponto, caminho)**
- Construtor da classe Estado. Inicializa os atributos com base nos parâmetros fornecidos.

**__lt__(self, other)**
- Método de comparação para permitir a ordenação dos estados com base em f.

**calcula_heuristica(self, x, y)**
- Calcula a heurística para o estado atual, estimando o custo para atingir o objetivo (representado por coordenadas x e y).

**transicoes(self)**
- Gera os possíveis estados sucessores a partir do estado atual.

## Função menor_passo(estado)

#### Variáveis Globais:

- lista_visitados: Lista que mantém um registro dos pontos já visitados durante a busca.
- heap_tam: Variável global que controla o tamanho atual do heap.
- heap: Heap mínimo utilizado para armazenar estados durante a busca.
- labirinto: Objeto da classe Labirinto que representa a estrutura do labirinto.
- Este arquivo tem como objetivo fornecer uma estrutura modular para realizar a busca do menor caminho em um labirinto.


## Arquivo tela.py

Este arquivo contém implementações relacionadas às telas do jogo, incluindo a tela inicial e a tela final.

### Função tela_inicial():

**_Descrição_:**

Esta função cria a tela inicial do jogo, exibindo títulos, textos informativos e uma imagem de fundo. Ela aguarda a tecla de espaço ser pressionada para iniciar o jogo.

**_Fluxo de Execução_:** 
Inicializa o Pygame.
Configura as dimensões da tela com base no tamanho da célula e cria a janela.
Carrega a imagem de fundo (grama) e redimensiona para preencher a tela.
Configura títulos e textos informativos com diferentes fontes e tamanhos.
Entra em um loop infinito até que a tecla de espaço seja pressionada ou o usuário feche a janela.
Preenche a tela com a imagem de fundo, títulos e textos informativos.
Atualiza a tela e controla a taxa de atualização.

**_Retorno_:**
Retorna True quando a tecla de espaço é pressionada, indicando que o jogo deve começar.

### Função tela_final():

**_Descrição_:**
Esta função cria a tela final do jogo, exibindo uma imagem de vitória, títulos e textos informativos. Além disso, reproduz uma trilha sonora em loop.

**_Fluxo de Execução_**:
Inicializa o Pygame.
Configura as dimensões da tela e cria a janela.
Carrega a imagem de vitória (galinha_wins) e redimensiona para preencher a tela.
Inicia a reprodução da trilha sonora em loop.
Configura títulos e textos informativos com diferentes fontes e tamanhos.
Entra em um loop infinito até que a tecla de espaço seja pressionada ou o usuário feche a janela.
Preenche a tela com a imagem de vitória, títulos e textos informativos.
Atualiza a tela e controla a taxa de atualização.

**_Retorno_**:
Retorna quando a tecla de espaço é pressionada, indicando que o jogo deve ser encerrado.

### Observações Gerais:
- Ambas as funções utilizam a biblioteca Pygame para manipulação de janelas, eventos e imagens.
- As imagens utilizadas são redimensionadas para preencher a tela.
- A função pygame.mixer.music.load é usada para carregar a trilha sonora, e pygame.mixer.music.play(-1) inicia a reprodução em loop.
- Os eventos de teclado (tecla de espaço) são utilizados para controlar o fluxo entre as telas.
- O Pygame Clock é utilizado para controlar a taxa de atualização da tela.
  
Este arquivo fornece a estrutura básica para a exibição das telas do jogo, criando uma experiência visual e sonora para o usuário.


## Arquivo Labirinto.py

Este arquivo contém a implementação da classe Labirinto, que representa um labirinto gerado aleatoriamente. O labirinto é utilizado no contexto de um jogo, e a classe oferece métodos para criar, imprimir e acessar o labirinto.

### Classe Labirinto:

**Método __init__(self):**

**_Descrição_:**
- O método de inicialização da classe Labirinto define o tamanho do labirinto e as coordenadas da saída.

**Método criar_labirinto(self)**:

**_Descrição_:**
- Este método cria um labirinto usando o algoritmo de geração de labirintos conhecido como "Randomized Prim's Algorithm". O labirinto é representado por uma matriz onde 'X' representa paredes e '0' representa caminhos.

#### Fluxo de Execução:
1. Inicializa uma matriz preenchida com paredes ('X').
2. Define funções auxiliares para verificar a validade de coordenadas, marcar uma célula como visitada e adicionar muros.
3. Marca a célula de início e chama a função recursiva adicionar_muro para criar caminhos no labirinto.
4. Marca a célula de fim.
5. Retorna a matriz do labirinto gerado.

**Método imprimir_labirinto(self)**:
_Descrição_:
- Este método imprime na saída padrão o labirinto representado pela matriz.
 
**Método get_labirinto(self)**:

**_Descrição_:**
- Este método retorna a matriz que representa o labirinto gerado.

### Observações Gerais:
- O labirinto gerado possui caminhos conectados da célula de início à célula de fim.
- A classe Labirinto utiliza o algoritmo de Prim para criar labirintos, resultando em uma estrutura de caminhos conectados aleatoriamente.
- A saída do labirinto está localizada na posição (13, 14).
- O labirinto é representado por uma matriz bidimensional de caracteres.
- A classe não é destinada a manipulações externas da matriz, apenas para criar e acessar o labirinto gerado.


## Arquivo Imagens.py

### Função abrir_imagens(labirinto, WIDTH, HEIGHT)

**_Parâmetros_**
- labirinto: Instância da classe Labirinto que contém a informação do labirinto.
- WIDTH: Largura da janela do jogo.
- HEIGHT: Altura da janela do jogo.

**_Descrição_:**
- Esta função carrega e redimensiona as imagens utilizadas no jogo para representar elementos como grama, arbustos, personagem e ovo.

**_Retorno_:**
- Retorna uma tupla contendo as imagens redimensionadas na seguinte ordem: (grama, arbusto, personagem, ovo).

### Função menu_principal(labirinto, WIDTH, HEIGHT)

**_Parâmetros_:**
- labirinto: Instância da classe Labirinto que contém a informação do labirinto.
- WIDTH: Largura da janela do jogo.
- HEIGHT: Altura da janela do jogo.

**_Descrição_:**
- Esta função é semelhante à função abrir_imagens e tem o mesmo propósito. No entanto, pode ser utilizada para carregar as imagens do menu principal do jogo.

**_Retorno_:**
- Retorna uma tupla contendo as imagens redimensionadas na seguinte ordem: (grama, arbusto, personagem, ovo).

### Observações Gerais:
- Ambas as funções utilizam a biblioteca Pygame para carregar e redimensionar as imagens.
- As imagens são redimensionadas para o tamanho de uma célula do labirinto, conforme especificado pelas variáveis tamanho_celula, tamanho_x e tamanho_y.
- As imagens são utilizadas posteriormente para desenhar o labirinto e elementos do jogo na tela.

## Arquivo Jogo.py

### Função solucao()

**_Descrição_:**
- A função solucao é responsável por encontrar a solução do labirinto e retorna o caminho certo para a saída.

**_Retorno_:**
- Retorna uma lista representando o caminho certo para a saída do labirinto.

### Função labirinto_in_game(labirinto, ponto, arbusto, grama, personagem, ovo)

**_Parâmetros__:**
- labirinto: Instância da classe Labirinto que contém a informação do labirinto.
- ponto: Instância da classe Ponto que representa a posição atual no labirinto.
- arbusto: Imagem representando um arbusto no jogo.
- grama: Imagem representando a grama no jogo.
- personagem: Imagem representando o personagem no jogo.
- ovo: Imagem representando o ovo no jogo.

**_Descrição_:**
- A função labirinto_in_game é responsável por gerenciar o jogo em si. Ela lida com os eventos do pygame, atualiza a posição do personagem, verifica se o jogador pressionou a tecla "S" para mostrar a solução, verifica se o jogador venceu e desenha o labirinto na tela.

**_Retorno_:**
- Retorna True se o jogo deve continuar e False se o jogador decidiu sair ou já venceu.

### Função atualizar_ponto(labirinto, ponto, new_x, new_y)

**_Parâmetros_:**
- labirinto: Instância da classe Labirinto que contém a informação do labirinto.
- ponto: Instância da classe Ponto que representa a posição atual no labirinto.
- new_x: Nova coordenada X para a posição do ponto.
- new_y: Nova coordenada Y para a posição do ponto.

### Descrição:
- A função atualizar_ponto verifica se a nova posição (new_x, new_y) é válida no labirinto e, se for o caso, atualiza a posição do ponto para essa nova coordenada.

### Funções andar_para_cima, andar_para_baixo, andar_para_esquerda e andar_para_direita
**_Parâmetros_:**
- labirinto: Instância da classe Labirinto que contém a informação do labirinto.
- ponto: Instância da classe Ponto que representa a posição atual no labirinto.

**_Descrição_:**
- Essas funções são responsáveis por mover o ponto para cima, para baixo, para a esquerda ou para a direita no labirinto, dependendo da tecla pressionada pelo jogador.

### Função verifica_vitoria(ponto)

**_Parâmetros_:**
- ponto: Instância da classe Ponto que representa a posição atual no labirinto.

**_Descrição_:**
- A função verifica_vitoria verifica se a posição atual do ponto corresponde à saída do labirinto.

### Função desenhar_labirinto(labirinto, ponto, arbusto, grama, personagem, ovo)

**_Parâmetros_:**
- labirinto: Instância da classe Labirinto que contém a informação do labirinto.
- ponto: Instância da classe Ponto que representa a posição atual no labirinto.
- arbusto: Imagem representando um arbusto no jogo.
- grama: Imagem representando a grama no jogo.
- personagem: Imagem representando o personagem no jogo.
-ovo: Imagem representando o ovo no jogo.

**_Descrição_:**
- A função desenhar_labirinto é responsável por desenhar o labirinto na tela do jogo, posicionando as imagens de acordo com as informações do labirinto e a posição do ponto.

### Função jogo(run)

**_Parâmetros_:**
- run: Variável que controla a execução do jogo.

**_Descrição_:**
- A função jogo é o ponto de entrada principal do jogo. Ela inicializa a janela do Pygame, carrega as imagens, inicia a música, abre a tela inicial, e chama a função labirinto_in_game para gerenciar o jogo.

### Observações Gerais:
- O código utiliza o módulo pygame para lidar com a interface gráfica do jogo.
- A música de fundo é carregada usando pygame.mixer.music, e é reproduzida em um loop infinito.
- O jogo é controlado pelas teclas de seta para cima, para baixo, para a esquerda e para a direita.
- Pressionar a tecla "S" durante o jogo exibe a solução do labirinto.
- O jogo é encerrado ao pressionar a tecla "ESC" ou ao vencer o labirinto.
- A função tela_inicial é chamada no início do jogo, e a função tela_final é chamada ao vencer o labirinto. Ambas interagem com o usuário exibindo informações na tela.

## Arquivo Ponto.y

### Classe Ponto

### Métodos:

### Método __init__(self, x, y)

**_Descrição:_**
- Método de inicialização da classe Ponto.
- Cria uma instância da classe Ponto com as coordenadas x e y.
  
**_Parâmetros:_**
- x: Valor da coordenada X.
- y: Valor da coordenada Y.
  
### Método __eq__(self, other)

**_Descrição_:**
- Método de comparação de igualdade.
- Compara se o ponto atual é igual a outro ponto.

**_Parâmetros_:**
- other: Outro objeto da classe Ponto para comparação.

**_Retorno_:**
- Retorna True se os pontos são iguais e False caso contrário.

### Método __repr__(self)
**_Descrição_:**
- Método de representação de string.
- Retorna uma representação em string do objeto no formato (x, y).

**_Retorno_:**
- Retorna uma string representando as coordenadas do ponto.

### Observações Gerais:
- A classe Ponto representa um ponto no plano cartesiano com coordenadas x e y.
- Os métodos especiais __eq__ e __repr__ são implementados para permitir a comparação de igualdade entre pontos e para fornecer uma representação em string adequada do ponto, respectivamente.

## REFERÊNCIAS:

https://stackoverflow.com/questions/29739751/implementing-a-randomly-generated-maze-using-prims-algorithm
https://youtu.be/BT2cjrxGpWo?feature=shared

