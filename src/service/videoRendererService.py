from model.world import World, CellData

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

        for row in reversed(range(world.worldSize)):
            for col in range(world.worldSize):
                if world.cells[row][col].isCreature:
                    x, y = row * self.upscaleFactor, col * self.upscaleFactor
                    center = (y + self.upscaleFactor // 2, x + self.upscaleFactor // 2)
                    cv2.circle(blankImage, center, self.upscaleFactor // 2, color=(0, 0, 255), thickness=-1)

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
