import sys
import random
sys.path.append('..')
from common import board


def pieces_difference(color,the_board):
    player_count = the_board.piece_count[color]      
    opponent_count = the_board.piece_count[the_board.opponent(color)] 
    return 100* ((player_count - opponent_count) / (opponent_count + player_count))

def mobility(color,the_board):
    player_moves= the_board.legal_moves(color)
    opponent_moves= the_board.legal_moves(opponent(color))
    if (player_moves + opponent_moves != 0):
	return 100 * ((player_moves - opponent_moves) / (player_moves + opponent_moves))
	return 0

def heuristic(color,the_board):
    mobility(color,the_board)
    #pieces_difference(color,the_board)


def minimax_ab(color,the_board):
    actual_the_board= the_board
    v_max = max_value(color, float('-inf') , float('inf') , actual_the_board)

    for move in actual_the_board.legal_moves(color):
        actual_the_board.process_move(move, color)
        if heuristic(color,actual_the_board) == v_max:
            return move
    return (-1,-1)
    
def max_value(color, alpha, beta, the_board):    

    for move in the_board.legal_moves(color):
        the_board.process_move(move, color)
        alpha = max(alpha, min_value(the_board.opponent(color), alpha, beta, the_board))
        if beta < alpha:
            return alpha
    return alpha

def min_value(color, alpha, beta, the_board):
    for move in the_board.legal_moves(color):
        the_board.process_move(move, color)
        beta = min(beta,max_value(the_board.opponent(color), alpha, beta, the_board))
        if beta < alpha:
            return beta
    return beta

def make_move(the_board, color):
    """
    Returns a random move from the list of possible ones
    :return: (int, int)
    """
    color = board.Board.WHITE if color == 'white' else board.Board.BLACK
    legal_moves = the_board.legal_moves(color)

    return minimax_ab(color,the_board) if len(legal_moves) > 0 else (-1, -1)

if __name__ == '__main__':
    b = board.from_file(sys.argv[1])
    f = open('move.txt', 'w')
    f.write('%d,%d' % make_move(b, sys.argv[2]))
    f.close()