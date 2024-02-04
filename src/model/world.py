from model.creature import Creature

class World:
    cells: list
    worldSize: int
    population: int = 0

class CellData:
    
    def __init__(self) -> None:
        self.isCreature = False
        self.isBlockage = False
        self.creature: Creature = None