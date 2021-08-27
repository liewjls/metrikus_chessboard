'''
Created on 27 Aug 2021

@author: jenny
'''

def get_pieces_type(pieces_name):
    
    pieces_handler = None 
    
    for cls in Pieces.__subclasses__():
        if cls._pieces_type() == pieces_name:
            pieces_handler = cls()
            break
    
    return pieces_handler 

class Pieces(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.type = None 
        self.location = None 
        self.line = None 
        
        return 
    
    def set_current_location(self, line, position):
        self.line = line
        self.location = position
        
        return 
    
    def get_current_position(self):
        
        current_position = "{}x{}".format(self.line, self.location)
        
        return current_position
    
    
    
    
    
    