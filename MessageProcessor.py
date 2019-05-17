#clase para procesar los mensajes que recibe el servidor
class MessageProcessor:

	#metodo para definir el tamaño de la memoria real
	@staticmethod
	def setRealMemorySize(data):
	    command = data.split()
	    if len(command)<2 : #si el comando no tiene los argumentos necesarios
	        return 0,0,'\nInsuficientes parametros'
	    if command[0] != 'RealMemory': #si el comando no corresponde con lo que se quiere ejecutar
	        return 0,0,'\nEl comando no es el esperado, intenta de nuevo.'
	    try: #se asigna el valor de la memoria real
	        realMemorySize = int(command[1])
	    except ValueError: #si no se recibió un valor numerico
	        return 0,0,'\nIngresa un entero para el tamanio de la memoria'
		if realMemorySize <= 0: #si tratan de ingresar un valor negativo
			return 0,0,'Ingresa un numero positivo'
		#cuando ya se obtuvieron argumentos valido se imprime
	    return realMemorySize,1,'\nEl tamanio de la memoria se cambio con exito'

	#metodo para definir el tamaño del tamaño de
	@staticmethod
	def setSwapMemorySize(data):
	    command = data.split()
	    if len(command)<2 : #si no tiene los argumentos necesarios
	        return 0,0,'\nInsuficientes parametros'
	    if command[0] != 'SwapMemory': #si el comando no corresponde con lo que se quiere ejecutar
	        return 0,0,'\nEl comando no es el esperado, intenta de nuevo.'
	    try: #se asigna el valor del tamaño de 
	        swapMemorySize = int(command[1])
	    except ValueError: #si no se recibió un valor numerico
	        return 0,0,'\nIngresa un entero para el tamanio de la memoria'
		if swapMemorySize <= 0: #si tratan de ingresar un valor negativo
			return 0,0,'Ingresa un numero positivo'
		#cuando ya se obtuvieron argumentos valido se imprime
	    return swapMemorySize,1,'\nEl tamanio de la memoria se cambio con exito'

	#metodo para definir el tamaño de pagina
	@staticmethod
	def setPageSize(realMemorySize,data):
	    command = data.split()
	    if len(command)<2 : #si no tiene los argumentos necesarios
	        return 0,0,'\nInsuficientes parametros'
	    if command[0] != 'PageSize': #si el comando no corresponde con lo que se quiere ejecutar 
	        return 0,0,'\nEl comando no es el esperado, intenta de nuevo.'
	    try: #se asigna el valor del tamaño de 
	        pageSize = int(command[1])
	    except ValueError: #si no se recibió un valor numerico
	        return 0,0,'\nIngresa un entero para el tamanio de las paginas'
		if pageSize <= 0: #si tratan de ingresar un valor negativo
			return 0,0,'\nIngresa un numero positivo'
		if realMemorySize*1024<pageSize: # si el valor que se busca asignar es superior al de los marcos
			return 0,0,'\nEl tamanio de pagina debe ser menor o igual al tamanio de la memoria real'
		#cuando ya se obtubieron argumentos valido se imprime
	    return pageSize,1,'\nEl tamanio de las paginas se cambio con exito'

	#metodo para establecer la palitica a utlizar
	@staticmethod
	def setPolitic(data):
	    command = data.split()
	    if len(command)>=1 and command[0] == 'E': #si se tiene al menos un comando y es el comando E
	        return '',2,'\nHasta Luego'
	    if len(command)<2 :  #si no tiene los argumentos necesarios
	        return '',0,'\nInsuficientes parametros'
	    if command[0] != 'PoliticaMemory': #si el comando no corresponde con lo que se quiere ejecutar
	        return '',0,'\nEl comando no es el esperado, intenta de nuevo.'
	    if command[1] != 'FIFO' and command[1] != 'LIFO': #si no se recibe alguna de las políticas soportadas
	        return '',0,'\nDicha Politica no es manejada por el programa'
	    #cuando ya se obtuvo una política correcta
	    return command[1],1,'\nLa politica de remplazo se cambio con exito'

	#metodo para recibir una nueva instrucción
	@staticmethod
	def instruction(data):
	    command = data.split()
	    values = []
	    if len(command)==0: #si no se recibieron valores
	    	return 0,values,'\nInsuficientes parametros'
	    if command[0]=='F': #cuando se recibe el comando F
	        return -1,values,'F'
	    if command[0]=='C': #cuando se recibe el comando C
	    	return 0,values,'C'
	    if command[0]=='P': #cuando se recibe el comando P para cargar un proceso
	    	if len(command)<3: #cuando se recibe P si todos sus valores
	    		return 0,values,'\nInsuficientes parametros'
	    	try: #se agrega el valor en bytes del proceso
	        	values.append(int(command[1]))
	        except ValueError: #si no se recibió un valor numerico
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
			if values[0] <= 0: #si tratan de ingresar un valor negativo
				return 0,values,'Ingresa un numero positivo'
	    	try: #se agrega el valor del identificador del proceso
	        	values.append(int(command[2]))
	        except ValueError: #si no se recibió un valor numerico
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
	    	#se regresa lo recibido 
	    	return 0,values,'P'
	    if command[0]=='A': #cuando se recibe el comando A para accesar a la direccion virtual de un proceso
	    	if len(command)<4: #cuando no se reciben todos los argumentos
	    		return 0,values,'\nInsuficientes parametros'
	    	try: #se trata de guadar el valor "d" de la dirección virtual del proceso
		        values.append(int(command[1]))
	        except ValueError: #cuando no se recibe un valor entero
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
			if values[0] < 0 : #cuando se recibe un valor negativo
				return 0,values,'Ingresa un numero positivo o 0'
	    	try:
	        	values.append(int(command[2]))
	        except ValueError:
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
	    	try: #se trata de guadar el valor "p" del proceso
	        	values.append(int(command[3]))
	        except ValueError: #cuando no se recibe un valor entero
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
	    	#se regresa lo recibido 
	    	return 0,values,'A'
	    if command[0]=='L': #cuando se recibe el comando L para liberar paginas
	    	if len(command)<2: #si no se reciben todos los argumentos
	    		return 0,values,'\nInsuficientes parametros'
	    	try: #se trata de guardar el valor p del proceso
	        	values.append(int(command[1]))
	        except ValueError: #cuando no se recibe un valor entero
		        return 0,values,'\nLos parametros de este comando deben ser enteros'
	    	#se regresa lo recibido 
	    	return 0,values,'L'
	    #cuando no se recibe un de los comandos posibles
	    return 0,values,'\nEl comando no es el esperado, intenta de nuevo.'