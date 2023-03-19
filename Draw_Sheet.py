# Simple pygame program

# Import and initialize the pygame library
from Label_and_Track import LabelNotes
import csv
import pygame
import pandas as pd
pygame.init()


# Set up the drawing window
screen = pygame.display.set_mode([9000, 500])

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.set_caption('Pygame')
    # Fill the background with white
    screen.fill((255, 255, 255))
#  -------------------------------------------------------------------------- #
    # Draw treble clef section
    y = 85
    for i in range(5):
        pygame.draw.line(screen, (0, 0, 0),
                         [50, y],
                         [8000, y], 3)
        y += 20
    # Draw bass clef section
    y += 120
    for i in range(5):
        line = pygame.draw.line(screen, (0, 0, 0),
                                [50, y],
                                [8000, y], 3)
        y += 20
#  IMAGE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Import and resize image
    img = pygame.image.load("Quarter_note.png")
    width, height = img.get_size()
    img = pygame.transform.scale(img, (width/28, height / 28))
# Define note locatation --------------------------------
    # Get CSV file
    nlf = pd.read_csv('Note_Length_Frame.csv')
    rect = img.get_rect()
    # Where is the note???
    # Draw the Note
    # Using blit to copy content from one surface to other

    for i in range(0, len(nlf)-1):
        """"""
        row = nlf.iloc[i]
        Note = row['Note']
        Frame = row['Starting_Frame']
    # BASS CLEF NOTES
        if Note == 'G1':
            rect.center = Frame, 358
            screen.blit(img, rect)
        if Note == 'A1':
            rect.center = Frame, 348
            screen.blit(img, rect)
        if Note == 'C2':
            rect.center = Frame, 328
            screen.blit(img, rect)
        if Note == 'D2':
            rect.center = Frame, 318
            screen.blit(img, rect)
        if Note == 'E2':
            rect.center = Frame, 308
            screen.blit(img, rect)
        if Note == 'F2':
            rect.center = Frame, 298
            screen.blit(img, rect)
        if Note == 'G2':
            rect.center = Frame, 288
            screen.blit(img, rect)
        if Note == 'A2':
            rect.center = Frame, 278
            screen.blit(img, rect)
    # TREBLE CLEF NOTES
        if Note == 'C3':
            rect.center = Frame, 158
            screen.blit(img, rect)
        if Note == 'D3':
            rect.center = Frame, 148
            screen.blit(img, rect)
        if Note == 'E3':
            rect.center = Frame, 138
            screen.blit(img, rect)
        if Note == 'F3':
            rect.center = Frame, 128
            screen.blit(img, rect)
        if Note == 'G3':
            rect.center = Frame, 118
            screen.blit(img, rect)
        if Note == 'A3':
            rect.center = Frame, 108
            screen.blit(img, rect)
        if Note == 'B3':
            rect.center = Frame, 98
            screen.blit(img, rect)
        if Note == 'C4':
            rect.center = Frame, 88
            screen.blit(img, rect)
        if Note == 'D4':
            rect.center = Frame, 78
            screen.blit(img, rect)
        if Note == 'E4':
            rect.center = Frame, 68
            screen.blit(img, rect)
        if Note == 'F4':
            rect.center = Frame, 58
            screen.blit(img, rect)
        if Note == 'G4':
            rect.center = Frame, 48
            screen.blit(img, rect)
    # Flip the display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()

# Note = X
# Frame = Y
