'''
Created on 27 Aug 2021

@author: jenny
'''
from notation.pieces import get_pieces_type


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
        
        self.current_player = 0
        
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
        
        self._setup_chess_pieces(self.player_id_0)
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
        count = 1
        map_str = " | a | b | c | d | e | f | g | h |\n"
        for i in current_map:
            map_str +="{}".format(count)
            for item in i:
                if item:
                    #Get the pieces icon 
                    for pieces_obj in player_pieces:
                       
                        for icon_list in player_pieces[pieces_obj]:
                            if icon_list[0] == item:
                                icon = icon_list[1].get_pieces_icon()
                                map_str += "| {} ".format(icon) 
                                break 
                else:
                    map_str += "|   "   
                
            map_str += "|\n"
            count +=1
            
        print("-> Current Position:\n\n{}".format(map_str))
        print("================================")

        return 
    
    def update_pieces_notation(self, pieces_type, start_square, end_square):
        
        found = False 
        
        try:
            #TODO: Need to validate the string must only 2 digit.
            start_y = int(ord(start_square[0]) - 97)
            start_x = int(start_square[1]) - 1 
            
            end_y = int(ord(end_square[0]) - 97)
            end_x = int(end_square[1]) -1 
            
            
            #Get the current mapping of the pieces 
            current_map = self.chess_storage['current_mapping']
            
            my_pieces_name = current_map[start_x][start_y]
            
            if my_pieces_name:
                #Check the player id:
                current_pieces_info_list = my_pieces_name.split('_')
                current_pieces_name = current_pieces_info_list[0]
                player_id = int(current_pieces_info_list[-1])            
                if player_id != self.current_player:
                    print("-> It is player {} turn. Not allow Player {}.".format(self.current_player, 
                                                                              player_id))
                    return False            
            
            is_taken = self.isTaken(end_x, end_y, my_pieces_name)
            
            if my_pieces_name and self.validateMove(end_x, end_y, start_x, start_y, 
                                                    my_pieces_name, is_taken):

                if current_pieces_name != pieces_type:
                    print("->Invalid option. current pieces:{} requested pieces:{}".format(current_pieces_name, 
                                                                                         pieces_type))
                    return False 
                

                print("-> Attempting to moving {}".format(my_pieces_name))
                
                current_map[start_x][start_y] = None 
                current_map[end_x][end_y] = my_pieces_name
                
                player_pieces = self.chess_storage['pieces']
                
                for player_id in player_pieces:    
                    
                    for pieces_obj in player_pieces[player_id]:
                        
                        if pieces_obj[0] == my_pieces_name:
                            
                            pieces_obj[1].set_current_location(end_x, end_y)
                            found = True
                            break
                    
                    if found:
                        # The move seems valid. Update next player turn status
                        self.current_player = 1 if self.current_player == 0 else 0
                        break
            else:
                print("-> Error: Invalid pieces..")
        
        except Exception as e:
            print("-> Exception caught. {}".format(e))
        
        return found
    
    def validateMove(self, new_x, new_y, current_x, current_y, pieces_name, isTaken):
        
        isAllow = False 
        
        #Checking and validate the move 
        player_pieces = self.chess_storage['pieces']
        print("-> Validation: piece:{}".format(pieces_name))
        for player_id in player_pieces:
            
            for pieces_obj in player_pieces[player_id]:
                
                if pieces_obj[0] == pieces_name:
                    print("-> Validating:{} isTaken:{}".format(pieces_name, isTaken))
                    isAllow = pieces_obj[1].validate_movement(current_x, current_y, new_x, new_y, isTaken)
                    
        return isAllow

    def isTaken(self, current_x, current_y, new_pieces):
        
        isTaken = False 
        
        try:
            pieces_name = self.chess_storage['current_mapping'][current_x][current_y]
            
            if pieces_name:
                #TODO: possible to check whether it can be taken? 
                current_pieces_list = pieces_name.split('_')
                current_pieces_player_id = int(current_pieces_list[-1])
            
                if current_pieces_player_id == self.current_player:
                    print("-> Error: Not allow take own pieces: ")
                    isTaken = False 
                    pieces_name = None
                    raise Exception("Invalid Option")
                
                print("-> Current pieces:{} over taking {}".format(pieces_name, new_pieces))
            
            if pieces_name:
                print("taking out the pieces {}".format(pieces_name))
                player_pieces = self.chess_storage['pieces']
                
                for player_id in player_pieces:
                    
                    for pieces_obj in player_pieces[player_id]:
                        
                        if pieces_obj[0] == pieces_name:
                            print("-> To be delete - Found Pieces:{}".format(pieces_name))
                            player_pieces[player_id].remove(pieces_obj)
                            self.chess_storage['current_mapping'][current_x][current_y] = None 
                            
                            isTaken = True
                            
                            break
                    
            
        except Exception as e:
            print("Error:{}".format(e))
            raise e 
            
        return isTaken
    
    def validate_pieces_notation(self, name):
        
        isValid = False 
        for item in self.pieces_notation:
            if name in item.values():
                isValid = True 
                break
            else:
                isValid = False
        
        return isValid
        
        
    