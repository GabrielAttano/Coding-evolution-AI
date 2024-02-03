# Coding evolution
#### :construction: WORK IN PROGRESS :construction:	
This repository wouldn't exist without the video that inspired it, 
[I programmed some creatures. They Evolved.
](https://www.youtube.com/watch?v=N3tRFayqVtk&t=905s) by David Randall Miller.

----
# Coding life
## Table of contents
1. [Description](#description)
2. [Running the project](#running-the-project)
3. [Settings](#settings)
3. [Roadmap](#roadmap)

## Description
The main idea is to simulate evolution using a neural network. Basically, simulate creatures that have neural networks as their brain and are selected to reproduce according to some arbitrary rule chosen by a higher power.

:construction: This is currently a work in progress, and is not yet optimized at all. Expect it to take quite some time in simulating more than a few hundred creatures. :construction:

## Running the project
Clone the project anywhere you like, then create and activate a virtual environment in the source folder (Recommended). With it activated, install the requirements.txt with:
```
pip install -r requirements.txt
```
After installing the requirements, you can navigate to the src folder and run the application from there:
```
python application.py
```
If you want to fidget with the settings, you can do so in the simulationSettings.json, located at the src folder.

## Settings
To change the settings of the application, you can do them in the simulationSettings.json, located at the src folder.

Here's how it looks:
```json
{
    "creatureSettings": 
    {
        "genomeLength": 32,
        "innerNeurons": 4,
        "weightDivisor": 8000,
        "maxAge": 20,
        "mutationChance": 0.001
    },
    "worldSettings":
    {
        "worldSize": 128,
        "startPopulation": 1000
    },
    "simulationSettings":
    {   
        "totalGenerations": 1500,
        "totalSteps": 300,
        "debug": false,
        "saveVideo": true,
        "showTime": true,
        "saveVideoGenerations": [0, 10, 20, 50, 100, 250, 500, 750, 1000, 1499]
    }
}
```
#### Creature settings
`genomeLength`: The amount of genes in each creature genome.

`innerNeurons`: The amount of intermediate neurons in each creature brain.

`weightDivisor`: Number used to divide a 16 bit signed integer and use the result as the weight of each connection. The default value **8000** gives the range -4.09 to -4.09.

`maxAge`: creature max age.

`mutationChance`: Gene mutation chance.

#### World settings
`worldSize`: World size.

`startPopulations`: The amount of creatures in the start of each generation.

#### Simulation settings
There is only one selection implemented, and it isnt really a choice. Currently, all creatures in the bottom-left corner of the world are selected and kept for the next generation population.

`totalGenerations`: The amount of generations that the simulation is going to do.

`totalSteps`: The amount of steps in each generation. The brain simulation and actions for each creature are done in each step.

`debug`: Print some extra informations when running the application

`saveVideo`: Save a video at the end of each generation. (If not using specific generations, it will **slow** the application down)

`showTime`: Show the time taken in each generation

`saveVideoGenerations`: The simulation only saves videos of the generations in this list. Currently, this must have at least one number or no video is going to be saved at all.

## Roadmap

Currently, the application is *kind of* running as intended. However, there is crearly *some* performance issues that must be solved, and a overhaul of the very rudimentary video-creating mess that exists right now.
This is going to be my main focus, along with making the code cleaner and easier to work with. After those issues are solved, the goal is to expand on the main idea from the [video that inspired this project](https://www.youtube.com/watch?v=N3tRFayqVtk&t=905s) and test different ideas for selection, the simulation itself, and easier interaction with the program for a broader audience.
- [ ] Map renderer
    - [ ] Color each creature using their genome
    - [ ] Better solution for the frame generation
- [ ] Selections
    - [ ] Fix and add new selections
- [ ] Refactor code
    - [ ] Better readability
    - [ ] Multiprocesses
- [ ] Neurons
    - [ ] Add new sensory neurons

##### About the video
While the video inspired this repository, it isn't intended to be a copy. I've made sure to avoid looking at any code, and to instead use the video and this place as an way to explore and learn new things. 
