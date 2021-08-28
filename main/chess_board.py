'''
Created on 27 Aug 2021

@author: jenny
'''

from main.notation.pieces import get_pieces_type

class ChessBoard(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        #Player ID
        self.player_id_0 = 0
        self.player_id_1 = 1
        
        self.chess_storage = {}
        self.pieces_notation = [
            {
                'name' : 'king', 
                'location' : [4],
                'line' : 0
            },
            {
                'name' : 'queen', 
                'location': [3],
                'line' : 0
            },
            {
                'name' : 'rook', 
                'location': [0, 7],
                'line' : 0
            },
            {
                'name' : 'knight', 
                'location': [1, 6],
                'line' : 0
            },
            {
                'name' : 'bishop', 
                'location': [2, 5],
                'line' : 0
            },
            {
                'name' : 'pawn', 
                'location': [0, 1, 2, 3, 4, 5, 6, 7],
                'line' : 1
            }
        ]
        
        #Setting up the buffer for the chessboard (8x8)
        n = 8
        self.chess_storage['current_mapping'] = [[None] * n for i in range(n)]
        self.chess_storage['pieces'] = {}        
        
        print("[ChessBoard] Setting up Player 1 pieces default position:")
        self._setup_chess_pieces(self.player_id_0)

        print("[ChessBoard] Setting up Player 2 pieces default position:")
        self._setup_chess_pieces(self.player_id_1)
        
        return 
    
    def _setup_chess_pieces(self, player_id):
        
        pieces_handler = []
        temp_pieces_list = []

        
        for i in self.pieces_notation:
            
            p_name = i['name']
            p_location_list = i['location']
            position_buffer = 0 
            
            if player_id == 1:
                position_buffer = 5 if p_name == 'pawn' else 7
                
            p_line_position = i['line'] + position_buffer
            total_piece = len(p_location_list)
            count_piece = 0 if total_piece  > 1 else None
            pieces_name = None 
            
            for pl in p_location_list:
                current_pieces_obj = get_pieces_type(p_name)
                current_pieces_obj.set_current_location(p_line_position, pl)
                current_pieces_obj.set_pieces_icon(player_id)
                
                if isinstance(count_piece, int):
                    pieces_name = "{}_{}_{}".format(p_name, count_piece, player_id)
                    count_piece += 1
                else:
                    pieces_name = "{}_{}".format(p_name, player_id)
                    
                current_pieces_obj.set_pieces_name(pieces_name)
                
                pieces_handler.append([pieces_name, current_pieces_obj])
                x_pos = current_pieces_obj.get_x_position()
                y_pos = current_pieces_obj.get_y_position()
                
                temp_pieces_list.append([player_id, 
                                        pieces_name,
                                        current_pieces_obj.get_x_position(),
                                        current_pieces_obj.get_y_position(), 
                                        current_pieces_obj.get_pieces_icon()])
                
                self.chess_storage['current_mapping'][x_pos][y_pos] = pieces_name
                
            # temp_pieces_list.sort(key=lambda x:(x[2], x[3]))    
            # for i in temp_pieces_list:
            #     print("Player {} {}\t  {} {} {}".format(i[0], 
            #                                          i[1], 
            #                                          i[2], #x
            #                                          i[3], #y
            #                                          i[4]))
        
        self.chess_storage['pieces'][player_id] = pieces_handler
                
        return 
    
    def print_pieces_position(self):
        
        player_pieces = self.chess_storage['pieces']
        current_map = self.chess_storage['current_mapping']
        
        map_str = ""
        for i in current_map:
            
            for item in i:
                if item:
                    #Get the pieces icon 
                    for pieces_obj in player_pieces:
                        myItem = player_pieces[pieces_obj]
                        
                        for icon_list in myItem:
                            if icon_list[0] == item:
                                icon = icon_list[1].get_pieces_icon()
                                map_str += "|{}".format(icon) 
                                break 
                else:
                    map_str += "| "   
                
            map_str += "|\n"
            
        print("Current Position:\n\n{}".format(map_str))
        print("================================")

        return 

      
        
        
    