from model.world import World, CellData

import numpy as np
import cv2

class VideoRenderer:
    def __init__(self) -> None:
        self.inMemoryFrames = list()

    def saveFrame(self, world: World):
        blank_image = np.ones((world.worldSize, world.worldSize, 3), dtype=np.uint8) * 255

        for row in reversed(range(world.worldSize)):
            for col in range(world.worldSize):
                if world.cells[row][col].isCreature:
                    x, y = row, col
                    cv2.circle(blank_image, (y, x), radius = 1, color=(0, 0, 255), thickness=-1)

        # Save the image
        self.inMemoryFrames.append(blank_image.copy())

    def createVideo(self, name: str):
        height, width, _ = self.inMemoryFrames[0].shape
        size = (width, height)

        out = cv2.VideoWriter(name+'.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

        for i in range(len(self.inMemoryFrames)):
            resized_frame = cv2.resize(self.inMemoryFrames[i], size, interpolation=cv2.INTER_NEAREST)
            out.write(resized_frame)

        out.release()

    def clearFrames(self):
        self.inMemoryFrames.clear()
