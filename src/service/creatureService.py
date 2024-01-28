from src.model.creature import Creature
from src.service.geneticsService import generateRandomGene

def generateCreatureWithGenome(settings) -> Creature:
    # creature = Creature(genomeLength, innerNeurons)
    creature = Creature(
        settings["genomeLength"],
        settings["innerNeurons"],
        settings["maxAge"]
    )

    for i in range(0, creature.genomeLength):
        newGene = generateRandomGene()
        creature.genome.append(newGene)

    return creature