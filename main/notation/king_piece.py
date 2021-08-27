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
        
        print("[PKing] Constructor")
        self.type = "KING"
        self.location = '1e0'
                
        return 
    
    def _pieces_type(self):
        return "king"
    
    