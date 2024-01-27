from src.service.worldService import generateWorld, printWorld, insertCreature
from src.service.creatureService import generateCreatureWithGenome
from src.service.geneticsService import generateInputNeurons, generateActionNeurons
import src.service.actionNeuronService as acNeuronService

from src.model.world import World
from src.model.genetics import Neuron, NeuronTypes, SensoryNeuron
from src.model.creature import Creature

import time
import os

world = World()
generateWorld(world, 10)

creature = generateCreatureWithGenome(5, 5)
# for gene in creature.genome:
#     print(gene)
#     print(decodeGene(gene))


insertCreature(world, 5, 0, creature)
# printWorld(world)
# print(world.population)

os.system("cls")
printWorld(world)
time.sleep(1)

for i in range(0, 60):
    acNeuronService.doAction(world, creature, acNeuronService.Actions.MOVE_RANDOM)
    os.system("cls")
    printWorld(world)
    time.sleep(1)



sensoryNeurons = generateInputNeurons()
actionNeurons = generateActionNeurons()
# for sensoryNeuron in sensoryNeurons:
#     print(sensoryNeuron.name)
# for actionNeuron in actionNeurons:
#     print(actionNeuron.name)


