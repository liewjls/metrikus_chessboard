'''
Created on 27 Aug 2021

@author: jenny
'''
from main.notation.pieces import get_pieces_type

class ChessBoard(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print("[Pieces Storage] Constructor")
        
        #Player ID
        self.player_id_0 = 0
        self.player_id_1 = 1
        
        self.chess_storage = {}
        self.pieces_notation = [
            {
                'name' : 'king', 
                'location' : ['e'],
                'line' : 0
            },
            {
                'name' : 'queen', 
                'location': ['d'],
                'line' : 0
            },
            {
                'name' : 'rook', 
                'location': ['a', 'h'],
                'line' : 0
            },
            {
                'name' : 'knight', 
                'location': ['b', 'g'],
                'line' : 0
            },
            {
                'name' : 'bishop', 
                'location': ['c', 'f'],
                'line' : 0
            },
            {
                'name' : 'pawn', 
                'location': ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'h'],
                'line' : 1
            }
        ]
        
        print("[ChessBoard] Setting up Player 1 pieces default position:")
        self._setup_chess_pieces(self.player_id_0)

        print("[ChessBoard] Setting up Player 2 pieces default position:")
        self._setup_chess_pieces(self.player_id_1)
        
        return 
    
    def _setup_chess_pieces(self, player_id):
        
        pieces_handler = []
        for i in self.pieces_notation:
            
            p_name = i['name']
            p_location_list = i['location']
            position_buffer = 0 
            
            if player_id == 1:
                position_buffer = 5 if p_name == 'pawn' else 7
                
            p_line_position = i['line'] + position_buffer
            
            for pl in p_location_list:
                current_pieces_obj = get_pieces_type(p_name)
                current_pieces_obj.set_current_location(p_line_position, pl)
                
                pieces_handler.append(current_pieces_obj)
        
        self.chess_storage[self.player_id_0] = {}
        self.chess_storage[self.player_id_0]['pieces'] = pieces_handler
        
        print("Total pieces_handler size:{}".format(len(pieces_handler))) 
        
        return 
    
    