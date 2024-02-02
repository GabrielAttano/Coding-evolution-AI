from model.world import World
from model.creature import Creature
from model.brain import Brain, Connection

from service.worldService import generateWorld, insertCreatureRandomPosition, paintWorld, createVideo
from service.creatureService import generateCreatureWithGenome
from service.geneticsService import generateActionNeurons, generateInputNeurons
from service.brainService import generateCreatureBrain, simulateBrain

from datetime import datetime

def handleSimulation(settings: dict):
    worldSettings = settings["worldSettings"]
    creatureSettings = settings["creatureSettings"]
    simulationSettings = settings["simulationSettings"]
    isDebug = settings["debug"]

    if isDebug:
        print("=================================")
        print("Debug mode activated.")
        print("=================================")
        print("World settings: " + str(worldSettings))
        print("Creature settings: " + str(creatureSettings))

    scriptStartTime = datetime.now()

    # ========== Creating world ==========
    if isDebug:
        print("=================================")
        print("Creating world. Size: " + str(worldSettings["worldSize"]))
        
    world = World()
    generateWorld(world, worldSettings["worldSize"])

    if isDebug: print("Finished creating world.")

    # ========== Populating world ==========
    if isDebug: 
        print("=================================")
        print("Generating creatures. Total: " + str(worldSettings["startPopulation"]))
    creatures = list()
    for i in range(worldSettings["startPopulation"]):
        creatures.append(generateCreatureWithGenome(creatureSettings))
    if isDebug: print("Finished generating creatures. Total: " + str(len(creatures)))

    if isDebug: print("Inserting creatures into world randomly.")
    for creature in creatures:
        insertCreatureRandomPosition(world, creature)
    if isDebug: print("Finished inserting creatures. World population: " + str(world.population))

    # ========== load neurons ==========
    if isDebug:
        print("=================================")
        print("Loading neurons")

    sensoryNeurons = generateInputNeurons()
    actionNeurons = generateActionNeurons()

    if isDebug:
        print("Finished loading neurons.")
        print("Total sensory neurons: " + str(len(sensoryNeurons)))
        print("Total action neurons: " + str(len(actionNeurons)))

    # ========== generating creature's brains ==========
    if isDebug:
        print("=================================")
        print("Generating brains")
    
    for creature in creatures:
        if isDebug: print("-------------------------")
        generateCreatureBrain(creature, sensoryNeurons, actionNeurons, creatureSettings["weightDivisor"])
        if isDebug:
            brain: Brain = creature.brain
            print(f"Total sensory neurons: {str(len(brain.sensoryNeurons))}")
            print(f"Total intermediate neurons: {str(len(brain.intermediateNeurons))}")
            print(f"Total action neurons: {str(len(brain.actionNeurons))}")
            print("-------------------------")

    if isDebug:
        print("Finished generating creature's brains")
    scriptEndTime = datetime.now()

    saveVideo: bool = settings["saveVideo"]
    frameList = list()
    simulationStartT = datetime.now()
    for i in range(simulationSettings["totalSteps"]):
        if isDebug: 
            print(f"Simulating step {i}")
        for creature in creatures:
            simulateBrain(world, creature)
        if saveVideo:
            paintWorld(world, True, frameList)
    simulationEndT = datetime.now()

    if saveVideo: createVideo(frameList)
    if settings["showTime"]: 
        print(f"Setup total time: {str(scriptEndTime-scriptStartTime)}")
        print(f"Simulation total time: {str(simulationEndT-simulationStartT)}")
        
    
