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
		if realMemorySize <= 0:
			return 0,0,'Ingresa un numero positivo'
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
		if swapMemorySize <= 0:
			return 0,0,'Ingresa un numero positivo'
	    return swapMemorySize,1,'\nEl tamanio de la memoria se cambio con exito'

	@staticmethod
	def setPageSize(realMemorySize,data):
	    command = data.split()
	    if len(command)<2 : 
	        return 0,0,'\nInsuficientes parametros'
	    if command[0] != 'PageSize': 
	        return 0,0,'\nEl comando no es el esperado, intenta de nuevo.'
	    try:
	        pageSize = int(command[1])
	    except ValueError:
	        return 0,0,'\nIngresa un entero para el tamanio de las paginas'
		if pageSize <= 0:
			return 0,0,'\nIngresa un numero positivo'
		if realMemorySize*1024<pageSize:
			return 0,0,'\nEl tamanio de pagina debe ser menor o igual al tamanio de la memoria real'
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
	    values = []
	    if len(command)==0:
	    	return 0,values,'\nInsuficientes parametros'
	    if command[0]=='F':
	        return -1,values,'F'
	    if command[0]=='C':
	    	return 0,values,'C'
	    if command[0]=='P':
	    	if len(command)<3:
	    		return 0,values,'\nInsuficientes parametros'
	    	try:
	        	values.append(int(command[1]))
	        except ValueError:
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
			if values[0] <= 0:
				return 0,values,'Ingresa un numero positivo'
	    	try:
	        	values.append(int(command[2]))
	        except ValueError:
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
	    	return 0,values,'P'
	    if command[0]=='A':
	    	if len(command)<4:
	    		return 0,'\nInsuficientes parametros'
	    	try:
		        values.append(int(command[1]))
	        except ValueError:
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
			if values[0] < 0 :
				return 0,values,'Ingresa un numero positivo o 0'
	    	try:
	        	values.append(int(command[2]))
	        except ValueError:
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
	    	try:
	        	values.append(int(command[3]))
	        except ValueError:
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
	    	return 0,values,'A'
	    if command[0]=='L':
	    	if len(command)<2:
	    		return 0,'\nInsuficientes parametros'
	    	try:
	        	values.append(int(command[1]))
	        except ValueError:
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
	    	return 0,values,'L'
	    return 0,values,'\nEl comando no es el esperado, intenta de nuevo.'