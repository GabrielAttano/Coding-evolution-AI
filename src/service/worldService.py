from src.model.world import World, CellData
from src.model.creature import Creature, facingDirection

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

def insertCreature(world: World, posX: int, posY: int, creature: Creature):
    cell: CellData = world.cells[posY][posX]
    if not cell.isCreature:
        cell.isCreature = True
        cell.creature = creature
        creature.positionX = posX
        creature.positionY = posY
        world.population += 1
