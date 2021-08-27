'''
Created on 27 Aug 2021

@author: jenny
'''
from main.notation.pieces import Pieces, get_pieces_type

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
        
        self._setup_chess_pieces()
        
        return 
    
    def _setup_chess_pieces(self):
        
        pieces_handler = []
        pieces_handler.append(get_pieces_type('king'))
        
        self.chess_storage[self.player_id_0] = {}
        self.chess_storage[self.player_id_0]['pieces'] = pieces_handler
         
        return 