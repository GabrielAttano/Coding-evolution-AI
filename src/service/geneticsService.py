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
        name="x distance",
        sensoryFunction=snFunctions.xDistanceFunction
    ))

    inputNeurons.append(SensoryNeuron(
        name="y distance",
        sensoryFunction=snFunctions.yDistanceFunction
    ))

    inputNeurons.append(SensoryNeuron(
        name="random input",
        sensoryFunction=snFunctions.randomInput
    ))

    inputNeurons.append(SensoryNeuron(
        name="facing creature",
        sensoryFunction=snFunctions.facingCreature
    ))

    inputNeurons.append(SensoryNeuron(
        name="adjacent to creature",
        sensoryFunction=snFunctions.adjacentToCreature
    ))

    return inputNeurons

def generateActionNeurons() -> list:
    actionNeurons = list()

    actionNeurons.append(ActionNeuron(
        name="move forward facing",
        actionFunction=acFunctions.moveForwardFacing
    ))

    actionNeurons.append(ActionNeuron(
        name="move reverse facing",
        actionFunction=acFunctions.moveReverseFacing
    ))

    actionNeurons.append(ActionNeuron(
        name="move rightleft facing",
        actionFunction=acFunctions.moveRightLeftFacing
    ))

    actionNeurons.append(ActionNeuron(
        name="move upbottom world",
        actionFunction=acFunctions.moveUpBottomWorld
    ))

    actionNeurons.append(ActionNeuron(
        name="move rightleft world",
        actionFunction=acFunctions.moveRightLeftWorld
    ))

    actionNeurons.append(ActionNeuron(
        name="move random",
        actionFunction=acFunctions.moveRandom
    ))

    actionNeurons.append(ActionNeuron(
        name="set responsiveness",
        actionFunction=acFunctions.setResponsiveness
    ))

    return actionNeurons

def generateIntermediateNeurons(total: int) -> list:
    intermediateNeurons = list()
    for i in range(total):
        name = "IN" + str(i)
        intermediateNeurons.append(IntermediateNeuron(name))
    return intermediateNeurons
