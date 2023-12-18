import pygame
import numpy as np 
import pandas as pd 




class Board:
    def __init__(self, rows=8, cols=8):
        # Initialize the board
        self.board = self.create_board()
        self.xMax = 8
        self.yMax = 8
        self.xMin = 0
        self.yMin = 0

        # log is a tuple with every x and y pair that holds information about the board
        # whether squares have pieces, are checked, yada yada.

        # need to initialize this systematically so I can mess with dimensions. 
        
        self.log = {(x, y): {'checked': False} for x in range(rows) for y in range(cols)}


        # Load images for pieces or any other graphical assets




    def capture(self, pos):
        
        piece = self.log[pos]
        
        
        self.log[pos] = None 
        
        
        return piece
        

    def create_board(self):
        # Create an 8x8 grid representation of the board
        # This could be a 2D list (array) where each element represents a square on the board

        self.board = {(x, y): {'piece': None} for x in range(self.rows) for y in range(self.cols)}
        
        

        
        
        

    def draw(self, screen):
        # Draw the board and pieces on the screen
        # This function will be called in the main game loop
        pass

    def update(self):
        # Update the board state (if needed)
        # This could include updating piece positions, checking for check/checkmate, etc.

        """
         this function gets called after a piece moves. It will check for statemate, check, checkmate
         and then update player priority. I may return a tuple of flags that will go to the player. This
         will keep the design flexible. But might make it a little less intuitive. I will have to
         document well. Here I go.

        """




        pass
        
    # Additional methods as needed for handling game logic, piece





    def check_selected(self):

        # might have to move to main method 
        """
        checks for if the piece has been clicked. If it has, returns true.
        """

        pass


    def generate_movement_vectors(self, piece):

        squares_to_check = []
        

        
        
        if piece.get_type().equals('Bishop'):
            gen_bishop_vectors(piece)
        


    # from here down is the current implementation for move checking. I'll add checks for
    # each individual piece that 
            
    def piece_can_move_here(self, pos, piece):

        
        # check if piece is trying to escape the board 

        if not (self.xMin > pos[0] > self.xMax - 1 or self.yMin > pos[1] > self.yMax - 1):
            return False
        
        
        
        # if there is not a piece in the way. Do this by accessing the log attribute using pos as the key.
        
        
        
        if (self.board[pos] is not None):
            
            # return true if the piece is anything but a pawn (it will take)
            
            return not piece.get_type() == 'Pawn'
                
            
            
            
            
            
        
        




        
    def gen_bishop_vectors(self, piece):

        impeded = False  # if the vector hits a wall or another piece

        squares_to_check = []
        directions = ['nw', 'ne', 'sw', 'se']
        
        for dir in directions:

            x = piece.x # x component. Resets each direction
            y = piece.y # y component. Resets each direction


            # mutliply the truth of each direction with 1 to get the unit movement vector
            dx = int(dir == 'n') * 1 - int(dir == 's') * -1
            dy = int(dir == 'e') * 1 - int(dir == 'w') * -1



            
            if not self.piece_can_move_here((x+dx, y+dy), piece):

                impeded = True


            while not impeded:
                
                
        
                # Apply the unit movement vector to get the new position
                x += dx
                y += dy
                
                

                # Check if the new position is valid and not impded
                if not self.piece_can_move_here((x, y), piece):
                    impeded = True
                    break
                    
                if self.board[(x,y)] is not None:
                    impeded = True
                
                self.log[(x,y)] = True
                
                
                
    """
    So it begins. Implemenation of the other vectors. I'm probably gonna try and write all of these 
    before I start testing the backend. we'll see. 
    
    """
    def get_pawn_vectors(self, piece):
        """
        This function yada yada
        """
        
        # we need to grab only the square right above. Note that the pawn is annoying because it is the
        # 1. Asymmetrical, 2. can't take pieces in movement path, 3. turns into other pieces sometimes
        
        # so we will start by checking the piece position and establishing asymmetry
        
        pos = piece.pos
        dir = -1 if piece.get_color() == "Black" else 1
        
        # from here
        
        
        pass
    
    
    def get_knight_vectors(self, piece):
        
        pass
    
    def get_rook_vectors(self, piece):
        
        pass
    
    def get_queen_vectors(self,piece):
        
        pass
    
    def get_king_vectors(self, piece):
        
        pass
                


                
   

           
        
        






        



