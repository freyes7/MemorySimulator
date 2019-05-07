from Memory import Memory
class MemoryLIFO(Memory):

	def __init__(self, realMSize, swapMSize, pSize):
		Memory.__init__(self,realMSize, swapMSize, pSize)
                self.pages = self.pageSize

        def loadProcess(self, process, processSize):
                pass

        def accessAddress(self, address, process, modifyBit):
                pass

        def freeProcess(self, process):
                pass

