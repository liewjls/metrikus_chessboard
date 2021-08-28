'''
Created on 27 Aug 2021

@author: jenny
'''
from chess_board import ChessBoard

def print_menu():
    print("m. Move pieces")
    print("p. Print current board")
    print("e. Exit")
    
    return 

if __name__ == '__main__':
    print("Hello Chess Controller")
    
    chess_game = ChessBoard()
    option = True 
    
    while(option):
        print_menu()
        choice = input("Enter option:")
        
        if choice == 'm':
            print("Enter piece notation, start-square, end-square. eg: pawn d2 d4")
            pieces_type = "pawn"
            start_square = "d2"
            end_square='d4'
            chess_game.update_pieces_notation(pieces_type, start_square, end_square)
            
            chess_game.print_pieces_position()
            
        elif choice == 'p':
            chess_game.print_pieces_position()
        elif choice == 'e':
            print("exiting now. Bye bye")
            option = False 
        else: 
            print("Invalid choice. Choose again")
            
    print("Completed Chess Game")