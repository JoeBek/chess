import pygame

class Board:
    def __init__(self):
        # Initialize the board
        self.board = self.create_board()
        self.boardSizeX = 8
        self.boardSizeY = 8


        # Load images for pieces or any other graphical assets




    def create_board(self):
        # Create an 8x8 grid representation of the board
        # This could be a 2D list (array) where each element represents a square on the board

        n = self.boardSizeX
        m = self.boardSizeY
        

        return [[None for _ in range(n)] for _ in range(m)]
        
        

    def draw(self, screen):
        # Draw the board and pieces on the screen
        # This function will be called in the main game loop
        pass

    def update(self):
        # Update the board state (if needed)
        # This could include updating piece positions, checking for check/checkmate, etc.
        pass

    # Additional methods as needed for handling game logic, piece





    def check_selected(self):

        # might have to move to main method 
        """
        checks for if the piece has been clicked. If it has, returns true.
        """

        pass


    def generate_movement_vectors(self, piece):

        type 

        
        
        if piece.get_type().equals('Bishop'):
            gen_bishop_vectors(self)
        





        



