'''
Created on 27 Aug 2021

@author: jenny
'''
from .pieces import Pieces
from notation_constant import DEFAULT_PLAYER_ID

class PPawn(Pieces):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        self.type = "pawn"
        self.moved = False
         
        return 
    
    @classmethod
    def _pieces_type(self):
        return "pawn"
    
    
    def set_pieces_icon(self, player_id):
        self.icon = '♙' if player_id == DEFAULT_PLAYER_ID else '♟'
        return
        
    def validate_movement(self,current_x, current_y, new_x, new_y, isTaken=False):
        
        isAllow = False 
        diff_x = abs(current_x - new_x)
        diff_y = abs(current_y - new_y)

        if not self.moved: 
            #Means initial movement, allow 2 
            isAllow = ( (diff_x == 2 or diff_x ==1) and diff_y == 0) or \
                       (diff_x == 0 and (diff_y == 1 or diff_y == 2))
                       
            if isAllow:
                self.moved = True 
                
        elif isTaken:
            isAllow = (diff_x == 1 and diff_y == 1) or \
                        (diff_x == 1 and diff_y == 0) or \
                        (diff_x == 0 and diff_y == 1)
                        
        else:
            isAllow = ( diff_x ==1 and diff_y == 0) or \
                       (diff_x == 0 and diff_y == 1 )
            
        return isAllow
    
    