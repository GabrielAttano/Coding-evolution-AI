from service.simulationService import handleSimulation
from service.settingsService import SettingsHandler

import json
import os

if __name__ == "__main__":
    settingsHandler = SettingsHandler()
    handleSimulation(settingsHandler)
