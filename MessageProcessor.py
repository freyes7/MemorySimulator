class MessageProcessor:

	@staticmethod
	def setRealMemorySize(data):
	    command = data.split()
	    if len(command)<2 : 
	        return 0,0,'\nInsuficientes parametros'
	    if command[0] != 'RealMemory': 
	        return 0,0,'\nEl comando no es el esperado, intenta de nuevo.'
	    try:
	        realMemorySize = int(command[1])
	    except ValueError:
	        return 0,0,'\nIngresa un entero para el tamanio de la memoria'
	    return realMemorySize,1,'\nEl tamanio de la memoria se cambio con exito'

	@staticmethod
	def setSwapMemorySize(data):
	    command = data.split()
	    if len(command)<2 : 
	        return 0,0,'\nInsuficientes parametros'
	    if command[0] != 'SwapMemory': 
	        return 0,0,'\nEl comando no es el esperado, intenta de nuevo.'
	    try:
	        swapMemorySize = int(command[1])
	    except ValueError:
	        return 0,0,'\nIngresa un entero para el tamanio de la memoria'
	    return swapMemorySize,1,'\nEl tamanio de la memoria se cambio con exito'

	@staticmethod
	def setPageSize(data):
	    command = data.split()
	    if len(command)<2 : 
	        return 0,0,'\nInsuficientes parametros'
	    if command[0] != 'PageSize': 
	        return 0,0,'\nEl comando no es el esperado, intenta de nuevo.'
	    try:
	        pageSize = int(command[1])
	    except ValueError:
	        return 0,0,'\nIngresa un entero para el tamanio de las paginas'
	    return pageSize,1,'\nEl tamanio de las paginas se cambio con exito'

	@staticmethod
	def setPolitic(data):
	    command = data.split()
	    if len(command)>=1 and command[0] == 'E': 
	        return '',2,'\nHasta Luego'
	    if len(command)<2 : 
	        return '',0,'\nInsuficientes parametros'
	    if command[0] != 'PoliticaMemory': 
	        return '',0,'\nEl comando no es el esperado, intenta de nuevo.'
	    if command[1] != 'FIFO' and command[1] != 'LIFO':
	        return '',0,'\nDicha Politica no es manejada por el programa'
	    return command[1],1,'\nLa politica de remplazo se cambio con exito'

	@staticmethod
	def instruction(data):
	    command = data.split()
	    if len(command)>=1 and command[0]=='F':
	        return -1,'\nElige la nueva politica de remplazo o ingresa E para terminar'
	    return 0,'\nError'