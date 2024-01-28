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
    settings = loadSettings()
    


# world = World()
# worldSize = 3000

# generateWorld(world, worldSize)

# creature = generateCreatureWithGenome(5, 5)
# for gene in creature.genome:
#     print(gene)
#     print(decodeGene(gene))


# insertCreature(world, int(worldSize/2), int(worldSize/2), creature)
# printWorld(world)
# print(world.population)

# os.system("cls")
# printWorld(world)
# paintWorld(world)
# time.sleep(1)

# for i in range(0, 60):
#     acNeuronService.doAction(world, creature, acNeuronService.Actions.MOVE_RANDOM)
#     os.system("cls")
#     paintWorld(world, False)



# sensoryNeurons = generateInputNeurons()
# actionNeurons = generateActionNeurons()
# for sensoryNeuron in sensoryNeurons:
#     print(sensoryNeuron.name)
# for actionNeuron in actionNeurons:
#     print(actionNeuron.name)


