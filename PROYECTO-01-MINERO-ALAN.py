#========================================================
# LifeStore
#========================================================
# Programa para el análisis de ventas de la tienda virtual
#========================================================

#--------------------------------------------------------
# Menú principal
#--------------------------------------------------------

	# Usuarios registrados como administradores
	# Usuario, Contraseña
	# admins = [['Javier', '123'], ['Emtech', 'Digital'], ['Alan', '555']]

# Muestra el menú por pantalla y lee una opción de teclado.
# La opción se debe encontrar entre 1 y 3.
admin = 0
while admin == 0: # Bucle que permite regresar al menú
	print('*** TIENDA VIRTUAL LIFESTORE ***')
	print('1) Iniciar sesión')
	print('2) Crear nuevo usuario')
	print('3) Salir')
	print()

	opcion = int(input('Seleccione una opción: '))
	while opcion < 1 or opcion > 3:
		opcion = int(input('Escoge una opción entre 1 y 3: '))

#--------------------------------------------------------
# Inicio de sesión
#--------------------------------------------------------

	# Usuarios registrados como administradores
	# Usuario, Contraseña
	admins = [['Javier', '123'], ['Emtech', 'Digital'], ['Alan', '555']]
	clientes = []

	if opcion == 1: # Opción Iniciar Sesión
		user = input('Usuario: ')
		password = input('Contraseña: ')

		for usuario in admins:
			if usuario[0] == user and usuario[1] == password:
				print('Bienvenido,', usuario[0] + '.',
				 'Has ingresado como ADMINISTRADOR.')
				print()
				admin = 1
				break
		else:
			print('**Usuario no registrado**')
			print()

	elif opcion == 2: # Opción Crear nuevo usuario
		new_user = input('Nuevo Usuario: ')
		new_password = input('Contraseña: ')
		clientes.append([new_user, new_password])
		for usuario in clientes:
			if usuario[0] == new_user and usuario[1] == new_password:
				print('Bienvenido,', usuario[0] + '.', 
					  'Has creado un usuario con el rol de CLIENTE.')
				print()
				admin = 1
				break

		else: # Opción Salir
			print()
			print('Adiós. Vuelve pronto.')
			quit()

#--------------------------------------------------------
# Menú de productos
#--------------------------------------------------------

# Importar los datos del archivo lifestore_file
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

lifestore_sales_copy = lifestore_sales[:]

main_menu = 1

if admin == 1:
	while main_menu == 1:
# Muestra el menú por pantalla y lee una opción de teclado.
# La opción se debe encontrar entre 1 y 7.
		print('*** HAS INGRESADO COMO:', usuario[0] + ' ***')
		print('1) Productos más vendidos:')
		print('2) Productos más buscados:')
		print('3) Productos con menos ventas:')
		print('4) Productos con menos búsquedas:')
		print('5) Mejores reseñas:')
		print('6) Peores reseñas')
		print('7) Salir')
		print()

		opcion = int(input('Seleccione una opción: '))
		while opcion < 1 or opcion > 7:
			opcion = int(input('Escoge una opción entre 1 y 7: '))

		if opcion == 1: # Productos más vendidos
			print()
			print('*** LOS 50 PRODUCTOS MÁS VENDIDOS ***')
			print()

			contador = 0
			total_ventas = [] # [[id, nombre_producto, contador]]

			for producto in lifestore_products: 
				for ventas in lifestore_sales:
					if producto[0] == ventas[1]: # producto[0]->id_producto, venta[1]->id_producto
						contador += 1
					
				formato = [contador, producto[0], producto[1]] # Ventas | Id | Producto
				total_ventas.append(formato)
				contador = 0

			ventas_ordenado = []
			while total_ventas:
				maximo = total_ventas[0][0]
				lista_actual = total_ventas[0]
				for venta_counter in total_ventas:
					if venta_counter[0] > maximo:
						maximo = venta_counter[0]
						lista_actual = venta_counter
				ventas_ordenado.append(lista_actual)
				total_ventas.remove(lista_actual)

			main_menu = 1

			print('| No. Ventas |   Id   |						 Producto 						|')
			for idx in range(0, 43):
				print('|\t', ventas_ordenado[idx][0], '     |\t',     ventas_ordenado[idx][1],
				  	'   |\t',						 ventas_ordenado[idx][2], '|')
				print()

		elif opcion == 2: # Productos con mayores búsquedas
			print()
			print('*** LOS 100 PRODUCTOS MÁS BUSCADOS ***')
			print()

			contador = 0
			total_busquedas = []

			for producto in lifestore_products: 
				for busquedas in lifestore_searches:
					if producto[0] == busquedas[1]:
						contador += 1
					
				formato = [contador, producto[0], producto[1]] # Búsquedas | Id | Producto
				total_busquedas.append(formato)
				contador = 0

			busquedas_ordenado = []
			while total_busquedas:
				maximo = total_busquedas[0][0]
				lista_actual = total_busquedas[0]
				for busquedas_counter in total_busquedas:
					if busquedas_counter[0] > maximo:
						maximo = busquedas_counter[0]
						lista_actual = busquedas_counter
				busquedas_ordenado.append(lista_actual)
				total_busquedas.remove(lista_actual)

			main_menu = 1

			print('| No. Búsquedas |   Id   |						 Producto 						|')
			for idx in range(0, 56):
				print('|\t', busquedas_ordenado[idx][0], '     |\t',     busquedas_ordenado[idx][1],
				  	'   |\t',						 busquedas_ordenado[idx][2], '|')
				print()


		# elif opcion == 2: # Productos por reseña en el servicio
		# 	print('Productos por reseña en el servicio')

		elif opcion == 3:
			print()
			print('*** LOS 50 PRODUCTOS CON MENOS VENTAS ***')
			print()

			contador = 0
			total_ventas = [] # [[id, nombre_producto, contador]]

			for producto in lifestore_products: 
				for ventas in lifestore_sales:
					if producto[0] == ventas[1]: # producto[0]->id_producto, venta[1]->id_producto
						contador += 1
					
				formato = [contador, producto[3], producto[1]] # Ventas | Id | Producto
				total_ventas.append(formato)
				contador = 0

			ventas_ordenado = []

			while total_ventas:
				minimo = total_ventas[0][0]
				lista_actual = total_ventas[0]
				for venta_counter in total_ventas:
					if venta_counter[0] < minimo:
						minimo = venta_counter[0]
						lista_actual = venta_counter
				ventas_ordenado.append(lista_actual)
				total_ventas.remove(lista_actual)

			main_menu = 1
				
			print('| No. Ventas |   Categoría   |						 Producto 						|')
			for idx in range(0, 51):
				print('|\t', ventas_ordenado[idx][0], '     |\t',     ventas_ordenado[idx][1],
				  	'   |\t',						 ventas_ordenado[idx][2], '|')
				print()

		# elif opcion == 3:
		# 	print('Total de ingresos y ventas promedio mensuales')

		elif opcion == 4:
			print()
			print('*** LOS 50 PRODUCTOS CON MENOS BUSQUEDAS ***')
			print()

			contador = 0
			total_busquedas = []

			for producto in lifestore_products: 
				for busquedas in lifestore_searches:
					if producto[0] == busquedas[1]:
						contador += 1
					
				formato = [contador, producto[3], producto[1]] # Búsquedas | Id | Producto
				total_busquedas.append(formato)
				contador = 0

			busquedas_ordenado = []

			while total_busquedas:
				minimo = total_busquedas[0][0]
				lista_actual = total_busquedas[0]
				for busquedas_counter in total_busquedas:
					if busquedas_counter[0] < minimo:
						minimo = busquedas_counter[0]
						lista_actual = busquedas_counter
				busquedas_ordenado.append(lista_actual)
				total_busquedas.remove(lista_actual)

			main_menu = 1

			print('| No. Búsquedas |   Categoría   |						 Producto 						|')
			for idx in range(0, 51):
				print('|\t', busquedas_ordenado[idx][0], '     |\t',     busquedas_ordenado[idx][1],
				  	'   |\t',						 busquedas_ordenado[idx][2], '|')
				print()

		elif opcion == 5:
			print()
			print('*** MEJORES RESEÑAS ***')
			print()
	 		
			for ventas in lifestore_sales:
				main_menu = 1
				score_ordenado = []

				while lifestore_sales:
					maximo = lifestore_sales[0][2]
					lista_actual = lifestore_sales[0]
					for score_counter in lifestore_sales:
						if score_counter[2] > maximo:
							maximo = score_counter[2]
							lista_actual = score_counter
					score_ordenado.append(lista_actual)
					lifestore_sales.remove(lista_actual)

				print('| Calificación |   Devoluciones   |	 Id   |')
				for idx in range(0, 21):
					print('|\t', score_ordenado[idx][2], '\t\t   |\t\t', score_ordenado[idx][4],
					  	'\t\t  | ', score_ordenado[idx][1], '\t  |')
					print()
					
		elif opcion == 6:
			print()
			print('*** PEORES RESEÑAS ***')
			print()
	 
			for ventas in lifestore_sales_copy:
				main_menu = 1
				score_ordenado = []

				while lifestore_sales_copy:
					minimo = lifestore_sales_copy[0][2]
					lista_actual = lifestore_sales_copy[0]
					for score_counter in lifestore_sales_copy:
						if score_counter[2] < minimo:
							minimo = score_counter[2]
							lista_actual = score_counter
					score_ordenado.append(lista_actual)
					lifestore_sales_copy.remove(lista_actual)

				print('| Calificación |   Devoluciones   |	 Id   |')
				for idx in range(0, 21):
					print('|\t', score_ordenado[idx][2], '\t\t   |\t\t', score_ordenado[idx][4],
					  	'\t\t  | ', score_ordenado[idx][1], '\t  |')
					print()
					

		elif opcion == 7:
			print()
			print('Adiós. Vuelve pronto.')
			quit()



elif admin == 0:
	for cliente in clientes:
		if cliente[0] == new_user and cliente[1] == new_password:
			print('*** HAS INGRESADO COMO:', cliente[0] + ' ***')
			print()
			print('Esta tipo de cuenta no permite visualizar esta información.')
			print('Intenta con una cuenta de administrador.')