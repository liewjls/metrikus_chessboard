'''
Created on 27 Aug 2021

@author: jenny
'''
from main.notation.pieces import Pieces

class PRook(Pieces):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        print("[PRook] Constructor")
        self.type = "rook"
        self.location = '1e0'
                
        return 
    
    @classmethod
    def _pieces_type(self):
        return "rook"
    
    