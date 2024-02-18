from model.world import World, CellData
from service.brainService import decodeGeneToBinary

import numpy as np
import cv2

class VideoRenderer:
    def __init__(self, fps = 30, upscaleFactor = 10) -> None:
        self.inMemoryFrames = list()
        self.fps = fps
        self.upscaleFactor = upscaleFactor

    def saveFrame(self, world: World):
        upscaledSize = (world.worldSize * self.upscaleFactor, world.worldSize * self.upscaleFactor, 3)
        blankImage = np.ones(upscaledSize, dtype=np.uint8) * 255

        for row in range(world.worldSize):
            for col in range(world.worldSize):
                if world.cells[row][col].isCreature:
                    creatureColor = self.getColorFromGenome(world.cells[row][col].creature.genome)
                    x, y = row * self.upscaleFactor, col * self.upscaleFactor
                    center = (y + self.upscaleFactor // 2, x + self.upscaleFactor // 2)
                    cv2.circle(blankImage, center, self.upscaleFactor // 2, color=creatureColor, thickness=-1)

        # Save the image
        self.inMemoryFrames.append(blankImage.copy())

    def createVideo(self, name: str):
        height, width, _ = self.inMemoryFrames[0].shape
        size = (width, height)

        out = cv2.VideoWriter(name+'.mp4', cv2.VideoWriter_fourcc(*'mp4v'), self.fps, size)

        for i in range(len(self.inMemoryFrames)):
            resized_frame = cv2.resize(self.inMemoryFrames[i], size, interpolation=cv2.INTER_NEAREST)
            out.write(resized_frame)

        out.release()

    def clearFrames(self):
        self.inMemoryFrames.clear()

    def getColorFromGenome(self, genome: list):
        redBinary = decodeGeneToBinary(genome[0])
        greenBinary = decodeGeneToBinary(genome[len(genome)//2])
        blueBinary = decodeGeneToBinary(genome[-1])

        red = int(redBinary[1], 2) % 255
        green = int(greenBinary[3], 2) % 255
        blue = int(blueBinary[1], 2) % 255

        return (blue, green, red)
        
