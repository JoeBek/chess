import pygame


'''
This class's purpose is to add functionality to each piece in order to make
moving them around the board very simple. This is 

'''
class Piece:
    def __init__(self, type, color, x, y):
        """
        Initialize a chess piece.

        :param color: String, either 'white' or 'black' indicating the piece's color.
        :param position: Tuple (x, y) representing the piece's position on the board.
        :param x: int representing x coordinate
        :param y: int representing y coordinate 
        """
        self.color = color
        self.type = type
        self.x = x
        self.y = y
        self.is_captured = False
        self.selected = False

    def move(self, x, y):
        """
        Move the piece to a new position.

        :param new_position: Tuple (x, y) representing the new position.
        """
        self.x = x
        self.y = y

    def capture(self):
        """
        Mark this piece as captured.
        """
        self.is_captured = True

    def get_type(self):
        return self.type


    # boundary checking will happen in board class

    def legal_move(self, x, y):
        pass


    def legal_move_pawn(self, x, y, can_take):

        if (self.y + 1 == y):
            return True
        
        if (not can_take):
            return False
        
        if ()
        

    def legal_move_bishop(self, x , y):

        if (self.type != 'bishop'):
            return False
        
        return (x - self.x == y - self.y)
    

    def legal_move_knight(self, x, y):
        

        #one legal move
        one = abs(x - self.x) == 1 and abs(y - self.y) == 2

        #other legal move
        two = abs(x - self.x) == 2 and abs()
        return ()
    

    #rff
    def legal_move_rook(self, x, y):
        
        if (self.type != 'rook'):
            return False
        
        
        return (x - self.x == 0 or y - self.y == 0)
    
    
    # From here down, I'm implementing movement by piece, by direction. 
    # Each piece gets an overarching function, 
    # with arguments for different directions (west, northwest, etc).
    # 
    

    def move_pawn(self, directions):
        """
        :param directions: tuple of directions that are relevant to each piece. :
        """

    def move_bishop(self, directions):
        """
        :param directions: tuple of directions that are relevant to each piece. :
        """
    
    def move_knight(self, directions):
        """
        :param directions: tuple of directions that are relevant to each piece. :
        """

    def move_rook(self, directions):
        """
        :param directions: tuple of directions that are relevant to each piece. :
        """

    def move_queen(self, directions):
        """
        :param directions: tuple of directions that are relevant to each piece. :
        """















    # move to board. Blocking has to check on board level. 

    # 
    def blocking_check_bishop(self, x, y):

        for i in range(abs(self.x - x)):

            pass




    



        


    # You might want to add more methods here depending on your game logic,
    # such as methods to get a list of valid moves for this piece, etc.
