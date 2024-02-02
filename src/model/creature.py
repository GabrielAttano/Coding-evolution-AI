from src.model.brain import Brain
from enum import Enum

class facingDirection(Enum):
    UP = "Up"
    RIGHT = "Right"
    BOTTOM = "Bottom"
    LEFT = "Left"

class Creature:
    def __init__(self, genomeLength: int, innerNeurons: int, maxAge: int) -> None:
        self.genomeLength = genomeLength
        self.innerNeurons = innerNeurons
        self.genome = list()
        
        self.responsiveness = 1.0
        
        self.brain = Brain()
        self.queuedAction = None

        self.age = 0
        self.maxAge = maxAge

        self.positionX = 0
        self.positionY = 0
        self.facing = facingDirection.UP
        