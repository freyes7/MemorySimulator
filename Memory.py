from Page import Page

class Memory:


	processesInMemory = {}
	def __init__(self, realMemorySize, swapMemorySize, pageSize):
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
		if str(process) in processesInMemory:
			processToDelete = processesInMemory[str(process)]
			for process in processToDelete:
