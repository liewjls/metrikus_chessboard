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
                'location' : ['e']
            },
            {
                'name' : 'queen', 
                'location': ['d']
            },
            {
                'name' : 'rook', 
                'location': ['a', 'h']
            },
            {
                'name' : 'knight', 
                'location': ['b', 'g']
            },
            {
                'name' : 'bishop', 
                'location': ['c', 'f']
            },
            {
                'name' : 'pawn', 
                'location': ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'h']
            }
        ]
        
        self._setup_chess_pieces()
        
        return 
    
    def _setup_chess_pieces(self):
        
        pieces_handler = []
        for i in self.pieces_notation:
            pieces_handler.append(get_pieces_type(i['name']))
        
        self.chess_storage[self.player_id_0] = {}
        self.chess_storage[self.player_id_0]['pieces'] = pieces_handler
         
        return 