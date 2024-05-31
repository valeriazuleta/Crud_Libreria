clientes = [
    [3100, 'juan'],
    [3101, 'maria'],
    [3102, 'pedro'],
    [3103, 'laura']
]

libros = [
    [12552, 'iliada', 5300, 25],
    [12553, 'platero', 2500, 16],
    [12554, 'Cien', 3600, 35]
]

ventas = [
    ('V-1020', 3100, 12552, 4, 21200),
    ('V-1025', 3103, 12554, 2, 5000),
    ('V-1030', 3100, 12554, 3, 10800),
    ('V-1035', 3101, 12553, 9, 22500)
]


def menu_principal():
    while True:
        print(" ")
        print("---Menu Principal---")
        print("1. Clientes")
        print("2. Libros")
        print("3. Ventas")
        print("4. Estadisticas")
        print("5. Salir")
        print()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            menu_clientes()
        elif opcion == 2:
            menu_libros()
        elif opcion == 3:
            menu_ventas()
        elif opcion == 4:
            menu_estadistica()
        elif opcion == 5:
            print("Ha salido exitosamente.")
            break
        else:
            print("Ingrese una opción válida.")

def menu_clientes():
    while True:
        print(" ")
        print("---Clientes---")
        print("1. Ingresar Clientes")
        print("2. Lista de Clientes")
        print("3. Actualizar Cliente")
        print("4. Buscar Cliente")
        print("5. Eliminar Cliente")
        print("6. Volver a Menu Principal")
        print()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            ingresar_cliente()
        elif opcion == 2:
            lista_clientes()
        elif opcion == 3:
            actualizar_cliente()
        elif opcion == 4:
            buscar_cliente()
        elif opcion == 5:
            eliminar_cliente()
        elif opcion == 6:
            break
        else:
            print("Ingrese una opción válida.")

def ingresar_cliente():
    codigo = int(input("Ingrese el código del cliente: "))
 
    nombre = input("Ingrese el nombre del cliente: ")
    
    # Validar si el cliente ya existe
    for cliente in clientes:
        if cliente[0] == codigo:
            print("El cliente ya existe.")
            return
    #Agrega cliente a la lista 
    cliente = [codigo, nombre]
    clientes.append(cliente)
    print("Cliente ingresado correctamente.")


def lista_clientes():
    print("---Lista de Clientes---")
    for cliente in clientes:
        codigo, nombre = cliente
        print("Código:", codigo ,"Nombre:", nombre )
        print("-----------------------")

def actualizar_cliente():
    codigo = int(input("Ingrese el código del cliente a actualizar: "))
    encontrado = False
    for cliente in clientes:
        if cliente[0] == codigo:
            nombre = input("Ingrese el nuevo nombre del cliente: ")
            cliente[1] = nombre
            encontrado = True
            print("Cliente actualizado correctamente.")
            break
    if not encontrado:
        print("Cliente no encontrado.")

def buscar_cliente():
    codigo = int(input("Ingrese el código del cliente a buscar: "))
    encontrado = False
    for cliente in clientes:
        if cliente[0] == codigo:
            print("Cliente encontrado:")
            print("Código:", cliente[0] , "Nombre:", cliente[1])
            encontrado = True
            break
    if not encontrado:
        print("Cliente no encontrado.")

def eliminar_cliente():
    codigo = int(input("Ingrese el código del cliente a eliminar: "))
    encontrado = False
    for cliente in clientes:
        if cliente[0] == codigo:
            clientes.remove(cliente)
            encontrado = True
            print("Cliente eliminado correctamente.")
            break
    if not encontrado:
        print("Cliente no encontrado.")

def menu_libros():
    while True:
        print(" ")
        print("---Libros---")
        print("1. Ingresar Libro")
        print("2. Lista de Libros")
        print("3. Actualizar Libro")
        print("4. Buscar Libro")
        print("5. Eliminar Libro")
        print("6. Volver a Menu Principal")
        print()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            ingresar_libro()
        elif opcion == 2:
            lista_libros()
        elif opcion == 3:
            actualizar_libro()
        elif opcion == 4:
            buscar_libro()
        elif opcion == 5:
            eliminar_libro()
        elif opcion == 6:
            break
        else:
            print("Ingrese una opción válida.")

def menu_libros():
    while True:
        print(" ")
        print("---Libros---")
        print("1. Ingresar Libro")
        print("2. Lista de Libros")
        print("3. Actualizar Libro")
        print("4. Buscar Libro")
        print("5. Eliminar Libro")
        print("6. Volver a Menu Principal")
        print()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            ingresar_libro()
        elif opcion == 2:
            lista_libros()
        elif opcion == 3:
            actualizar_libro()
        elif opcion == 4:
            buscar_libro()
        elif opcion == 5:
            eliminar_libro()
        elif opcion == 6:
            break
        else:
            print("Ingrese una opción válida.")

def ingresar_libro():
    codigo = int(input("Ingrese el código del libro: "))
    titulo = input("Ingrese el título del libro: ")
    precio = float(input("Ingrese el precio del libro: "))
    stock = int(input("Ingrese la cantidad en stock del libro: "))
    
    # Validar si el libro ya existe
    for libro in libros:
        if libro[0] == codigo:
            print("El libro ya existe.")
            return
    
    libro = [codigo, titulo, precio, stock]
    libros.append(libro)
    print("Libro ingresado correctamente.")

def lista_libros():
    print("---Lista de Libros---")
    for libro in libros:
        print("Código:", libro[0] , "Título:", libro[1] , "Precio:", libro[2] , "Stock:", libro[3])
        print("--------------------")

#def actualizar_libro():
    #codigo = int(input("Ingrese el código del libro a actualizar: "))
    
    # Buscar el libro
    #for libro in libros:
        #if libro[0] == codigo:
            #print("Libro encontrado:")
            #print("Código:", libro[0])
            #print("Título:", libro[1])
            #print("Precio:", libro[2])
            #print("Stock:", libro[3])
            #print("--------------------")
            
            #nuevo_precio = float(input("Ingrese el nuevo precio del libro: "))
            #nuevo_stock = int(input("Ingrese la nueva cantidad en stock del libro: "))
            
            #libro[2] = nuevo_precio
            #libro[3] = nuevo_stock
            
            #print("Libro actualizado correctamente.")
            #return
    
    #print("Libro no encontrado.")

def actualizar_libro():
    codigo = int(input("Ingrese el código del libro a actualizar: "))

    # Buscar el libro
    for libro in libros:
        if libro[0] == codigo:
            print("Libro encontrado:")
            print("Código:", libro[0])
            print("Título:", libro[1])
            print("Precio:", libro[2])
            print("Stock:", libro[3])
            print("--------------------")

            opcion = input("¿Desea actualizar el título? (s/n): ")
            if opcion.lower() == 's':
                nuevo_titulo = input("Ingrese el nuevo título del libro: ")
                libro[1] = nuevo_titulo

            opcion = input("¿Desea actualizar el código? (s/n): ")
            if opcion.lower() == 's':
                nuevo_codigo = int(input("Ingrese el nuevo código del libro: "))
                libro[0] = nuevo_codigo

            opcion = input("¿Desea actualizar el precio? (s/n): ")
            if opcion.lower() == 's':
                nuevo_precio = float(input("Ingrese el nuevo precio del libro: "))
                libro[2] = nuevo_precio

            opcion = input("¿Desea actualizar el stock? (s/n): ")
            if opcion.lower() == 's':
                nuevo_stock = int(input("Ingrese la nueva cantidad en stock del libro: "))
                libro[3] = nuevo_stock

            print("Libro actualizado correctamente.")
            return

    print("Libro no encontrado.")


def buscar_libro():
    codigo = int(input("Ingrese el código del libro a buscar: "))
    
    # Buscar el libro
    for libro in libros:
        if libro[0] == codigo:
            print("Libro encontrado:")
            print("Código:", libro[0])
            print("Título:", libro[1])
            print("Precio:", libro[2])
            print("Stock:", libro[3])
            print("--------------------")
            return
    
    print("Libro no encontrado.")

def eliminar_libro():
    codigo = int(input("Ingrese el código del libro a eliminar: "))
    
    # Buscar el libro
    for libro in libros:
        if libro[0] == codigo:
            libros.remove(libro)
            print("Libro eliminado correctamente.")
            return
    
    print("Libro no encontrado.")

def menu_ventas():
    while True:
        print(" ")
        print("---Ventas---")
        print("1. Realizar Venta")
        print("2. Lista de Ventas")
        print("3. Actualizar Venta")
        print("4. Buscar Venta")
        print("5. Eliminar Venta")
        print("6. Volver a Menu Principal")
        print()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            realizar_venta()
        elif opcion == 2:
            lista_ventas()
        elif opcion == 3:
            actualizar_venta()
        elif opcion == 4:
            buscar_venta()
        elif opcion == 5:
            eliminar_venta()
        elif opcion == 6:
            break
        else:
            print("Ingrese una opción válida.")   

def realizar_venta():
    # obtengo el ultimo codigo venta existente 
    ultimo_codigo_venta = int(ventas[-1][0].split('-')[1]) if ventas else 1015

    #genero el nuevo codigo de venta
    nuevo_codigo_venta = f"V-{ultimo_codigo_venta + 5}"

    codigo_cliente = int(input("Ingrese el código del cliente: "))

    # Buscar cliente
    cliente_encontrado = None
    for cliente in clientes:
        if cliente[0] == codigo_cliente:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        print("Cliente no encontrado.")
        return

    codigo_libro = int(input("Ingrese el código del libro: "))

    # Buscar libro
    libro_encontrado = None
    for libro in libros:
        if libro[0] == codigo_libro:
            libro_encontrado = libro
            break

    if libro_encontrado is None:
        print("Libro no encontrado.")
        return

    cantidad = int(input("Ingrese la cantidad vendida: "))

    # Validar cantidad vendida
    if cantidad <= 0:
        print("Cantidad no válida. Ingrese una cantidad mayor a 0.")
        return

    # Verificar disponibilidad de cantidad en inventario
    if cantidad > libro_encontrado[3]:
        print("No hay suficientes cantidades en el inventario.")
        return

    precio_unitario = libro_encontrado[2]
    subtotal = precio_unitario * cantidad

    nueva_venta = (nuevo_codigo_venta, codigo_cliente, codigo_libro, cantidad, subtotal)
    ventas.append(nueva_venta)

    print("Venta realizada correctamente.")

    # Actualizar cantidades de libros en el inventario
    libro_encontrado[3] -= cantidad

    # Incrementar el código de venta en 5 unidades y actualizar las cantidades de libros
    #incremento_codigo_venta = 5
    #for libro in libros:
     #   libro[0] += incremento_codigo_venta

def lista_ventas():
    print("---Lista de Ventas---")
    if len(ventas) == 0:
        print("No hay ventas registradas.")
    else:
        for venta in ventas:
            print("Código de venta:", venta[0] , "Código de cliente:", venta[1] , "Código de libro:", venta[2] , "Cantidad:", venta[3] , "Subtotal:", venta[4])
            print("--------------------")

def actualizar_venta():
    codigo_venta = input("Ingrese el código de la venta que desea actualizar: ")

    for i, venta in enumerate(ventas):
        if venta[0] == codigo_venta:
            venta_encontrada = venta
            indice_venta = i
            break
    else:
        print("Venta no encontrada")
        return

    print("Información actual de la venta:")
    print("Código de venta:", venta_encontrada[0])
    print("Código de cliente:", venta_encontrada[1])
    print("Código de libro:", venta_encontrada[2])
    print("Cantidad:", venta_encontrada[3])
    print("Subtotal:", venta_encontrada[4])

    while True:
        print("\nOpciones de actualización:")
        print("1. Actualizar código de cliente")
        print("2. Actualizar código de libro")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Salir")
        
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            nuevo_codigo_cliente = input("Ingrese el nuevo código de cliente: ")
            if not cliente_existe(nuevo_codigo_cliente):
                print("El código de cliente no existe. Intente nuevamente.")
                continue
            venta_encontrada = (venta_encontrada[0], nuevo_codigo_cliente, venta_encontrada[2], venta_encontrada[3], venta_encontrada[4])
            print("Código de cliente actualizado.")
        elif opcion == 2:
            nuevo_codigo_libro = input("Ingrese el nuevo código de libro: ")
            if not libro_existe(nuevo_codigo_libro):
                print("El libro no existe. Intente nuevamente.")
                continue
            venta_encontrada = (venta_encontrada[0], venta_encontrada[1], nuevo_codigo_libro, venta_encontrada[3], venta_encontrada[4])
            print("Código de libro actualizado.")
        elif opcion == 3:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            codigo_libro = venta_encontrada[2]
            if not validar_cantidad_disponible(codigo_libro, nueva_cantidad):
                print("No hay suficientes cantidades disponibles en el inventario.")
                continue
            venta_encontrada = (venta_encontrada[0], venta_encontrada[1], venta_encontrada[2], nueva_cantidad, venta_encontrada[4])
            print("Cantidad actualizada.")
        elif opcion == 4:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            venta_encontrada = (venta_encontrada[0], venta_encontrada[1], venta_encontrada[2], venta_encontrada[3], nuevo_precio)
            print("Precio actualizado.")
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Ingrese una opción válida.")

    ventas[indice_venta] = venta_encontrada
    print("Venta actualizada correctamente.")

    while True:
        respuesta = input("¿Desea actualizar algo más en esta venta? (S/N): ")
        if respuesta.upper() == 'S':
            while True:
                print("\nOpciones de actualización:")
                print("1. Actualizar código de cliente")
                print("2. Actualizar código de libro")
                print("3. Actualizar cantidad")
                print("4. Actualizar precio")
                print("5. Salir")
                
                opcion = int(input("Ingrese una opción: "))

                if opcion == 1:
                    nuevo_codigo_cliente = input("Ingrese el nuevo código de cliente: ")
                    if not cliente_existe(nuevo_codigo_cliente):
                        print("El código de cliente no existe. Intente nuevamente.")
                        continue
                    venta_encontrada = (venta_encontrada[0], nuevo_codigo_cliente, venta_encontrada[2], venta_encontrada[3], venta_encontrada[4])
                    print("Código de cliente actualizado.")
                elif opcion == 2:
                    nuevo_codigo_libro = input("Ingrese el nuevo código de libro: ")
                    if not libro_existe(nuevo_codigo_libro):
                        print("El libro no existe. Intente nuevamente.")
                        continue
                    venta_encontrada = (venta_encontrada[0], venta_encontrada[1], nuevo_codigo_libro, venta_encontrada[3], venta_encontrada[4])
                    print("Código de libro actualizado.")
                elif opcion == 3:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    codigo_libro = venta_encontrada[2]
                    if not validar_cantidad_disponible(codigo_libro, nueva_cantidad):
                        print("No hay suficientes cantidades disponibles en el inventario.")
                        continue
                    venta_encontrada = (venta_encontrada[0], venta_encontrada[1], venta_encontrada[2], nueva_cantidad, venta_encontrada[4])
                    print("Cantidad actualizada.")
                elif opcion == 4:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    venta_encontrada = (venta_encontrada[0], venta_encontrada[1], venta_encontrada[2], venta_encontrada[3], nuevo_precio)
                    print("Precio actualizado.")
                elif opcion == 5:
                    break
                else:
                    print("Opción inválida. Ingrese una opción válida.")

            ventas[indice_venta] = venta_encontrada
            print("Venta actualizada correctamente.")
        elif respuesta.upper() == 'N':
            break
        else:
            print("Respuesta inválida. Intente nuevamente.")




def buscar_venta():
    codigo_venta = input("Ingrese el código de la venta a buscar: ")

    # Buscar la venta
    venta_encontrada = None
    for venta in ventas:
        if venta[0] == codigo_venta:
            venta_encontrada = venta
            break

    if venta_encontrada is None:
        print("Venta no encontrada.")
    else:
        print("Venta encontrada:")
        print("Código de venta:", venta_encontrada[0])
        print("Código de cliente:", venta_encontrada[1])
        print("Código de libro:", venta_encontrada[2])
        print("Cantidad:", venta_encontrada[3])
        print("Subtotal:", venta_encontrada[4])
        print("--------------------")

def eliminar_venta():
    codigo_venta = input("Ingrese el código de la venta a eliminar: ")

    # Buscar la venta
    venta_encontrada = None
    for venta in ventas:
        if venta[0] == codigo_venta:
            venta_encontrada = venta
            break

    if venta_encontrada is None:
        print("Venta no encontrada.")
        return

    ventas.remove(venta_encontrada)
    print("Venta eliminada correctamente.")

def cliente_existe(codigo_cliente):
    for cliente in clientes:
        if cliente[0] == codigo_cliente:
            return True
    return False

def libro_existe(codigo_libro):
    for libro in libros:
        if libro[0] == codigo_libro:
            return True
    return False

def validar_cantidad_disponible(codigo_libro, cantidad):
    for libro in libros:
        if libro[0] == codigo_libro:
            if libro[3] >= cantidad:
                return True
            else:
                return False
    return False 

def menu_estadistica():
    while True:
        print(" ")
        print("------")
        print("1. Ventas Totales por ISBN")
        print("2. Libros Más y Menos Vendidos")
        print("3. Venta Total de la Librería")
        print("4. Cliente con Mayor Compra por Venta")
        print("5. Cliente con Mayor Volumen de Compra Total")
        print("6. Volver a Menu Principal")
        print()
        opcion = input("Ingrese una opción: ")


        if opcion == "1":
            ventas_totales_por_isbn()

        elif opcion == "2":
            libros_mas_menos_vendidos()
            
        elif opcion == "3":
            venta_total_libreria()
            
        elif opcion == "4":
            cliente_mayor_compra_venta()
            
        elif opcion == "5":
            cliente_mayor_volumen_compra_total()
            
        elif opcion == "6":
            return
        else:
            print("Opción inválida, por favor intente de nuevo.")
#def ventas_totales_por_isbn():
 #   isbn = input("Ingrese el ISBN del libro: ")

   # total_ventas = 0
    #for venta in ventas:
     #   if venta[2] == isbn:
      #      total_ventas += venta[3]  # Sumar la cantidad de la venta

    #print("Ventas totales del libro con ISBN", isbn, ":", total_ventas)

def ventas_totales_por_isbn():
    isbn = input("Ingrese el ISBN: ")
    ventas_totales = 0

    for venta in ventas:
        if str(venta[2]) == str(isbn):
            ventas_totales += venta[3]

    print("Ventas totales para el ISBN", isbn, ":", ventas_totales)


def libros_mas_menos_vendidos():
    libros_vendidos = {}

    # Calcular la cantidad de ventas para cada libro
    for venta in ventas:
        isbn = venta[2]
        cantidad = venta[3]
        if isbn in libros_vendidos:
            libros_vendidos[isbn] += cantidad
        else:
            libros_vendidos[isbn] = cantidad

    # Encontrar el libro más vendido
    libro_mas_vendido = max(libros_vendidos, key=libros_vendidos.get)
    cantidad_mas_vendida = libros_vendidos[libro_mas_vendido]

    # Encontrar el libro menos vendido
    libro_menos_vendido = min(libros_vendidos, key=libros_vendidos.get)
    cantidad_menos_vendida = libros_vendidos[libro_menos_vendido]

    print("Libro más vendido:")
    print("ISBN:", libro_mas_vendido)
    print("Cantidad vendida:", cantidad_mas_vendida)
    print()

    print("Libro menos vendido:")
    print("ISBN:", libro_menos_vendido)
    print("Cantidad vendida:", cantidad_menos_vendida)

def venta_total_libreria():
    total_ventas = sum(venta[3] for venta in ventas)  # Sumar todas las cantidades de venta
    print("Venta total de la librería:", total_ventas)

def cliente_mayor_compra_venta():
    cliente_mayor_compra = None
    monto_mayor_compra = 0

    for venta in ventas:
        codigo_cliente = venta[1]
        subtotal = venta[4]

        if subtotal > monto_mayor_compra:
            monto_mayor_compra = subtotal
            cliente_mayor_compra = codigo_cliente

    print("Cliente con la mayor compra por venta:")
    print("Código de cliente:", cliente_mayor_compra)
    print("Monto de compra:", monto_mayor_compra)

def cliente_mayor_volumen_compra_total():
    clientes_compras = {}

    # Calcular el volumen de compra para cada cliente
    for venta in ventas:
        codigo_cliente = venta[1]
        subtotal = venta[4]

        if codigo_cliente in clientes_compras:
            clientes_compras[codigo_cliente] += subtotal
        else:
            clientes_compras[codigo_cliente] = subtotal

    # Encontrar el cliente con mayor volumen de compra total
    cliente_mayor_compra_total = max(clientes_compras, key=clientes_compras.get)
    monto_mayor_compra_total = clientes_compras[cliente_mayor_compra_total]

    print("Cliente con el mayor volumen de compra total:")
    print("Código de cliente:", cliente_mayor_compra_total)
    print("Monto total de compra:", monto_mayor_compra_total)

def mostrar_menu_principal():
    while True:
        print(" ")
        print("----- Menu Principal -----")
        print("1. Clientes")
        print("2. Libros")
        print("3. Ventas")
        print("4. Estadísticas")
        print("5. Salir")
        print()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_libros()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            menu_estadistica()
        elif opcion == "5":
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")



menu_principal()