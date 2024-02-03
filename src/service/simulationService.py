from model.world import World
from model.creature import Creature
from model.brain import Brain

import service.worldService as worldService
from service.creatureService import generateCreatureWithGenome, selfReplicate
from service.geneticsService import generateActionNeurons, generateInputNeurons
from service.brainService import generateCreatureBrain, simulateBrain
from service.actionNeuronService import doAction

from datetime import datetime

def handleSimulation(settings: dict):
    worldSettings = settings["worldSettings"]
    creatureSettings = settings["creatureSettings"]
    simulationSettings = settings["simulationSettings"]
    isDebug = simulationSettings["debug"]

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
    worldService.generateWorld(world, worldSettings["worldSize"])

    if isDebug: print("Finished creating world.")

    # ========== Populating world ==========
    startPopulation = worldSettings["startPopulation"]
    if isDebug: 
        print("=================================")
        print("Generating creatures. Total: " + str(startPopulation))

    creatures = populateWorld(startPopulation, world, isDebug, creatureSettings)

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

    totalGenerations = simulationSettings["totalGenerations"]
    saveVideo = simulationSettings["saveVideo"]
    saveVideoGenerations = simulationSettings["saveVideoGenerations"]
    mutationChance = creatureSettings["mutationChance"]

    framesInMemory = list()
    saveGenerationVideo = False

    for i in range(totalGenerations):
        if saveVideo:
            saveGenerationVideo = i in saveVideoGenerations
        
        print(f"Simulating generation {i}")
        framesInMemory = simulateGeneration(creatures, world, simulationSettings, saveGenerationVideo)
        if saveGenerationVideo:
            videoName = f"generation_{i}"
            worldService.createVideo(framesInMemory, videoName)

        # Selecting creatures and reproducing
        selectedCreatures = worldService.selectCreaturesInPosition(
            world, worldService.SelectionTypes.TOP_LEFT, creatures
        )
        print(f"Total selected creatures: {str(len(selectedCreatures))}")
        survivalRate = (len(selectedCreatures) / startPopulation) * 100
        print(f"Generation {str(i + 1)} survival rate: {str(survivalRate)}%")
        worldService.clearWorld(world)
        creatures = repopulateWorld(startPopulation, world, isDebug, selectedCreatures, mutationChance)
        for creature in creatures:
            generateCreatureBrain(creature, sensoryNeurons, actionNeurons, creatureSettings["weightDivisor"])
        

    if simulationSettings["showTime"]: print(f"Setup total time: {str(scriptEndTime-scriptStartTime)}")

def simulateGeneration(creatures: list, world: World, simulationSettings: dict, saveVideo: bool) -> list:
    # Loading configs
    isDebug = simulationSettings["debug"]
    showTime = simulationSettings["showTime"]
    totalSteps = simulationSettings["totalSteps"]
    # Others
    simulationStartT = datetime.now()
    frameList = list()

    if isDebug: print("Starting simulation")
    creature: Creature = None
    for i in range(totalSteps):
        if isDebug: print(f"Simulating step {i}")

        # Simulate brain of creatures to get queued action
        for creature in creatures:
            simulateBrain(world, creature)
        # do queued actions
        for creature in creatures:
            doAction(world, creature, creature.queuedAction)

        if saveVideo: worldService.paintWorld(world, True, frameList)

    if isDebug: print("Finished simulation")
    simulationEndT = datetime.now()
    if showTime: print(f"Simulation total time: {str(simulationEndT-simulationStartT)}")
    return frameList

def populateWorld(totalPopulation: int, world: World, isDebug: bool, creatureSettings: dict) -> list:
    creatures = list()
    for _ in range(totalPopulation):
        creatures.append(generateCreatureWithGenome(creatureSettings))

    if isDebug: print("Finished generating creatures. Total: " + str(len(creatures)))
    if isDebug: print("Inserting creatures into world randomly.")

    for creature in creatures:
        worldService.insertCreatureRandomPosition(world, creature)

    if isDebug: print("Finished inserting creatures. World population: " + str(world.population))

    return creatures

def repopulateWorld(totalPopulation: int, world: World, isDebug: bool, creatures: list, mutationChance: float) -> list:
    validCreatures = list()

    # Gets the creatures below maximum age (and age them +1)
    creature: Creature = None
    for creature in creatures:
        creature.age += 1
        if creature.age <= creature.maxAge:
            validCreatures.append(creature)
    
    newCreatures = list()
    while len(newCreatures) < totalPopulation:
        for creature in validCreatures:
            newCreatures.append(selfReplicate(creature, mutationChance))
            if len(newCreatures) >= totalPopulation:
                break

    if isDebug: print("Finished generating creatures. Total: " + str(len(newCreatures)))
    if isDebug: print("Inserting creatures into world randomly.")

    for creature in newCreatures:
        worldService.insertCreatureRandomPosition(world, creature)
    
    if isDebug: print("Finished inserting creatures. World population: " + str(world.population))
    return newCreatures
    



    
