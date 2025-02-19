import pygame
from PyUI.Screen import Screen
from PyUI.PageElements import *

def drawHeart(self, screen):
    print('drawing heart')
    # Coordinates for the heart shape
    heart_points = [
        (75, 150),  # Bottom left curve
        (100, 120), # Top left curve
        (125, 150), # Top center point
        (150, 120), # Top right curve
        (175, 150), # Bottom right curve
        (125, 200), # Bottom point
    ]
    # Draw the heart shape
    pygame.draw.polygon(self.surface, (255, 0, 0), heart_points)
    screen.state['heartDrawn'] = True


class SpecialButton(Button):
    def __init__(self):
        super().__init__((400, 300), 50, 50, "click me!", 24, (255, 255, 255))

    def onClick(self, screen):
        print("You've clicked a special button")
        screen.state['showHeart'] = not screen.state['showHeart']
        screen.state['heartDrawn'] = False  # Reset the flag when toggling the heart display
        # Reset the screen to the original color
        screen.surface.fill(screen.color)
# Update the screen:
        screen.elementsToDisplay()
        screen.display()

