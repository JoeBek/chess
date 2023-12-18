# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


"""
image path storage
"""
pawn_path = "C:\\Users\\joe\\PersonalProjects\\chess\\sprites\\pieces\\arcade_style_chess_pawn_transparent_background.png"

knight_path = "C:\\Users\\joe\\PersonalProjects\\chess\\sprites\\pieces\\arcade_style_chess_knight_transparent_background.png"

bishop_path = "C:\\Users\\joe\\PersonalProjects\\chess\\sprites\\pieces\\arcade_style_chess_bishop_transparent_background.png"

rook_path = "C:\\Users\\joe\\PersonalProjects\\chess\\sprites\\pieces\\arcade_style_chess_rook_transparent_background.png"

queen_path = "C:\\Users\\joe\\PersonalProjects\\chess\\sprites\\pieces\\transparent_arcade_style_chess_queen.png"

king_path = "C:\\Users\\joe\\PersonalProjects\\chess\\sprites\\pieces\\arcade_style_chess_king_transparent_background.png"




"""
end image path storage
"""

piece_images = {"Pawn": pawn_path, "Knight": knight_path, "Bishop": bishop_path, "Rook": rook_path,
                "King": king_path, "Queen": queen_path}




image = pygame.image.load("C:\\Users\\joe\\PersonalProjects\\chess\\sprites\\otherboard2.png")  # Replace with your image path

smaller_image = pygame.transform.scale(image, (700, 700))  # Set the desired size


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    screen.blit(smaller_image, (300, 10))

    # RENDER YOUR GAME HERE
    
    




    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


# resolve this garbage

def draw_pieces(screen, piece_positions):
    for position, piece in piece_positions.items():
        x, y = position
        screen.blit(piece_images[piece.get_type()], (x*100, y*100))