import os
import json

class SettingsHandler:
    def __init__(self, configurationPath = "") -> None:
        self.rawCreatureSettings = dict()
        self.genomeLength = int
        self.innerNeurons = int
        self.weightDivisor = int
        self.maxAge = int
        self.mutationChance = float

        self.rawWorldSettings = dict()
        self.worldSize = int
        self.startPopulation = int
        
        self.rawSimulationSettings = dict()
        self.totalGenerations = int
        self.totalSteps = int
        self.debug = bool
        self.saveVideo = bool
        self.showTime = bool
        self.saveVideoGenerations = list
        
        self.loadSettings(configurationPath)
    
    def loadSettings(self, path: str = ""):
        configurationPath = ""

        if path == "":
            scriptPath = os.path.abspath(__file__)
            parentFolder = os.path.dirname(scriptPath)
            grandparentFolder = os.path.dirname(parentFolder)
            configurationPath = os.path.join(grandparentFolder, 'simulationSettings.json')
        else:
            configurationPath = path
        
        settings = dict()
        with open(configurationPath, 'r') as file:
            settings = json.load(file)

        self.parseLoadedSettings(settings)     
        
    def parseLoadedSettings(self, loadedSettings: dict):
        self.parseCreatureSettings(loadedSettings["creatureSettings"])
        self.parseWorldSettings(loadedSettings["worldSettings"])
        self.parseSimulationSettings(loadedSettings["simulationSettings"])

    def parseCreatureSettings(self, creatureSettings: dict):
        self.rawCreatureSettings = creatureSettings
        self.genomeLength = creatureSettings["genomeLength"]
        self.innerNeurons = creatureSettings["innerNeurons"]
        self.weightDivisor = creatureSettings["weightDivisor"]
        self.maxAge = creatureSettings["maxAge"]
        self.mutationChance = creatureSettings["mutationChance"]

    def parseWorldSettings(self, worldSettings: dict):
        self.rawWorldSettings = worldSettings
        self.worldSize = worldSettings["worldSize"]
        self.startPopulation = worldSettings["startPopulation"]

    def parseSimulationSettings(self, simulationSettings: dict):
        self.rawSimulationSettings = simulationSettings
        self.totalGenerations = simulationSettings["totalGenerations"]
        self.totalSteps = simulationSettings["totalSteps"]
        self.debug = simulationSettings["debug"]
        self.saveVideo = simulationSettings["saveVideo"]
        self.showTime = simulationSettings["showTime"]
        self.saveVideoGenerations = simulationSettings["saveVideoGenerations"]
