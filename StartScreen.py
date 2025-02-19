from PyUI.Screen import Screen
from PyUI.PageElements import *
from MyElementsBetterThanFowlerLOL import *

class StartScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (255, 182, 193))
        self.state = {
            "displayText": "Happy Valentine's Day!",
            'showHeart': False,
            'heartDrawn': False
        }
        
    def elementsToDisplay(self):
        self.elements = [
            Label((0, 0), 800, 100, self.state['displayText'], 48, (0, 0, 0)),
            SpecialButton()
        ]
        if self.state['showHeart'] and not self.state['heartDrawn']:
            drawHeart(self)
            self.state['heartDrawn'] = True

                  