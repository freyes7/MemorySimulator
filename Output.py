from tabulate import tabulate
from Page import Page
from Process import Process
import copy
import operator

#clase para imprimir las tablas con los valor del estado de los procesos y la mamoria
class Output:

	#inicializacion de las vatiables globales
	global lastRealList
	global lastSwapList
	global commandTableRows
	global faultTableRows

	# Static Row Lists
	commandTableRows = []
	faultTableRows = []


	lastRealList = []
	lastSwapList = []

	# Headers
	#se inicializan los encabezados de la tabla
	@staticmethod
	def resetTableRows():
		global commandTableRows
		global faultTableRows
		global lastRealList
		global lastSwapList
		commandTableRows = [["Tiempo","comando","dir. real","M","S","Terminados"]]
		faultTableRows = []
		lastRealList = []
		lastSwapList = []

	#se agrega la colmna de fallos de pagina
	@staticmethod
	def addFaultRow(process):
		global faultTableRows

		pid = process.getId() #se obtiene el id del proceso
		turnaround = process.getTurnaroundTime() #se obtiene el calor del turnaround
		pageFaults = process.getPageFaults() #se obiene la cantidad de fallos de pagina
		swapins = process.getSwapIn() #se obtienen los
		swapouts = process.getSwapOut() #se obtienen los 
		rendimiento = str(process.getPerformance()) #se obtiene el valor del rendimiento
		#se agregan los valores a la fila
		faultTableRows.append([pid, turnaround, pageFaults, swapins, swapouts, rendimiento])

	#metodo para agregar un falo a un proceso que no ha terminado
	@staticmethod
	def addFaultRowNotEndedProcess(process):
		global faultTableRows

		pid = process.getId() #se obtiene el id del proceso
		turnaround = "-" #no ha terminado, así que aún no tiene turnaround
		pageFaults = process.getPageFaults() #se obtienen los fallos de pagina
		swapins = process.getSwapIn() #se obtienen los
		swapouts = process.getSwapOut() #se obtienen los
		rendimiento = str(process.getPerformance()) #se obtiene el valor del rendimiento
		#se agregan los valores a la fila
		faultTableRows.append([pid, turnaround, pageFaults, swapins, swapouts, rendimiento])

	#metodo para insertar valores en la fila de comandos
	@staticmethod
	def addCommandRow(tiempo, commandName, dirReal, realList, swapList, finished):
		global lastRealList
		global lastSwapList
		global commandTableRows

		MList = []
		SList = []

		#Solo se ejecuta si antes las listas estaban vacias
		if(len(lastRealList) == 0 and len(lastSwapList) == 0):
			MList.append("M[" + str(len(realList)) + ":L]")
			SList.append("S[" + str(len(swapList)) + ":L]")
			
			#se repite para cada valor en la lista de 
			for i in range(len(realList)):
				lastRealList.append(Page(realList[i].getTypeMemory(), realList[i].getProcess(), realList[i].getLinkedPage()))

			#se repite para cada valor en la lista de 
			for i in range(len(swapList)):
				lastSwapList.append(Page(swapList[i].getTypeMemory(), swapList[i].getProcess(), swapList[i].getLinkedPage()))
			
			commandTableRows.append([tiempo, commandName, dirReal, ', '.join(MList), ', '.join(SList), ', '.join(finished)])
			return ""

		#se actualixza el tamaño de las listas
		sizeRealList = len(realList)
		sizeSwapList = len(swapList)

		# Real Lists

		tmpMinFreeIndex = 0
		freeOrEqual = "" # F | E

		#para todos los que se encuentren en la lista
		for i in range(sizeRealList):
			#print "RPL<", realList[i].getProcess() ,"> RPA<", lastRealList[i].getProcess() ,"> | ROL<", realList[i].getOcupyNumber() ,"> RON<", lastRealList[i].getOcupyNumber() ,"> | RLL<", realList[i].getLinkedPage() ,"> RLN<", lastRealList[i].getLinkedPage() ,">"
			#Si todos los valores coinciden
			if (realList[i].getProcess() == lastRealList[i].getProcess()) and (realList[i].getOcupyNumber() == lastRealList[i].getOcupyNumber()) and (realList[i].getLinkedPage() == realList[i].getLinkedPage()):
				# EQUAL
				#Si esta libre
				if(freeOrEqual == "F"):
					if(i-tmpMinFreeIndex > 1):
						MList.append("M[" + str(tmpMinFreeIndex) + "-" + str(i-1) + ":L]")
					else:
						MList.append("M[" + str(tmpMinFreeIndex) + ":L]")
					tmpMinFreeIndex = i
				
				freeOrEqual = "E"

				if(i == sizeRealList-1):
					MList.append("=")
				
			else:
				# UNIQUE & DIFFERENT
				
				if(realList[i].getOcupyNumber() > 0):
					
					
					if(freeOrEqual == "F"):
						if(i-tmpMinFreeIndex > 1):
							MList.append("M[" + str(tmpMinFreeIndex) + "-" + str(i-1) + ":L]")
						else:
							MList.append("M[" + str(tmpMinFreeIndex) + ":L]")
					elif(freeOrEqual == "E"):
						MList.append("=")
					tmpMinFreeIndex = 0
					freeOrEqual = ""

					MList.append("M[" + str(i) + ":" + str(realList[i].getProcess()) + "," + str(realList[i].getLinkedPage()) + "]")
					
				# FREE
				else:
					
					#si está igual se imprime =
					if(freeOrEqual == "E"):
						MList.append("=")
						tmpMinFreeIndex = 0

					#si no esta libre 
					if(freeOrEqual != "F"):
						freeOrEqual = "F"
						tmpMinFreeIndex = i					
					
					#si es el ultimo valor de la lista
					if(i == sizeRealList-1):
						if(i-tmpMinFreeIndex > 1):
							MList.append("M[" + str(tmpMinFreeIndex) + "-" + str(i-1) + ":L]")
						else:
							MList.append("M[" + str(tmpMinFreeIndex) + ":L]")
					
			lastRealList[i] = Page(realList[i].getTypeMemory(), realList[i].getProcess(), realList[i].getLinkedPage())
			lastRealList[i].setOcupyNumber(realList[i].getOcupyNumber())

		# Swap Lists

		tmpMinFreeIndex = 0
		freeOrEqual = "" # F | E

		for i in range(sizeSwapList):
			#print "SPL<", swapList[i].getProcess() ,"> SPA<", lastSwapList[i].getProcess() ,"> | SOL<", swapList[i].getOcupyNumber() ,"> SON<", swapList[i].getOcupyNumber() ,"> | SLL<", swapList[i].getLinkedPage() ,"> SLN<", lastSwapList[i].getLinkedPage() ,">"
			if (swapList[i].getProcess() == lastSwapList[i].getProcess()) and (swapList[i].getOcupyNumber() == lastSwapList[i].getOcupyNumber()) and (swapList[i].getLinkedPage() == lastSwapList[i].getLinkedPage()):
				# EQUAL
				
				if(freeOrEqual == "F"):
					if(i-tmpMinFreeIndex > 1):
						SList.append("S[" + str(tmpMinFreeIndex) + "-" + str(i-1) + ":L]")
					else:
						SList.append("S[" + str(tmpMinFreeIndex) + ":L]")
					tmpMinFreeIndex = i
				
				freeOrEqual = "E"

				if(i == sizeSwapList-1):
					SList.append("=")

			else:
				# UNIQUE & DIFFERENT
				
				if(swapList[i].getOcupyNumber() > 0):
					if(freeOrEqual == "F"):
						if(i-tmpMinFreeIndex > 1):
							SList.append("S[" + str(tmpMinFreeIndex) + "-" + str(i-1) + ":L]")
						else:
							SList.append("S[" + str(tmpMinFreeIndex) + ":L]")
					elif(freeOrEqual == "E"):
						SList.append("=")
					tmpMinFreeIndex = 0
					freeOrEqual = ""

					SList.append("S[" + str(i) + ":" + str(swapList[i].getProcess()) + "," + str(swapList[i].getLinkedPage()) + "]")
					
				# FREE
				else:
					
					if(freeOrEqual == "E"):
						SList.append("=")
						tmpMinFreeIndex = 0
					
					freeOrEqual = "F"
					if(i == sizeSwapList-1):
						if(i-tmpMinFreeIndex > 1):
							SList.append("S[" + str(tmpMinFreeIndex) + "-" + str(i-1) + ":L]")
						else:
							SList.append("S[" + str(tmpMinFreeIndex) + ":L]")
					

			lastSwapList[i] = Page(swapList[i].getTypeMemory(), swapList[i].getProcess(), swapList[i].getLinkedPage())
			lastSwapList[i].setOcupyNumber(swapList[i].getOcupyNumber())
				

		commandTableRows.append([str(tiempo), str(commandName), str(dirReal), ',\n'.join(MList), ',\n'.join(SList), ', '.join(str(tmp1) for tmp1 in finished)])

	#metodo para desplegar la tabla de fallos
	@staticmethod
	def displayFaultsTable():
		global faultTableRows
		#se ordenan los valores
		faultTableRows = sorted(faultTableRows, key=operator.itemgetter(0),reverse=True)
		#se agregan los encabezados de la tabla
		faultTableRows.append(["proceso","turnaround","# page faults","swapins","swapouts","rendimiento"])

		#se imprime la tabla
		print tabulate(faultTableRows[::-1],headers="firstrow",tablefmt="fancy_grid"),"\n"

	#metodo para desplegar la tabla final de comandos
	@staticmethod
	def displayCommandsTableLast():
		global commandTableRows
		#se imprime la tabla
		print tabulate([["Tiempo","comando","dir. real","M","S","Terminados"],commandTableRows[len(commandTableRows)-1]],headers="firstrow",tablefmt="fancy_grid"),"\n"

	#metodo para desplegar la tabla de comandos
	@staticmethod
	def displayCommandsTable():
		global commandTableRows
		print tabulate(commandTableRows,headers="firstrow",tablefmt="fancy_grid"),"\n"