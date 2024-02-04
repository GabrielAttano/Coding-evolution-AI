from model.world import World
from model.creature import Creature
from model.brain import Brain

from service.videoRendererService import VideoRenderer
from service.settingsService import SettingsHandler
from service.neuronService import NeuronsHandler
import service.worldService as worldService
from service.creatureService import generateCreatureWithGenome, selfReplicate
from service.brainService import simulateBrain, generateCreaturesBrain
from service.actionNeuronService import doAction

from datetime import datetime

def handleSimulation(settingsHandler: SettingsHandler):
    if settingsHandler.debug:
        print("=================================")
        print("Debug mode activated.")
        print("=================================")
    scriptStartTime = datetime.now()

    # ========== Creating world ==========
    if settingsHandler.debug:
        print("=================================")
        print("Creating world. Size: " + str(settingsHandler.worldSize))
        
    world = World()
    worldService.generateWorld(settingsHandler)

    if settingsHandler.debug: print("Finished creating world.")

    # ========== load neurons ==========
    if settingsHandler.debug:
        print("=================================")
        print("Loading neurons")
    neuronsHandler = NeuronsHandler()
    if settingsHandler.debug:
        print("Finished loading neurons.")
        print("Total sensory neurons: " + str(len(neuronsHandler.sensoryNeurons)))
        print("Total action neurons: " + str(len(neuronsHandler.actionNeurons)))

    scriptEndTime = datetime.now()

    simulateGenerations(settingsHandler, neuronsHandler, world)

    if settingsHandler.showTime: 
        print(f"Setup total time: {str(scriptEndTime-scriptStartTime)}")

def simulateGenerations(settingsHandler: SettingsHandler, neuronsHandler: NeuronsHandler, world: World):
    saveGenerationVideo = False
    videoRenderer = VideoRenderer()

    creatures = worldService.populateWorld(world, settingsHandler)
    generateCreaturesBrain(creatures, neuronsHandler, settingsHandler.weightDivisor)

    for i in range(settingsHandler.totalGenerations):
        # Checks if this generation must be saved as a video
        if settingsHandler.saveVideo:
            saveGenerationVideo = i in settingsHandler.saveVideoGenerations
        
        print(f"Simulating generation {i}")
        simulateGeneration(creatures, world, settingsHandler, saveGenerationVideo, videoRenderer)

        if saveGenerationVideo:
            videoRenderer.createVideo(f"generation_{i}")
            videoRenderer.clearFrames()

        # Selecting creatures and reproducing
        selectedCreatures = worldService.selectCreaturesInPosition(
            world, 
            worldService.SelectionTypes.TOP_LEFT, 
            creatures
        )
        print(f"Total selected creatures: {str(len(selectedCreatures))}")
        survivalRate = (len(selectedCreatures) / settingsHandler.startPopulation) * 100
        print(f"Generation {str(i + 1)} survival rate: {str(survivalRate)}%")

        # Remove creatures from the world
        worldService.clearWorld(world)

        # Repopulate creatures with the selected ones
        creatures = worldService.repopulateWorld(world, creatures, settingsHandler)
        generateCreaturesBrain(creatures, neuronsHandler, settingsHandler.weightDivisor)


def simulateGeneration(
        creatures: list, world: World, settingsHandler: SettingsHandler, saveVideo: bool, videorenderer: VideoRenderer = None
    ):

    if settingsHandler.debug: print("Starting simulation")
    simulationStartT = datetime.now()

    creature: Creature = None
    for i in range(settingsHandler.totalSteps):
        if settingsHandler.debug: print(f"Simulating step {i}")

        # Simulate brain of creatures to get queued action
        for creature in creatures:
            simulateBrain(world, creature)
        # do queued actions
        for creature in creatures:
            doAction(world, creature, creature.queuedAction)

        if saveVideo: 
            videorenderer.saveFrame(world)

    if settingsHandler.debug: print("Finished simulation")
    simulationEndT = datetime.now()
    if settingsHandler.showTime: 
        print(f"Simulation total time: {str(simulationEndT-simulationStartT)}")
