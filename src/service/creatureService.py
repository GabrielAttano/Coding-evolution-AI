from model.creature import Creature

from service.neuronService import generateRandomGene, copyGenome

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

def selfReplicate(creature: Creature, mutationChance: float) -> Creature:
    newCreature = Creature(creature.genomeLength, creature.innerNeurons, creature.maxAge)
    newCreature.genome = copyGenome(creature.genome, mutationChance)
    return newCreature
    

