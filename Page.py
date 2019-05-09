class Page:

    def __init__(self, typeMemory, process, linkedPage):
        self.ocupyNumber = 0
        self.typeMemory = typeMemory
        self.process = process
        self.linkedPage = linkedPage

    def getTypeMemory(self):
        return self.typeMemory

    def getProcess(self):
        return self.process

    def getLinkedPage(self):
        return self.linkedPage

    def getOcupyNumber(self):
        return self.ocupyNumber

    def setProcess(self, process):
        self.process = process

    def setLinkedPage(self, linkedPage):
        self.linkedPage = linkedPage

    def setOcupyNumber(self, value):
        self.ocupyNumber = value
    
    def setTypeMemory(self, typeMemory):
        self.typeMemory = typeMemory