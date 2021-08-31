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
    chess_game.print_pieces_position()
    while(option):
        print_menu()
        choice = input("Enter option:")
        choice = choice.lower().replace(' ', '')
        
        if choice == 'm':
            
            pieces_type = input("Enter piece notation: ")
            pieces_type = pieces_type.replace(' ', '').lower()
            if chess_game.validate_pieces_notation(pieces_type):
                    
                start_square = input("Enter start-square: ")
                end_square = input("Enter end-square: ")
                
                #Remove all empty spaces from the user input
                #Also convert into lowercase too.

                start_square = start_square.replace(' ', '').lower()
                end_square = end_square.replace(' ', '').lower()
                
                if chess_game.update_pieces_notation(pieces_type, start_square, end_square):
                    chess_game.print_pieces_position()
                
            else:
                print("Invalid Option. Ignored.")
            
        elif choice == 'p':
            chess_game.print_pieces_position()
        elif choice == 'e':
            print("exiting now. Bye bye")
            option = False 
        else: 
            print("Invalid choice. Choose again")
            
    print("Completed Chess Game")