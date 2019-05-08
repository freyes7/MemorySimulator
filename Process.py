from Page import Page

class Process:

    frames = []
    def __init__(self, size, pageSize):
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