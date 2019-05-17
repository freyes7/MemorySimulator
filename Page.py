#clase que define el diseño de las paginas que se usaran en la memoria
class Page:

    #metodo de inicialización de las paginas
    def __init__(self, typeMemory, process, linkedPage):
        self.ocupyNumber = 0
        self.typeMemory = typeMemory
        self.process = process
        self.linkedPage = linkedPage

    #metodo que regresa el tipo de memoria que usa la pagina
    def getTypeMemory(self):
        return self.typeMemory

    #metodo que regresa el proceso que contiene a la pagina
    def getProcess(self):
        return self.process

    #metodo que regresa
    def getLinkedPage(self):
        return self.linkedPage

    #metodo que regresa
    def getOcupyNumber(self):
        return self.ocupyNumber

    #metodo para definir el proceso al que pertenece
    def setProcess(self, process):
        self.process = process

    #metodo para definir
    def setLinkedPage(self, linkedPage):
        self.linkedPage = linkedPage

    #metodo para definir
    def setOcupyNumber(self, value):
        self.ocupyNumber = value
    
    #metodo para definir el tipo de memoria
    def setTypeMemory(self, typeMemory):
        self.typeMemory = typeMemory