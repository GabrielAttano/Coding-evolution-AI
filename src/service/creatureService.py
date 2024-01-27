from src.model.creature import Creature
from src.service.geneticsService import generateRandomGene

def generateCreatureWithGenome(genomeLength: int, innerNeurons: int) -> Creature:
    creature = Creature(genomeLength, innerNeurons)
    
    for i in range(0, genomeLength):
        newGene = generateRandomGene()
        creature.genome.append(newGene)

    return creature