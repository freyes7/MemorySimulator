class Memory:

	def __init__(self, realMemorySize, swapMemorySize, pageSize):
		self.realMemorySize = realMemorySize
		self.swapMemorySize = swapMemorySize
		self.pageSize = pageSize

	def loadProcess(self, process, processSize):
		pass

	def accessAddress(self, address, process, modifyBit):
		pass

	def freeProcess(self, process):
		pass