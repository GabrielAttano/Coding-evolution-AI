from src.service.worldService import generateWorld, printWorld, insertCreature, paintWorld
from src.service.creatureService import generateCreatureWithGenome
from src.service.geneticsService import generateInputNeurons, generateActionNeurons
import src.service.actionNeuronService as acNeuronService

from src.model.world import World
from src.model.genetics import Neuron, NeuronTypes, SensoryNeuron
from src.model.creature import Creature

import time
import os

world = World()
worldSize = 3000

generateWorld(world, worldSize)

creature = generateCreatureWithGenome(5, 5)
# for gene in creature.genome:
#     print(gene)
#     print(decodeGene(gene))


insertCreature(world, int(worldSize/2), int(worldSize/2), creature)
# printWorld(world)
# print(world.population)

os.system("cls")
# printWorld(world)
# paintWorld(world)
# time.sleep(1)

for i in range(0, 60):
    acNeuronService.doAction(world, creature, acNeuronService.Actions.MOVE_RANDOM)
    os.system("cls")
    paintWorld(world, False)



sensoryNeurons = generateInputNeurons()
actionNeurons = generateActionNeurons()
# for sensoryNeuron in sensoryNeurons:
#     print(sensoryNeuron.name)
# for actionNeuron in actionNeurons:
#     print(actionNeuron.name)


