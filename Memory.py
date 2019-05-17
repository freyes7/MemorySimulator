from Page import Page            #To import the 
from Process import Process
from collections import deque
from Output import Output

#clase para poder hacer manejo de la memoria que se simula
class Memory:

	#metodo de inicialización de la memoria
	def __init__(self, realMemorySize, swapMemorySize, pageSize, politic):
		self.processesInMemory = {}
		self.freedProcesses = set()
		self.processesInQueue = set()
		self.queueProcess = deque()
		self.realMemorySize = realMemorySize
		self.swapMemorySize = swapMemorySize
		self.pageSize = pageSize
		self.politic = politic
		self.realMemory = []
		self.swapMemory = []
		self.realMemoryFrames = realMemorySize*1024/pageSize
		self.swapMemoryFrames = swapMemorySize*1024/pageSize
		self.freeRealMemoryFrames = self.realMemoryFrames
		self.freeSwapMemoryFrames = self.swapMemoryFrames
		self.enterIndex = 0
		for i in range(self.realMemoryFrames):
			self.realMemory.append(Page('RealMemory',0,0))

		for i in range(self.swapMemoryFrames):
			self.swapMemory.append(Page('SwapMemory',0,0))

	
	def pri(self):
		print("Real")
		for page in self.realMemory:
			print(str(page.getOcupyNumber())+' '+str(page.getProcess())+' '+str(page.getLinkedPage()))
		print("Swap")
		for page in self.swapMemory:
			print(str(page.getOcupyNumber())+' '+str(page.getProcess())+' '+str(page.getLinkedPage()))
		

	#metodo para hacer un intercambio en la memoria
	def toSwap(self,index):
		newIndex = 0
		while self.swapMemory[newIndex].getOcupyNumber() != 0:
			newIndex = newIndex + 1
		self.swapMemory[newIndex].setProcess(self.realMemory[index].getProcess())
		self.swapMemory[newIndex].setLinkedPage(self.realMemory[index].getLinkedPage())
		self.swapMemory[newIndex].setOcupyNumber(1)
		self.processesInMemory[self.realMemory[index].getProcess()].setLinkedPage(self.realMemory[index].getLinkedPage(),newIndex)
		self.processesInMemory[self.realMemory[index].getProcess()].setTypeMemory(self.realMemory[index].getLinkedPage(),'SwapMemory')
		self.realMemory[index].setOcupyNumber(0)
		self.freeRealMemoryFrames = self.freeRealMemoryFrames + 1
		self.freeSwapMemoryFrames = self.freeSwapMemoryFrames - 1

		self.processesInMemory[self.realMemory[index].getProcess()].addSwapIn()

	#metodo para liberar un frame de memoria
	def releaseRealMemoryFrame(self):
		index = 0
		while self.realMemory[index].getOcupyNumber() == 0:
			index = index + 1
		if self.politic == 'FIFO': #si se usa FIFO
			for i in range(index,self.realMemoryFrames): #para cada frame de la memoria
				if self.realMemory[i].getOcupyNumber()>0 and self.realMemory[i].getOcupyNumber() < self.realMemory[index].getOcupyNumber():
					index = i
		elif self.politic == 'LIFO': #si se usa LIFO
			for i in range(index,self.realMemoryFrames): #para cada frame de la memoria
				if self.realMemory[i].getOcupyNumber() > self.realMemory[index].getOcupyNumber():
					index = i
		self.toSwap(index)

	#metodo para cargar la memoria real
	def loadRealMemory(self, processNumber, lowerBound, upperBound):
		i = 0
		while lowerBound <= upperBound:
			while self.realMemory[i].getOcupyNumber() != 0:
				i = i + 1
			self.enterIndex = self.enterIndex + 1
			self.realMemory[i].setOcupyNumber(self.enterIndex)
			self.freeRealMemoryFrames = self.freeRealMemoryFrames - 1
			self.processesInMemory[processNumber].setLinkedPage(lowerBound,i)
			self.processesInMemory[processNumber].setTypeMemory(lowerBound,'RealMemory')
			self.realMemory[i].setProcess(processNumber)
			self.realMemory[i].setLinkedPage(lowerBound)
			lowerBound = lowerBound + 1
			i = i + 1

	#metodo para cargar un proceso
	def safeLoading(self,processNumber):
		j = 0
		process = self.processesInMemory[processNumber] #se accede al proceso
		while process.getNumberOfFrames() - j > self.realMemoryFrames:
			limit = self.realMemoryFrames - self.freeRealMemoryFrames
			for i in range(limit):
				self.releaseRealMemoryFrame()
			self.loadRealMemory(processNumber,j, j + self.realMemoryFrames - 1)
			j = j + self.realMemoryFrames
		if process.getNumberOfFrames() - j > self.freeRealMemoryFrames:
			pagesToFree = process.getNumberOfFrames() - j - self.freeRealMemoryFrames
			for i in range(pagesToFree):
				self.releaseRealMemoryFrame()
		self.loadRealMemory(processNumber,j, process.getNumberOfFrames() - 1)
		#print("P")
		#print(processNumber)
		#self.pri()

	#metodo que carga un proceso a la memoria
	def loadProcess(self, process, processSize):
		#si el proceso está la lista de libres o en memoria o en cola
		if process in self.freedProcesses or process in self.processesInMemory or process in self.processesInQueue:
			return '\nEl proceso ya se ha usado anteriormente'
		framesNeeded = processSize/self.pageSize #se calcula la cantidad de frames necesarios
		if framesNeeded*self.pageSize < processSize: #si cantidad frames por el tamaño de las paginas es menor a lo requerido
			framesNeeded = framesNeeded + 1
		if framesNeeded > self.realMemoryFrames + self.swapMemoryFrames: #si se requieren más frames que los existentes
			return '\nLa memoria requerida es mayor que la total'
		newProcess = Process(process, processSize, self.pageSize) #se crea un nuevo proceso
		if framesNeeded > self.freeRealMemoryFrames + self.freeSwapMemoryFrames: #si se requiere más memoria que la libre
			self.queueProcess.append(newProcess)
			self.processesInQueue.add(process)
			return '\nProceso esperando liberacion de memoria'
		self.processesInMemory[process] = newProcess
		self.safeLoading(newProcess.getId())
		#cuando se termina de cargar el proceso
		return '\nProceso cargado con exito'

	#metodo que permite acceder a una dirección
	def accessAddress(self, address, processNumber, modifyBit):
		if processNumber in self.processesInMemory: #si el proceso se encuentra en la memoria
			self.processesInMemory[processNumber].addCommand()
			process = self.processesInMemory[processNumber] #se accede al proceso
			if address >= process.getSize(): #si la direccion solicitada está fuera del espacio del proceso
				return '\nPage Fault','-'
			frame = address / process.getPageSize() #se calcula el numero de frame
			displacement = address % process.getPageSize() #se calcula el desplazamiento en el frame
			page = process.getFrame(frame) #se obtiene la pagina a partir del valor de frame
			if page.getTypeMemory() == 'SwapMemory': #si el proceso se encuentra en memoria virtual
				self.processesInMemory[processNumber].addFault()
				self.processesInMemory[processNumber].addSwapOut()
				self.swapMemory[page.getLinkedPage()].setOcupyNumber(0)
				self.freeSwapMemoryFrames = self.freeSwapMemoryFrames + 1
				if self.freeRealMemoryFrames == 0:
					self.releaseRealMemoryFrame()
				self.loadRealMemory(processNumber,frame,frame)
			realMemory = self.processesInMemory[processNumber].getFrame(frame).getLinkedPage() * self.pageSize + displacement
			#self.pri()
			return '\nReal Memory ' + str(realMemory), str(realMemory)
		#si no se encuentra el proceso en la memoria
		return '\nNo existe dicho proceso en memoria', "-"

	#metodo para liberar un proceso de la memoria
	def freeProcess(self, process):

		#si el proceso se encuentra actualmente en memoria
		if process in self.processesInMemory:
			processToDelete = self.processesInMemory[process]#se accede al proceso que se eliminará
			framesToDelete = processToDelete.getFrames() #se obtienen los frames de ese proceso
			Output.addFaultRow(processToDelete) #se agrega a la fila de fallas
			for frame in framesToDelete: #para cada frame del proceso
				index = frame.getLinkedPage()
				if frame.getTypeMemory() == 'SwapMemory': #si el procesos está en la mememoria virtual
					self.swapMemory[index].setOcupyNumber(0)
					self.freeSwapMemoryFrames = self.freeSwapMemoryFrames + 1
				elif frame.getTypeMemory() == 'RealMemory': #si el proceso está en la memoria real
					self.realMemory[index].setOcupyNumber(0)
					self.freeRealMemoryFrames = self.freeRealMemoryFrames + 1
			self.freedProcesses.add(process)
			del self.processesInMemory[process] #se elimina el proceso que ha sido liberado

			#print("L")
			#print(process)
			#self.pri()

			while self.queueProcess:
				newProcess = self.queueProcess.popleft()
				if newProcess.getNumberOfFrames() <= self.freeRealMemoryFrames + self.freeSwapMemoryFrames:
					self.processesInMemory[newProcess.getId()] = newProcess
					self.safeLoading(newProcess.getId())
				else:
					self.queueProcess.appendleft(newProcess)
					break
			#cuando se termina de eliminar el proceso
			return '\nProceso eliminado con exito'

		#cuando no existe el proceso que se desea eliminar
		return '\nNo existe dicho proceso en memoria'
	
	#metodo para guardar un comentario
	def saveComment(self,data):
		return '\nComentario Guardado'

	#metodo para terminar la simulación de la memoria
	def endSimulation(self):
		for key in self.processesInMemory:#para cada proceso en la memoria
			Output.addFaultRowNotEndedProcess(self.processesInMemory[key])
			self.freedProcesses.add(key)
		for key in self.processesInQueue:
			self.freedProcesses.add(key)
		return '\nHasta Luego'