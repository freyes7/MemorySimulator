class Memory:

	def __init__(self, realMemorySize, swapMemorySize, pageSize):
		self.realMemorySize = realMemorySize
		self.swapMemorySize = swapMemorySize
		self.pageSize = pageSize
		self.realMemory = []
		self.swapMemory = []
		for i in range(realMemorySize*1024/pageSize):
			realMemory.append(Page(0,0))
		for i in range(swapMemorySize*1024/pageSize):
			swapMemory.append(Page(0,0))

	def loadProcess(self, process, processSize):
		pass

	def accessAddress(self, address, process, modifyBit):
		pass

	def freeProcess(self, process):
		pass