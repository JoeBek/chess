"""

This file handles the logic for the 2 players. The two player objects will function parallel
to the board, carrying things like points, wins and statuses such as checked or move priority.

"""



import pygame


def __init__(self, color):

    self.color = color
    self.points = 0  # points start at zero
    self.wins = 0  # wins start at zero
    
    self.toMove = False # flag for if it's your turn to move
    self.checked = False # flag for if you're in check






