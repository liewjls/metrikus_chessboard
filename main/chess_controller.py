'''
Created on 27 Aug 2021

@author: jenny
'''
from main.chess_board import ChessBoard

if __name__ == '__main__':
    print("Hello Chess Controller")
    
    chess_game = ChessBoard()
    
    chess_game.print_pieces_position()
    
    print("Completed Chess Game")