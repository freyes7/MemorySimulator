from Page import Page
import time

class Process:

    def __init__(self, size, pageSize):
	self.frames = []
	self.commandCount = 0
	self.initialTime = time.time()
        self.pageFaults = 0
        self.swapIn = 0
        self.swapOut = 0
        self.size = size
        self.pageSize = pageSize
        self.numberOfFrames = size/pageSize
        if self.numberOfFrames*pageSize<size:
            self.numberOfFrames = numberOfFrames + 1
        for i in range(numberOfFrames):
            self.frames.append(Page('Undefined',0,0))

    def getPageFaults(self):
        return self.pageFaults

    def getSwapIn(self):
        return self.swapIn

    def getSwapOut(self):
        return self.swapOut

    def getFrames(self):
        return self.frames

    def getFrame(self, index):
        return self.frames[index]

    def getTurnaroundTime(self):
	return time.time()-self.initialTime

    def addFault(self):
	self.pageFaults = self.pageFaults + 1

    def addSwapIn(self):
	self.swapIn = self.swapIn + 1

    def addSwapOut(self):
	self.swapOut = self.swapOut + 1

    def addCommand(self):
	self.commandCount = self.commandCount + 1

    def getPerformance(self):
	return 1 - self.pageFaults/self.commandCount
