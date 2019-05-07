from Memory import Memory
class MemoryLIFO(Memory):

	def __init__(self, realMSize, swapMSize, pSize):
		Memory.__init__(self,realMSize, swapMSize, pSize)
                self.pages = self.pageSize

        def loadProcess(self, process, processSize):
                return ''

        def accessAddress(self, address, process, modifyBit):
                return ''

        def freeProcess(self, process):
                return ''

