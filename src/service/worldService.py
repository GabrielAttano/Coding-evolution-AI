from src.model.world import World, CellData
from src.model.creature import Creature, facingDirection

import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

def generateWorld(world: World, worldSize: int):
        world.worldSize = worldSize

        world.cells = list()
        for i in range(worldSize):
            world.cells.append(list())
            for j in range(worldSize):
                world.cells[i].append(CellData())
    
def printWorld(world: World):
     for i in reversed(range(world.worldSize)):
        for j in range(world.worldSize):
            currentCell: CellData = world.cells[i][j]
            if currentCell.isCreature:
                if currentCell.creature.facing.value == facingDirection.UP.value:
                    print("^", end="")
                if currentCell.creature.facing.value == facingDirection.RIGHT.value:
                    print(">", end="")
                if currentCell.creature.facing.value == facingDirection.BOTTOM.value:
                    print("v", end="")
                if currentCell.creature.facing.value == facingDirection.LEFT.value:
                    print("<", end="")
                
                continue
            if currentCell.isBlockage:
                print("x", end="")
                continue
            print(" ", end="")
        print("\n")

def paintWorld(world: World, saveMode: bool):
    blank_image = np.ones((world.worldSize, world.worldSize, 3), dtype=np.uint8) * 255

    for row in reversed(range(world.worldSize)):
        for col in range(world.worldSize):
            if world.cells[row][col].isCreature:
                x, y = row, col
                cv2.circle(blank_image, (y, x), radius = 2, color=(0, 0, 255), thickness=-1)

    if not saveMode:
        plt.imshow(blank_image)
        plt.axis('off')
        plt.show()

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
    while currentWorldPop == world.population:
        randomX = random.randint(0, world.worldSize - 1)
        randomY = random.randint(0, world.worldSize - 1)
        insertCreature(world, randomX, randomY, creature)

