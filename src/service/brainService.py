from model.creature import Creature
from model.neuron import ActionNeuron, SensoryNeuron, IntermediateNeuron, NeuronTypes, Neuron
from model.brain import Connection
from model.world import World

from service.neuronService import generateIntermediateNeurons, NeuronsHandler
from service.functions.intermediateNeuronFunctions import getOutput
from service.functions.actionNeuronFunctions import Actions

import copy

# Brain generation

def generateCreatureBrain(creature: Creature, neuronsHandler: NeuronsHandler, weightDivisor: int):
    sensoryNeurons = neuronsHandler.sensoryNeurons
    actionNeurons = neuronsHandler.actionNeurons
    # generate all intermediateNeurons
    creature.brain.intermediateNeurons = generateIntermediateNeurons(creature.innerNeurons)
    
    # generate connections
    for gene in creature.genome:
        binaryGene = decodeGeneToBinary(gene)

        # Gets the source neuron
        sourceType = NeuronTypes.SENSORY if binaryGene[0] == "0" else NeuronTypes.INTERMEDIATE
        sourceNeuron: Neuron = getSourceNeuron(creature, sensoryNeurons, binaryGene)

        # Gets the sink neuron
        sinkType = NeuronTypes.INTERMEDIATE if binaryGene[2] == "0" else NeuronTypes.ACTION
        sinkNeuron: Neuron = getSinkNeuron(creature, actionNeurons, binaryGene)
        
        # Gets the weight of the connection
        sign = 1 if binaryGene[4][0] == '0' else -1
        decimalValue = int(binaryGene[4][1:], 2) * sign
        weight = decimalValue / weightDivisor

        connection: Connection = createConnection(creature, sourceNeuron, sinkNeuron, weight)
        creature.brain.connections.append(connection)

    removeUselessConnections(creature)
    sortConnections(creature)

def createConnection(creature: Creature, sourceNeuron: Neuron, sinkNeuron: Neuron, weight: float) -> Connection:
    connection = Connection()
    # ======= Weight =======
    connection.weight = weight

    # ======= Source neuron connection =======
    if sourceNeuron.type.value == NeuronTypes.SENSORY.value:
        # get the sensory neuron if it exists
        sensoryNeuron: SensoryNeuron = getSourceNeuronInBrain(creature, sourceNeuron)
        if sensoryNeuron == None:
            # if the neuron doesn't exist already in brain
            # create a shallow copy of it and insert in the brain
            sensoryNeuron = copy.copy(sourceNeuron)
            creature.brain.sensoryNeurons.append(sensoryNeuron)
        connection.sourceNeuron = sensoryNeuron
    elif sourceNeuron.type.value == NeuronTypes.INTERMEDIATE.value:
        # get the intermediate neuron
        intermediateNeuron: IntermediateNeuron = getIntermediateNeuronInBrain(creature, sourceNeuron)
        if intermediateNeuron == None:
            # if it doesnt exist, there is something wrong
            print("Couldnt find intermediate neuron in brain. Finishing...")
            return

        connection.sourceNeuron = intermediateNeuron

    # ======= Sink neuron connection =======
    if sinkNeuron.type.value == NeuronTypes.ACTION.value:
        # Get the action neuron if it exists
        actionNeuron: ActionNeuron = getSinkNeuronInBrain(creature, sinkNeuron)
        if actionNeuron == None:
            # if the neuron doesn't exist already in brain
            # create a shallow copy of it and insert in the brain
            actionNeuron = copy.copy(sinkNeuron)
            creature.brain.actionNeurons.append(copy.copy(actionNeuron))
        connection.sinkNeuron = actionNeuron
    elif sinkNeuron.type.value == NeuronTypes.INTERMEDIATE.value:
        # get the intermediate neuron
        intermediateNeuron: IntermediateNeuron = getIntermediateNeuronInBrain(creature, sinkNeuron)
        if intermediateNeuron == None:
            # if it doesnt exist, there is something wrong
            print("Couldnt find intermediate neuron in brain. Finishing...")
            return

        connection.sinkNeuron = intermediateNeuron

    return connection

def removeUselessConnections(creature: Creature):
    connection: Connection = None
    totalIntermediateConnections = dict()
    for intermediateNeuron in creature.brain.intermediateNeurons:
        totalIntermediateConnections[intermediateNeuron.name] = 0

    for connection in creature.brain.connections:
        if connection.sourceNeuron.type.value == NeuronTypes.INTERMEDIATE.value:
            # check if not connected to self
            if connection.sinkNeuron.type.value == NeuronTypes.INTERMEDIATE.value:
                if connection.sourceNeuron.name == connection.sinkNeuron.name:
                    continue
            # add to total connection count
            key = connection.sourceNeuron.name
            totalIntermediateConnections[key] += 1

    for key, value in totalIntermediateConnections.items():
        if value == 0:
            # print(f"Removing unused connections where sink and source is {key}")
            # print(f"Current total connections: {str(len(creature.brain.connections))}")
            removeSinkConnectionsByKey(creature, key)
            removeSourceConnectionsByKey(creature, key)
            # print(f"new total connections: {str(len(creature.brain.connections))}")
            
def removeSinkConnectionsByKey(creature: Creature, key: str):
    filteredConnections = [
        connection for connection in creature.brain.connections if connection.sinkNeuron.name != key
        ]
    creature.brain.connections = filteredConnections

def removeSourceConnectionsByKey(creature: Creature, key: str):
    filteredConnections = [
        connection for connection in creature.brain.connections if connection.sourceNeuron.name != key
        ]
    creature.brain.connections = filteredConnections
    
# Simulation

def simulateBrain(world: World, creature: Creature):
    updateSensoryNeurons(world, creature)
    resetSinkNeurons(creature)

    connection: Connection = None
    for connection in creature.brain.connections:
        simulateConnection(connection)
    
    finalAction: Actions = None
    finalActionValue = 0

    actionNeuron: ActionNeuron = None
    for actionNeuron in creature.brain.actionNeurons:
        action: Actions = actionNeuron.actionFunction(creature, actionNeuron.outputValue)
        if action != None and abs(actionNeuron.outputValue) > finalActionValue:
            finalAction = action
            finalActionValue = abs(actionNeuron.outputValue)
    
    creature.queuedAction = finalAction
    
def simulateConnection(connection: Connection):
    sourceNeuron: Neuron = connection.sourceNeuron
    sinkNeuron: Neuron = connection.sinkNeuron

    sinkNeuron.inputValue += sourceNeuron.outputValue * connection.weight

    sinkType = connection.sinkNeuron.type.value
    if sinkType == NeuronTypes.ACTION.value or sinkType == NeuronTypes.INTERMEDIATE.value:
        sinkNeuron.outputValue = getOutput(sinkNeuron.inputValue)

# Getters and utils        
def sortConnections(creature: Creature) -> list:
    sourceStartConnections = list()
    intermediateStartConnections = list()

    connection: Connection = None
    for connection in creature.brain.connections:
        if connection.sourceNeuron.type.value == NeuronTypes.SENSORY.value:
            sourceStartConnections.append(connection)
        if connection.sourceNeuron.type.value == NeuronTypes.INTERMEDIATE.value:
            intermediateStartConnections.append(connection)
    
    sourceStartConnections.extend(intermediateStartConnections)
    creature.brain.connections = sourceStartConnections

def resetSinkNeurons(creature: Creature):
    intermediateNeuron: IntermediateNeuron = None
    for intermediateNeuron in creature.brain.intermediateNeurons:
        intermediateNeuron.inputValue = 0
        intermediateNeuron.outputValue = 0
    actionNeuron: ActionNeuron = None
    for actionNeuron in creature.brain.actionNeurons:
        actionNeuron.inputValue = 0
        actionNeuron.outputValue = 0

def updateSensoryNeurons(world: World, creature: Creature):
    currentNeuron: SensoryNeuron = None
    for currentNeuron in creature.brain.sensoryNeurons:
        currentNeuron.outputValue = currentNeuron.sensoryFunction(world, creature)
        
def getSinkNeuronInBrain(creature: Creature, neuron: Neuron) -> ActionNeuron:
    for actionNeuron in creature.brain.actionNeurons:
        if actionNeuron.name == neuron.name:
            return actionNeuron
    return None

def getIntermediateNeuronInBrain(creature: Creature, neuron: Neuron) -> IntermediateNeuron:
    for intermediateNeuron in creature.brain.intermediateNeurons:
        if intermediateNeuron.name == neuron.name:
            return intermediateNeuron
        
def getSourceNeuronInBrain(creature: Creature, neuron: Neuron) -> SensoryNeuron:
    for sourceNeuron in creature.brain.sensoryNeurons:
        if sourceNeuron.name == neuron.name:
            return sourceNeuron
    return None

def getSourceNeuron(creature: Creature, sensoryNeurons: list, binaryGene: list()) -> Neuron:
    # Gets the source neuron
    sourceType = NeuronTypes.SENSORY if binaryGene[0] == "0" else NeuronTypes.INTERMEDIATE
    sourceNeuron: Neuron = None

    if sourceType.value == NeuronTypes.SENSORY.value:
        index = int(binaryGene[1], 2) % len(sensoryNeurons)
        sourceNeuron: SensoryNeuron = sensoryNeurons[index]
    else:
        index = int(binaryGene[1], 2) % len(creature.brain.intermediateNeurons)
        sourceNeuron: IntermediateNeuron = creature.brain.intermediateNeurons[index]
    
    return sourceNeuron

def getSinkNeuron(creature: Creature, actionNeurons: list, binaryGene: list()) -> Neuron:
    sinkType = NeuronTypes.INTERMEDIATE if binaryGene[2] == "0" else NeuronTypes.ACTION
    sinkNeuron: Neuron = None

    if sinkType.value == NeuronTypes.INTERMEDIATE.value:
        index = int(binaryGene[3], 2) % len(creature.brain.intermediateNeurons)
        sinkNeuron: IntermediateNeuron = creature.brain.intermediateNeurons[index]
    else:
        index = int(binaryGene[3], 2) % len(actionNeurons)
        sinkNeuron: ActionNeuron = actionNeurons[index]

    return sinkNeuron

def decodeGeneToBinary(gene: str) -> list:
    # Transforms the hexadecimal to binary
    decodedBinary = list()
    binary_string = ''.join(format(int(digit, 16), '04b') for digit in gene)
    
    # separates the binary
    # 0: source id
    decodedBinary.append(binary_string[0])
    # 1: source value
    decodedBinary.append(binary_string[1:8])
    # 2: sink id
    decodedBinary.append(binary_string[8:9])
    # 3: sink value
    decodedBinary.append(binary_string[9:16])
    # 5: weight value
    decodedBinary.append(binary_string[16:32])

    return decodedBinary

