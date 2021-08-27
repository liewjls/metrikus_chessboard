'''
Created on 27 Aug 2021

@author: jenny
'''
from main.notation.pieces import Pieces

class PKnight(Pieces):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        print("[PKnight] Constructor")
        self.type = "knight"
                
        return 
    
    @classmethod
    def _pieces_type(self):
        return "knight"
    
    