from enum import Enum

class NeuronTypes(Enum):
    SENSORY = "sensory"
    INTERMEDIATE = "intermediate"
    ACTION = "action"

class Neuron:
    def __init__(self, type: NeuronTypes, name: str) -> None:
        self.name = name
        self.type = type
        self.inputValue = 0.0
        self.outputValue = 0.0
        self.inputConnections = list()
        self.outputConnections = list()
        
class SensoryNeuron(Neuron):
    def __init__(self, name: str, sensoryFunction: callable) -> None:
        super().__init__(NeuronTypes.SENSORY, name)
        self.sensoryFunction = sensoryFunction
        
class ActionNeuron(Neuron):
    def __init__(self, name: str, actionFunction: callable) -> None:
        super().__init__(NeuronTypes.ACTION, name)
        self.actionFunction = actionFunction