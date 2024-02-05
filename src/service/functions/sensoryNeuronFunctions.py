from src.model.world import World, CellData
from src.model.creature import Creature, facingDirection

import random

def xDistanceFunction(world: World, creature: Creature):
    return creature.positionX / world.worldSize

def yDistanceFunction(world: World, creature: Creature):
    return creature.positionY / world.worldSize

def randomInput(world: World, creature: Creature):
    return random.random();

def facingCreature(world: World, creature: Creature):
    cell: CellData = getFacingCell(world, creature)
    if cell == None: 
        return 0
    
    if cell.isCreature:
        return 1
    else:
        return 0

def adjacentToCreature(world: World, creature: Creature):
    xPos = creature.positionX
    yPos = creature.positionY
    worldSize = world.worldSize
    cell: CellData = None

    for x in range(xPos-1, xPos+2):
        for y in range(yPos-1, yPos+2):
            if x < 0 or x >= worldSize: continue
            if y < 0 or y >= worldSize: continue
            if x == xPos and y == yPos: continue
            
            cell = world.cells[y][x]
            if cell.isCreature: 
                return 1

    return 0

def age(world: World, creature: Creature):
    return creature.age / creature.maxAge

def populationDensity(world: World, creature: Creature):
    pass

def blockageForward(world: World, creature: Creature):
    pass

def leftrightBlockage(world: World, creature: Creature):
    pass

def updownBlockage(world: World, creature: Creature):
    pass

def lastMovementX(world: World, creature: Creature):
    if creature.facing.value == facingDirection.RIGHT.value:
        return 1
    else:
        return 0

def lastMovementY(world: World, creature: Creature):
    if creature.facing.value == facingDirection.UP.value:
        return 1
    else:
        return 0

def nearestBorderDistance(world: World, creature: Creature):    
    distanceX = creature.positionX
    if creature.positionX >= world.worldSize // 2:
        distanceX = world.worldSize - creature.positionX
    distanceY = creature.positionY
    if creature.positionY >= world.worldSize // 2:
        distanceY = world.worldSize - creature.positionY
    
    nearestDistance = distanceX if distanceX < distanceY else distanceY
    return nearestDistance / world.worldSize

def getFacingCell(world: World, creature: Creature):
    cell: CellData = None
    posX = creature.positionX
    posY = creature.positionY

    if creature.facing.value == facingDirection.UP.value:
        if posY+1 < world.worldSize:
            cell = world.cells[posY+1][posX]

    if creature.facing.value == facingDirection.RIGHT.value:
        if posX+1 < world.worldSize:
            cell = world.cells[posY][posX+1]

    if creature.facing.value == facingDirection.BOTTOM.value:
        if posY-1 >= 0:
            cell = world.cells[posY-1][posX]

    if creature.facing.value == facingDirection.LEFT.value:
        if posX-1 >= 0:
            cell = world.cells[posY][posX-1]
    
    return cell
