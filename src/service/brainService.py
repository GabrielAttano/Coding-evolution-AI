from model.creature import Creature
from model.genetics import ActionNeuron, SensoryNeuron, IntermediateNeuron, NeuronTypes, Neuron

from service.geneticsService import generateIntermediateNeurons

def generateCreatureBrain(creature: Creature, sensoryNeurons: list, actionNeurons: list, weightDivisor: int):
    creature.brain.intermediateNeurons = generateIntermediateNeurons(creature.innerNeurons)

    for gene in creature.genome:
        binaryGene = decodeGeneToBinary(gene)

        # Gets the source neuron
        sourceType = NeuronTypes.SENSORY if binaryGene[0] == "0" else NeuronTypes.INTERMEDIATE
        sourceNeuron: Neuron = None

        if sourceType.value == NeuronTypes.SENSORY.value:
            index = int(binaryGene[1], 2) % len(sensoryNeurons)
            sourceNeuron: SensoryNeuron = sensoryNeurons[index]
        else:
            index = int(binaryGene[1], 2) % len(creature.brain.intermediateNeurons)
            sourceNeuron: IntermediateNeuron = creature.brain.intermediateNeurons[index]

        # Gets the sink neuron
        sinkType = NeuronTypes.INTERMEDIATE if binaryGene[2] == "0" else NeuronTypes.ACTION
        sinkNeuron: Neuron = None

        if sinkType.value == NeuronTypes.INTERMEDIATE.value:
            index = int(binaryGene[3], 2) % len(creature.brain.intermediateNeurons)
            sinkNeuron: IntermediateNeuron = creature.brain.intermediateNeurons[index]
        else:
            index = int(binaryGene[3], 2) % len(actionNeurons)
            sinkNeuron: ActionNeuron = actionNeurons[index]
        
        # Gets the weight of the connection
        sign = 1 if binaryGene[4][0] == '0' else -1
        decimalValue = int(binaryGene[4][1:], 2) * sign
        weight = decimalValue / weightDivisor
        
        print("source: " + sourceNeuron.name + " | Sink: " + sinkNeuron.name + " | weight: " + str(weight))

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

