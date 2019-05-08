class Page:

    ocupyBit = 0
    def __init__(self, typeMemory, process, linkedPage):
        self.typeMemory = typeMemory
        self.process = process
        self.linkedPage = linkedPage

    def getTypeMemory(self):
        return self.typeMemory

    def getProcess():
        return self.process

    def getLinkedPage():
        return self.linkedPage

    def setOcupyBit(self, value):
        self.ocupyBit = value