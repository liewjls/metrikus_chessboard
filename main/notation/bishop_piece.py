'''
Created on 27 Aug 2021

@author: jenny
'''
from main.notation.pieces import Pieces

class PBishop(Pieces):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        print("[PBishop] Constructor")
        self.type = "bishop"
                
        return 
    
    @classmethod
    def _pieces_type(self):
        return "bishop"
    
    