from Page import Page

class Process:

    def __init__(self, size, pageSize):
        self.size = size
        self.pageSize = pageSize
        self.frames = []
        self.numberOfFrames = size/pageSize
        if numberOfFrames*pageSize<size:
            numberOfFrames = numberOfFrames + 1
        for i in range(numberOfFrames):
            frames.append(Page(0,0))