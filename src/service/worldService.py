from model.world import World, CellData
from model.creature import Creature, facingDirection

from service.creatureService import selfReplicate, generateCreatureWithGenome
from service.settingsService import SettingsHandler

import random
from enum import Enum

class SelectionTypes(Enum):
    TOP = "top"
    TOP_LEFT = "top-left",
    TOP_RIGHT = "top-right",
    BOTTOM = "bottom"
    BOTTOM_LEFT = "bottom-left"
    BOTTOM_RIGHT = "bottom-right"

def generateWorld(world: World, settingsHandler: SettingsHandler):
        world.worldSize = settingsHandler.worldSize
        world.startPopulation = settingsHandler.startPopulation

        world.cells = list()
        for i in range(settingsHandler.worldSize):
            world.cells.append(list())
            for j in range(settingsHandler.worldSize):
                world.cells[i].append(CellData())

def clearWorld(world: World):
    currentCell: CellData = None
    for i in range(world.worldSize):
        for j in range(world.worldSize):
            currentCell = world.cells[i][j]
            currentCell.creature = None
            currentCell.isCreature = False
    world.population = 0

def insertCreature(world: World, posX: int, posY: int, creature: Creature):
    cell: CellData = world.cells[posY][posX]
    if not cell.isCreature:
        cell.isCreature = True
        cell.creature = creature
        creature.positionX = posX
        creature.positionY = posY
        world.population += 1

def insertCreatureRandomPosition(world: World, creature: Creature):
    currentWorldPop = world.population
    maxTries = 25
    tries = 0
    while currentWorldPop == world.population:
        if tries >= maxTries:
            break
        randomX = random.randint(0, world.worldSize - 1)
        randomY = random.randint(0, world.worldSize - 1)
        insertCreature(world, randomX, randomY, creature)
        tries += 1

    currentCell: CellData = None
    if tries >= maxTries:
        for i in range(world.worldSize):
            for j in range(world.worldSize):
                currentCell = world.cells[i][j]
                if not currentCell.isCreature and not currentCell.isBlockage:
                    print("force inserting creature")
                    insertCreature(world, i, j, creature)      

def populateWorld(world: World, settingsHandler: SettingsHandler) -> list:
    creatures = list()
    for _ in range(settingsHandler.startPopulation):
        creatures.append(generateCreatureWithGenome(settingsHandler.rawCreatureSettings))

    if settingsHandler.debug: 
        print("Finished generating creatures. Total: " + str(len(creatures)))
        print("Inserting creatures into world randomly.")

    for creature in creatures:
        insertCreatureRandomPosition(world, creature)

    if settingsHandler.debug:
        print("Finished inserting creatures. World population: " + str(world.population))

    return creatures

def repopulateWorld(world: World, creatures: list, settingsHandler: SettingsHandler) -> list:
    validCreatures = list()

    # Gets the creatures below maximum age (and age them +1)
    creature: Creature = None
    for creature in creatures:
        creature.age += 1
        if creature.age <= creature.maxAge:
            validCreatures.append(creature)
    
    newCreatures = list()
    while len(newCreatures) < settingsHandler.startPopulation:
        for creature in validCreatures:
            newCreatures.append(selfReplicate(creature, settingsHandler.mutationChance))
            if len(newCreatures) >= settingsHandler.startPopulation:
                break
    

    if settingsHandler.debug: 
        print("Finished generating creatures. Total: " + str(len(newCreatures)))
        print("Inserting creatures into world randomly.")

    for creature in newCreatures:
        insertCreatureRandomPosition(world, creature)
    
    if settingsHandler.debug: 
        print("Finished inserting creatures. World population: " + str(world.population))
    
    return newCreatures

def selectCreaturesInPosition(world: World, selectionType: SelectionTypes, creatures: list) -> list:
    if selectionType.value == SelectionTypes.TOP_LEFT.value:
        return selectTopLeft(world, creatures)

def selectTopLeft(world: World, creatures: list) -> list:
    selectedCreatures = list()
    halfSize = world.worldSize // 2

    creature: Creature = None
    for creature in creatures:
        validX = False
        validY = False
        if creature.positionX >= 0 and creature.positionX <= halfSize:
            validX = True
        if creature.positionY >= halfSize and creature.positionY <= world.worldSize:
            validY = True
        if validX and validY:
            selectedCreatures.append(creature)
    return selectedCreatures