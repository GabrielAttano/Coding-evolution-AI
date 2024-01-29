import secrets

from src.model.genetics import Neuron, NeuronTypes, SensoryNeuron, ActionNeuron, IntermediateNeuron

import src.service.functions.sensoryNeuronFunctions as snFunctions
import src.service.functions.actionNeuronFunctions as acFunctions

def generateRandomGene() -> str:
    random_hex = secrets.token_hex(4)
    return random_hex

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
