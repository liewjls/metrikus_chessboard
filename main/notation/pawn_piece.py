'''
Created on 27 Aug 2021

@author: jenny
'''
from main.notation.pieces import Pieces

class PPawn(Pieces):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        print("[PPawn] Constructor")
        self.type = "pawn"
         
        return 
    
    @classmethod
    def _pieces_type(self):
        return "pawn"
    
    