'''
Created on 27 Aug 2021

@author: jenny
'''
from main.notation.pieces import Pieces

class PKing(Pieces):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        self.type = "king"
        
        return 
    
    @classmethod
    def _pieces_type(self):
        return "king"
    
    def set_pieces_icon(self, player_id):
        self.icon = '♔' if player_id == 1 else '♚'
        return 