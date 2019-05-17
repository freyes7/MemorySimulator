from Page import Page
import time

#clase para configurar un proceso
class Process:

    #metodo de inicializacion de los procesos
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

    #metodo para obtener los fallos de pagina
    def getPageFaults(self):
        return self.pageFaults

    #metodo para obtener el tamaño de la pagina
    def getPageSize(self):
        return self.pageSize
        
    #metodo que regresa
    def getSwapIn(self):
        return self.swapIn

    #metodo que regresa
    def getSwapOut(self):
        return self.swapOut

    #metodo que regresa los frames
    def getFrames(self):
        return self.frames

    #metodo que regresa un frame esecifico
    def getFrame(self, index):
        return self.frames[index]

    #metodo que regresa el tamaño del proceso
    def getSize(self):
        return self.size

    #metodo que regresa la cantidad de frames de proceso
    def getNumberOfFrames(self):
        return self.numberOfFrames

    #metodo que regresa el id del proceso
    def getId(self):
        return self.id

    #metodo que regresa el turnarround del proceso
    def getTurnaroundTime(self):
        return time.time()-self.initialTime

    #metodo para agregar un fallo de pagina al proceso
    def addFault(self):
        self.pageFaults = self.pageFaults + 1

    #metodo para agregar
    def addSwapIn(self):
        self.swapIn = self.swapIn + 1

    #metodo para agregar
    def addSwapOut(self):
        self.swapOut = self.swapOut + 1

    #metodo para agregar un nuevo comando
    def addCommand(self):
        self.commandCount = self.commandCount + 1

    #metodo para obtener el rndimiento del proceso
    def getPerformance(self):
        #print "P<",self.id,"> Faults<",self.pageFaults,"> Commands<",self.commandCount,">"
        try:#se calcula el procentage de exito del proceso
            return 1.0 - float(self.pageFaults)/float(self.commandCount)
        except:#si no hubo fallos se regresa el total (1.0)
            return 1.0

    #metodo para definir
    def setLinkedPage(self, index, linkedPage):
        self.frames[index].setLinkedPage(linkedPage)

    #se define el tipo de memoria que usará el proceso
    def setTypeMemory(self, index, typeMemory):
        self.frames[index].setTypeMemory(typeMemory)