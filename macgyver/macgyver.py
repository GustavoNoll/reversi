import sys
import random
sys.path.append('..')
from common import board
from pathlib import Path
from copy import deepcopy

ply_alpha=4
def mobility(color,the_board):
    return_score=0
    player_moves= len(the_board.legal_moves(color))
    opponent_moves= len(the_board.legal_moves(the_board.opponent(color)))
    if (player_moves + opponent_moves != 0):
	    return_score=100 * (player_moves - opponent_moves) / (player_moves + opponent_moves)
    return return_score


def heuristic(color,the_board):
    return mobility(color,the_board)


def minimax_ab(color,the_board,ply):
    moves=the_board.legal_moves(color)
    bestscore  = float('-inf')
    return_move=moves[0]
    for move in moves:
        newboard= deepcopy(the_board)
        newboard.process_move(move, color)
        score=min_value(newboard.opponent(color),float('-inf'),float('inf'),newboard,ply-1)
        if score>bestscore:
            bestscore=score
            return_move=move
    return return_move
    
def max_value(color, alpha, beta, the_board,ply):    
    if len(the_board.legal_moves(color))==0 or ply==0:
        return heuristic(color,the_board)
    bestscore = float('-inf')
    for move in the_board.legal_moves(color):
        newboard= deepcopy(the_board)
        newboard.process_move(move, color)
        score = min_value(newboard.opponent(color), alpha, beta, newboard,ply-1)
        if score > bestscore:
            bestscore=score
        if bestscore>=beta:
            return bestscore
        alpha=max(alpha,bestscore)
    return bestscore

<<<<<<< HEAD
=======
def pieces_difference(color,the_board):
    player_count = the_board.piece_count[color]      
    opponent_count = the_board.piece_count[the_board.opponent(color)]
    return 100* (player_count - opponent_count) / (opponent_count + player_count)

def mobility(color,the_board):
    return_score=0
    player_moves= the_board.legal_moves(color)
    opponent_moves= the_board.legal_moves(the_board.opponent(color))
    if (player_moves + opponent_moves != 0):
	    return_score=100 * (player_moves - opponent_moves) / (player_moves + opponent_moves)
	return return_score


def heuristic(color,the_board):
    mobility(color,the_board)
    #pieces_difference(color,the_board)


def minimax_ab(color,the_board,ply=4):
    moves=the_board.legal_moves(color)
    bestscore  = float('-inf')
    return_move=moves[0]
    for move in moves:
        newboard= deepcopy(the_board)
        newboard.process_move(move, color)
        score=min_value(newboard.opponent(color),float('-inf'),float('inf'),newboard,ply-1)
        if score>bestscore:
            bestscore=score
            return_move=move
    return return_move
    
def max_value(color, alpha, beta, the_board,ply):    
    if len(the_board.legal_moves(color))==0 or ply==0:
        return heuristic(color,the_board)
    bestscore = float('-inf')
    for move in the_board.legal_moves(color):
        newboard= deepcopy(the_board)
        newboard.process_move(move, color)
        score = min_value(newboard.opponent(color), alpha, beta, newboard,ply-1)
        if score > bestscore:
            bestscore=score
        if bestscore>=beta:
            return bestscore
        alpha=max(alpha,bestscore)
    return bestscore

>>>>>>> 3b197f8c8bb13015dabacd3cd8e01ca40e1390a5
def min_value(color, alpha, beta, the_board,ply):
    if len(the_board.legal_moves(color))==0 or ply==0:
        return heuristic(color,the_board)
       
    bestscore = float('inf')
    for move in the_board.legal_moves(color):
        newboard= deepcopy(the_board)
        newboard.process_move(move, color)
        score = max_value(newboard.opponent(color), alpha, beta, newboard,ply-1)
        if score < bestscore:
            bestscore=score
        if bestscore<=beta:
            return bestscore
        beta=min(beta,bestscore)
    return bestscore

def make_move(the_board, color):
    """
    Returns a random move from the list of possible ones
    :return: (int, int)
    """
    color = board.Board.WHITE if color == 'white' else board.Board.BLACK
    legal_moves = the_board.legal_moves(color)

<<<<<<< HEAD
    return minimax_ab(color,the_board,ply_alpha) if len(legal_moves) > 0 else (-1, -1)


b = board.from_file("state.txt")
b.print_board()
f = open('move.txt', 'w')
f.write('%d,%d' % make_move(b, 'white'))
f.close()
=======
    return minimax_ab(color,the_board) if len(legal_moves) > 0 else (-1, -1)

if __name__ == '__main__':
    b = board.from_file(sys.argv[1])
    f = open('move.txt', 'w')
    f.write('%d,%d' % make_move(b, sys.argv[2]))
    f.close()
>>>>>>> 3b197f8c8bb13015dabacd3cd8e01ca40e1390a5
