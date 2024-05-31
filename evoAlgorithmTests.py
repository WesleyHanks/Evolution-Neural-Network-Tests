import math, random, sys

class Unit:

    def __init__(self, x=0, y=0, NNMultipliers=[0,0,0,0,0,0,0,0], NNBiases=[0,0,0,0,0,0,0,0,0,0]):
        self.x = x
        self.y = y
        self.NNMultipliers = NNMultipliers
        self.NNBiases = NNBiases

    def getNNOutput(self):
        moveUp = ((self.x * self.NNMultipliers[0]) - self.NNBiases[0]) + ((self.y * self.NNMultipliers[5]) - self.NNBiases[5])
        moveDown = ((self.x * self.NNMultipliers[1]) - self.NNBiases[1]) + ((self.y * self.NNMultipliers[6]) - self.NNBiases[6])
        moveRight = ((self.x * self.NNMultipliers[2]) - self.NNBiases[2]) + ((self.y * self.NNMultipliers[7]) - self.NNBiases[7])
        moveLeft = ((self.x * self.NNMultipliers[3]) - self.NNBiases[3]) + ((self.y * self.NNMultipliers[8]) - self.NNBiases[8])

        if moveUp >= moveDown and moveUp >= moveLeft and moveUp >= moveRight:
            self.y += 1
        elif moveDown >= moveLeft and moveDown >= moveRight:
            