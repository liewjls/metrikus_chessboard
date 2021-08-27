'''
Created on 27 Aug 2021

@author: jenny
'''
from main.notation.pieces import Pieces

class PQueen(Pieces):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        print("[PQueen] Constructor")
        self.type = "queen"
        self.location = '1e0'
                
        return 
    
    @classmethod
    def _pieces_type(self):
        return "queen"
    
    