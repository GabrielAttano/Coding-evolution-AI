from enum import Enum

from src.model.creature import Creature

tolerance = 0.7

class Actions(Enum):
    MOVE_FORWARD_FACING = "move forward facing"
    MOVE_REVERSE_FACING = "move reverse facing"
    MOVE_RIGHT_FACING = "move right facing"
    MOVE_LEFT_FACING = "move left facing"
    MOVE_UP_WORLD = "move up world"
    MOVE_RIGHT_WORLD = "move right world"
    MOVE_DOWN_WORLD = "move down world"
    MOVE_LEFT_WORLD = "move left world"
    MOVE_RANDOM = "move random"

def moveForwardFacing(creature: Creature, input: float):
    value = input * creature.responsiveness
    if abs(value) >= tolerance:
        return Actions.MOVE_FORWARD_FACING

def moveReverseFacing(creature: Creature, input: float):
    value = input * creature.responsiveness
    if abs(value) >= tolerance:
        return Actions.MOVE_REVERSE_FACING

def moveRightLeftFacing(creature: Creature, input: float):
    value = input * creature.responsiveness
    if value >= 0 and value >= tolerance:
        return Actions.MOVE_RIGHT_FACING
    if value < 0 and abs(value) >= tolerance:
        return Actions.MOVE_LEFT_FACING

def moveUpBottomWorld(creature: Creature, input: float):
    value = input * creature.responsiveness
    if value >= 0 and value >= tolerance:
        return Actions.MOVE_UP_WORLD
    if value < 0 and abs(value) >= tolerance:
        return Actions.MOVE_DOWN_WORLD

def moveRightLeftWorld(creature: Creature, input: float):
    value = input * creature.responsiveness
    if value >= 0 and value >= tolerance:
        return Actions.MOVE_RIGHT_WORLD
    if value < 0 and abs(value) >= tolerance:
        return Actions.MOVE_LEFT_WORLD

def moveRandom(creature: Creature, input: float):
    value = input * creature.responsiveness
    if abs(value) >= tolerance:
        return Actions.MOVE_RANDOM

def setResponsiveness(creature: Creature, input: float):
    value = input * creature.responsiveness
    creature.responsiveness = value
