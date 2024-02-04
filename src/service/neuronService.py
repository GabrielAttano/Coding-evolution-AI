import secrets
import random

from model.neuron import SensoryNeuron, ActionNeuron, IntermediateNeuron

import service.functions.sensoryNeuronFunctions as snFunctions
import service.functions.actionNeuronFunctions as acFunctions

def generateRandomGene() -> str:
    random_hex = secrets.token_hex(4)
    return random_hex

def copyGenome(genome: list, mutationChance: float) -> list:
    hex_digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    copiedGenome = list()
    for gene in genome:
        copiedGene = ""
        for char in gene:
            if random.random() <= mutationChance:
                index = random.randint(0, len(hex_digit_list)-1)
                copiedGene += hex_digit_list[index]
            else:
                copiedGene += char
        copiedGenome.append(copiedGene)
    return copiedGenome          

def generateInputNeurons() -> list:
    inputNeurons = list()

    inputNeurons.append(SensoryNeuron(
        name="S_xDist",
        sensoryFunction=snFunctions.xDistanceFunction
    ))

    inputNeurons.append(SensoryNeuron(
        name="S_yDist",
        sensoryFunction=snFunctions.yDistanceFunction
    ))

    inputNeurons.append(SensoryNeuron(
        name="S_rand",
        sensoryFunction=snFunctions.randomInput
    ))

    inputNeurons.append(SensoryNeuron(
        name="S_facCreat",
        sensoryFunction=snFunctions.facingCreature
    ))

    inputNeurons.append(SensoryNeuron(
        name="S_adjCreat",
        sensoryFunction=snFunctions.adjacentToCreature
    ))

    return inputNeurons

def generateActionNeurons() -> list:
    actionNeurons = list()

    actionNeurons.append(ActionNeuron(
        name="A_mvFwdF",
        actionFunction=acFunctions.moveForwardFacing
    ))

    actionNeurons.append(ActionNeuron(
        name="A_mvRvsF",
        actionFunction=acFunctions.moveReverseFacing
    ))

    actionNeurons.append(ActionNeuron(
        name="A_mvRlF",
        actionFunction=acFunctions.moveRightLeftFacing
    ))

    actionNeurons.append(ActionNeuron(
        name="A_mvUpbtW",
        actionFunction=acFunctions.moveUpBottomWorld
    ))

    actionNeurons.append(ActionNeuron(
        name="A_mvRlW",
        actionFunction=acFunctions.moveRightLeftWorld
    ))

    actionNeurons.append(ActionNeuron(
        name="A_mvRand",
        actionFunction=acFunctions.moveRandom
    ))

    actionNeurons.append(ActionNeuron(
        name="A_setResp",
        actionFunction=acFunctions.setResponsiveness
    ))

    return actionNeurons

def generateIntermediateNeurons(total: int) -> list:
    intermediateNeurons = list()
    for i in range(total):
        name = "I_" + str(i)
        intermediateNeurons.append(IntermediateNeuron(name))
    return intermediateNeurons
