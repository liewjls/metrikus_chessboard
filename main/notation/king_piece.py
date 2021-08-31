'''
Created on 27 Aug 2021

@author: jenny
'''
from .pieces import Pieces
from notation_constant import DEFAULT_PLAYER_ID

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
        self.icon = '♔' if player_id == DEFAULT_PLAYER_ID else '♚'
        return 
    
    def validate_movement(self,current_x, current_y, new_x, new_y, isTaken=False):
        
        return abs(current_x-new_x) == 1 and abs(current_y-new_y) == 1 
        