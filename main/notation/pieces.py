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
        self.y_position = None 
        self.x_position = None 
        self.icon = None 
        self.name = None 
        
        return 
    
    def set_current_location(self, line, position):
        self.x_position = line
        self.y_position = position
        
        return 
    
    def get_current_position(self):
        
        current_position = "{}{}".format(self.x_position, self.y_position)
        
        return current_position.upper()
    
    def get_pieces_icon(self):
        
        return self.icon
    
    def get_x_position(self):
        return self.x_position
    
    def get_y_position(self):
        return self.y_position
    
    def get_pieces_name(self):
        return self.name 
    
    def set_pieces_icon(self, player_id):
        return 
    
    def set_pieces_name(self, name):
        if name:
            self.name = name 
        else:
            self.name = self.type
        return
    
    def validate_movement(self,current_x, current_y, new_x, new_y, isTaken=False):
        return False
    
    