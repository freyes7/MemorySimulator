from Page import Page
from Process import Process
from collections import deque

class Memory:


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

	'''
	def pri(self):
		print("Real")
		for page in self.realMemory:
			print(str(page.getOcupyNumber())+' '+str(page.getProcess())+' '+str(page.getLinkedPage()))
		print("Swap")
		for page in self.swapMemory:
			print(str(page.getOcupyNumber())+' '+str(page.getProcess())+' '+str(page.getLinkedPage()))
	'''

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

	def releaseRealMemoryFrame(self):
		index = 0
		while self.realMemory[index].getOcupyNumber() == 0:
			index = index + 1
		if self.politic == 'FIFO':
			for i in range(index,self.realMemoryFrames):
				if self.realMemory[i].getOcupyNumber() < self.realMemory[index].getOcupyNumber():
					index = i
		elif self.politic == 'LIFO':
			for i in range(index,self.realMemoryFrames):
				if self.realMemory[i].getOcupyNumber() > self.realMemory[index].getOcupyNumber():
					index = i
		self.toSwap(index)

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

	def safeLoading(self,processNumber):
		j = 0
		process = self.processesInMemory[processNumber]
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

	def loadProcess(self, process, processSize):
		if process in self.freedProcesses or process in self.processesInMemory or process in self.processesInQueue:
			return '\nEl proceso ya se ha usado anteriormente'
		framesNeeded = processSize/self.pageSize
		if framesNeeded*self.pageSize < processSize:
			framesNeeded = framesNeeded + 1
		if framesNeeded > self.realMemoryFrames + self.swapMemoryFrames:
			return '\nLa memoria requerida es mayor que la total'
		newProcess = Process(process, processSize, self.pageSize)
		if framesNeeded > self.freeRealMemoryFrames + self.freeSwapMemoryFrames:
			self.queueProcess.append(newProcess)
			self.processesInQueue.add(process)
			return '\nProceso esperando liberacion de memoria'
		self.processesInMemory[process] = newProcess
		self.safeLoading(newProcess.getId())
		return '\nProceso cargado con exito'

	def accessAddress(self, address, process, modifyBit):
		return ' '

	def freeProcess(self, process):

		if process in self.processesInMemory:
			processToDelete = self.processesInMemory[process]
			framesToDelete = processToDelete.getFrames()
			for frame in framesToDelete:
				index = frame.getLinkedPage()
				if frame.getTypeMemory() == 'SwapMemory':
					self.swapMemory[index].setOcupyNumber(0)
					self.freeSwapMemoryFrames = self.freeSwapMemoryFrames + 1
				elif frame.getTypeMemory() == 'RealMemory':
					self.realMemory[index].setOcupyNumber(0)
					self.freeRealMemoryFrames = self.freeRealMemoryFrames + 1
			self.freedProcesses.add(process)
			del self.processesInMemory[process]

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
			return '\nProceso eliminado con exito'

		return '\nNo existe dicho proceso en memoria'