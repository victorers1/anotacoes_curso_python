#Jogo da velha
import numpy as np
import time
import matplotlib.pyplot as plt

def create_board():  # Cria o tabuleiro do jogo da velha
    return np.zeros((3,3))


def place(board, player, position):
    '''
    :param board: tabuleiro a ser modificado
    :param player: inteiro 1 ou 2 indicando o jogador
    :param position: posição do tabuleiro
    :return: nada
    '''
    if board[position] == 0:
        board[position] = player
    else:
        pass


def possibilities(board):
    lista = np.where(board == 0)
    x = lista[0]
    y = lista[1]

    lista_temp = []

    for i in range(len(x)):
        lista_temp.append((x[i],y[i]))
    return lista_temp


def random_place(board, player):
    poss = possibilities(board)
    ind = np.random.choice(len(poss))
    b = board.copy()
    b[poss[ind]] = player  # Seleciona uma posição possível aleatória e preenche com a jogada
    return b


def row_win(board, player):
    nLin = board.shape[0]
    for i in range(nLin):
        if np.all(board[i,:] == player):  # Assim que achar uma linha completa por 'player', retorna 'True'
            return True
    return False


def col_win(board, player):
    nLin = board.shape[0]
    for i in range(nLin):
        if np.all(board[:,i] == player):  # Assim que achar uma linha completa por 'player', retorna 'True'
            return True
    return False


def diag_win(board, player):
    nLin = board.shape[0]
    nCol = board.shape[1]
    princ = []
    secun = []
    for i in range(nLin):
        for j in range(nCol):
            if i == j:
                princ.append(board[i, j])
            elif i+j == 3:
                secun.append(board[i, j])

    if np.all(princ == player):
        return True
    elif np.all(secun == player):
        return True

    return False


def evaluate(board):
    '''
    :param board: tabuleiro
    :return: -1 em caso de empate, 0 se o jogo ainda está em andamento, ou, o número do jogador que ganhou
    '''
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def play_game():
    board = create_board()
    player = 2  # Deve iniciar com o segundo jogador pois a primeira linha do WHILE sempre inverte o valor
    while len(possibilities(board)) > 0:
        player = 1 if player == 2 else 2  # Altera entre os jogadores 1 e 2
        board = random_place(board, player)

        avalia = evaluate(board)
        if avalia != 0:
            return avalia

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            board = random_place(board, player)
            winner = evaluate(board)
          # use `evaluate(board)`, and store as `winner`.
            if winner != 0:
                break
    return winner

print(play_strategic_game())


'''
contador = []
start = time.time()
for i in range(1000):
    ggwp = play_game()
    if ggwp == 1:
        contador.append(1)
    elif ggwp == 2:
        contador.append(2)
stop = time.time()

tempo_decorrido = stop - start
print(tempo_decorrido)

plt.hist(contador)
plt.show()
'''

contador = []
start = time.time()
for i in range(1000):
    ggwp = play_strategic_game()
    if ggwp == 1:
        contador.append(1)
    elif ggwp == 2:
        contador.append(2)
stop = time.time()

tempo_decorrido = stop - start
print(tempo_decorrido)

plt.hist(contador)
plt.show()