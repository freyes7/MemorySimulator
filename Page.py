class Page:

    def __init__(self, typeMemory, process, linkedPage):
        self.ocupyBit = 0
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