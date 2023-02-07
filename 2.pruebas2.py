
nueva_lista = [2,4,6,"Mexico"]

for elemento in nueva_lista:
	try:
		print(elemento/2)
	except:
		print('No es un numero')