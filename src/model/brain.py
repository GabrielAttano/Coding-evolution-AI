from model.neuron import Neuron

class Brain:
    def __init__(self) -> None:
        self.sensoryNeurons = list()
        self.intermediateNeurons = list()
        self.actionNeurons = list()
        self.connections = list()
        self.isBrainCreated = False

class Connection:
    def __init__(self) -> None:
        self.sourceNeuron: Neuron = None
        self.sinkNeuron: Neuron = None
        self.weight: float = 0