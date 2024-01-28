from model.world import World
from model.creature import Creature

from service.worldService import generateWorld
from service.creatureService import generateCreatureWithGenome
from service.geneticsService import generateActionNeurons, generateInputNeurons, generateIntermediateNeurons

def handleSimulation(settings: dict):
    worldSettings = settings["worldSettings"]
    creatureSettings = settings["creatureSettings"]
    isDebug = settings["debug"]

    if isDebug:
        print("Debug mode activated.")
        print("World settings: " + str(worldSettings))
        print("Creature settings: " + str(creatureSettings))

    # ========== Creating world ==========
    if isDebug: print("Creating world. Size: " + str(worldSettings["worldSize"]))
    world = World()
    generateWorld(world, worldSettings["worldSize"])

    if isDebug: print("Finished creating world.")

    # ========== Populating world ==========
    if isDebug: print("Generating creatures. Total: " + str(worldSettings["startPopulation"]))
    creatures = list()
    for i in range(worldSettings["startPopulation"]):
        creatures.append(generateCreatureWithGenome(creatureSettings))

    if isDebug: print("Finished generating creatures. Total: " + str(len(creatures)))

    # ========== load neurons ==========
    if isDebug: print("Loading neurons")

    sensoryNeurons = generateInputNeurons()
    intermediateNeurons = generateIntermediateNeurons(creatureSettings["innerNeurons"])
    actionNeurons = generateActionNeurons()
    