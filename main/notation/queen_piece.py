'''
Created on 27 Aug 2021

@author: jenny
'''
from .pieces import Pieces

class PQueen(Pieces):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        self.type = "queen"
               
        return 
    
    @classmethod
    def _pieces_type(self):
        return "queen"
    
    def set_pieces_icon(self, player_id):
        self.icon = '♕' if player_id == 1 else '♛'
        return     