from src.model.creature import Creature, facingDirection
from src.model.world import World, CellData

from src.service.functions.actionNeuronFunctions import Actions

import random

def doAction(world: World, creature: Creature, action: Actions):
    # move Facing directions
    if action.value == Actions.MOVE_FORWARD_FACING.value:
        moveForwardFacing(world, creature)
        return
    
    if action.value == Actions.MOVE_FORWARD_FACING.value:
        moveReverseFacing(world, creature)
        return
    
    if action.value == Actions.MOVE_RIGHT_FACING.value:
        moveRightFacing(world, creature)

    if action.value == Actions.MOVE_LEFT_FACING.value:
        moveLeftFacing(world, creature)

    # move world position
    if action.value == Actions.MOVE_UP_WORLD.value:
        moveUpWorld(world, creature)
        return
    
    if action.value == Actions.MOVE_DOWN_WORLD.value:
        moveDownWorld(world, creature)
        return
    
    if action.value == Actions.MOVE_RIGHT_WORLD.value:
        moveRightWorld(world, creature)

    if action.value == Actions.MOVE_LEFT_WORLD.value:
        moveLeftWorld(world, creature)

    if action.value == Actions.MOVE_RANDOM.value:
        moveRandom(world, creature)

def moveRandom(world: World, creature: Creature):
    randomDirection = random.randint(0, 3)
    if randomDirection == 0:
        moveUpWorld(world, creature)
    if randomDirection == 1:
        moveRightWorld(world, creature)
    if randomDirection == 2:
        moveDownWorld(world, creature)
    if randomDirection == 3:
        moveLeftWorld(world, creature)

def moveLeftFacing(world: World, creature: Creature):
    if creature.facing.value == facingDirection.RIGHT.value:
        moveUpWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.BOTTOM.value:
        moveRightWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.UP.value:
        moveLeftWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.LEFT.value:
        moveDownWorld(world, creature)
        return

def moveRightFacing(world: World, creature: Creature):
    if creature.facing.value == facingDirection.LEFT.value:
        moveUpWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.UP.value:
        moveRightWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.BOTTOM.value:
        moveLeftWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.RIGHT.value:
        moveDownWorld(world, creature)
        return

def moveForwardFacing(world: World, creature: Creature):
    if creature.facing.value == facingDirection.UP.value:
        moveUpWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.RIGHT.value:
        moveRightWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.LEFT.value:
        moveLeftWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.BOTTOM.value:
        moveDownWorld(world, creature)
        return

def moveReverseFacing(world: World, creature: Creature):
    if creature.facing.value == facingDirection.BOTTOM.value:
        moveUpWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.LEFT.value:
        moveRightWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.RIGHT.value:
        moveLeftWorld(world, creature)
        return
    
    if creature.facing.value == facingDirection.UP.value:
        moveDownWorld(world, creature)
        return

def moveUpWorld(world: World, creature: Creature):
    posX = creature.positionX
    posY = creature.positionY
    creature.facing = facingDirection.UP

    if posY+1 < world.worldSize:
        newCell: CellData = world.cells[posY+1][posX]
        oldCell: CellData = world.cells[posY][posX]
        if newCell.isCreature or newCell.isBlockage:
            return

        creature.positionY = posY+1
        newCell.creature = creature
        newCell.isCreature = True

        oldCell.creature = None
        oldCell.isCreature = False

def moveDownWorld(world: World, creature: Creature):
    posX = creature.positionX
    posY = creature.positionY
    creature.facing = facingDirection.BOTTOM

    if posY-1 >= 0:
        newCell: CellData = world.cells[posY-1][posX]
        oldCell: CellData = world.cells[posY][posX]
        if newCell.isCreature or newCell.isBlockage:
            return

        creature.positionY = posY-1

        newCell.creature = creature
        newCell.isCreature = True

        oldCell.creature = None
        oldCell.isCreature = False

def moveRightWorld(world: World, creature: Creature):
    posX = creature.positionX
    posY = creature.positionY
    creature.facing = facingDirection.RIGHT

    if posX+1 < world.worldSize:
        newCell: CellData = world.cells[posY][posX+1]
        oldCell: CellData = world.cells[posY][posX]
        if newCell.isCreature or newCell.isBlockage:
            return

        creature.positionX = posX+1

        newCell.creature = creature
        newCell.isCreature = True

        oldCell.creature = None
        oldCell.isCreature = False

def moveLeftWorld(world: World, creature: Creature):
    posX = creature.positionX
    posY = creature.positionY
    creature.facing = facingDirection.LEFT

    if posX-1 >= 0:
        newCell: CellData = world.cells[posY][posX-1]
        oldCell: CellData = world.cells[posY][posX]
        if newCell.isCreature or newCell.isBlockage:
            return

        creature.positionX = posX-1

        newCell.creature = creature
        newCell.isCreature = True

        oldCell.creature = None
        oldCell.isCreature = False