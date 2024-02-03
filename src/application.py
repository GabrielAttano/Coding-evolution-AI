from service.simulationService import handleSimulation
from service.settingsService import SettingsHandler

import json
import os

def loadSettings() -> dict:
    scriptPath = os.path.abspath(__file__)
    configuration_path = os.path.join(os.path.dirname(scriptPath), 'simulationSettings.json')

    settings = dict()
    with open(configuration_path, 'r') as file:
        settings = json.load(file)
    
    return settings

if __name__ == "__main__":
    settingsHandler = SettingsHandler()
    handleSimulation(settingsHandler)
