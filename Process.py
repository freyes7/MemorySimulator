from Page import Page
import time

class Process:

    def __init__(self, id, size, pageSize):
    	self.frames = []
    	self.commandCount = 0
    	self.initialTime = time.time()
        self.pageFaults = 0
        self.swapIn = 0
        self.swapOut = 0
        self.id = id
        self.size = size
        self.pageSize = pageSize
        self.numberOfFrames = size/pageSize
        if self.numberOfFrames*pageSize<size:
            self.numberOfFrames = self.numberOfFrames + 1
        for i in range(self.numberOfFrames):
            self.frames.append(Page('Undefined',id,0))

    def getPageFaults(self):
        return self.pageFaults

    def getPageSize(self):
        return self.pageSize
        
    def getSwapIn(self):
        return self.swapIn

    def getSwapOut(self):
        return self.swapOut

    def getFrames(self):
        return self.frames

    def getFrame(self, index):
        return self.frames[index]

    def getSize(self):
        return self.size

    def getNumberOfFrames(self):
        return self.numberOfFrames

    def getId(self):
        return self.id

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
        print "P<",self.id,"> Faults<",self.pageFaults,"> Commands<",self.commandCount,">"
        try:
            return 1.0 - float(self.pageFaults)/float(self.commandCount)
        except:
            return 1.0

    def setLinkedPage(self, index, linkedPage):
        self.frames[index].setLinkedPage(linkedPage)

    def setTypeMemory(self, index, typeMemory):
        self.frames[index].setTypeMemory(typeMemory)