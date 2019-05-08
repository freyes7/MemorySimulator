from Page import Page

class Memory:


	def __init__(self, realMemorySize, swapMemorySize, pageSize):
		self.processesInMemory = {}
		self.freedProcesses = {}
		self.realMemorySize = realMemorySize
		self.swapMemorySize = swapMemorySize
		self.pageSize = pageSize
		self.realMemory = []
		self.swapMemory = []
		for i in range(realMemorySize*1024/pageSize):
			self.realMemory.append(Page('RealMemory',0,0))
		for i in range(swapMemorySize*1024/pageSize):
			self.swapMemory.append(Page('SwapMemory',0,0))

	def loadProcess(self, process, processSize):
		pass

	def accessAddress(self, address, process, modifyBit):
		pass

	def freeProcess(self, process):

		if process in self.processesInMemory:
			processToDelete = self.processesInMemory[process]
			framesToDelete = processToDelete.getFrames()
			for frame in framesToDelete:
				index = frame.getLinkedPage
				if frame.getTypeMemory == 'SwapMemory':
					self.swapMemory[index].setOcupyBit(0)
				elif frame.getTypeMemory == 'RealMemory':
					self.realMemory[index].setOcupyBit(0)
			self.freedProcesses.add(process)
			del self.processesInMemory[process]
			return '\nProceso eliminado con exito'

		return '\nNo existe dicho proceso en memoria'