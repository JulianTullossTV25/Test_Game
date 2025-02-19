from PyUI.Window import Window
from PyUI.PageElements import Button
from StartScreen import StartScreen
import pygame

# Initialize Pygame
pygame.init()

window = Window("Example App", (0, 255, 0))  # Create the window to work with

# Create Screen Objects for use
startScreen = StartScreen(window)

screen = startScreen  # Set screen to be the starting screen

while True:  # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for element in screen.elements:
                if isinstance(element, Button) and element.wasClicked(event.pos):
                    element.onClick(screen)

    window.checkForInput(screen)  # Checks for inputs on the screen
    screen.display()  # Updates the screen
    window.update(screen)  # Updates the window to reflect the new screen

