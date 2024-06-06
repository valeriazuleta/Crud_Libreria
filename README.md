# Crud_Libreria
### Descripción del Proyecto: Gestión de Librería

Este proyecto es un sistema de gestión de librerías desarrollado en Python, que permite administrar clientes, libros y ventas, así como generar estadísticas relevantes para el negocio. El sistema está diseñado para ejecutarse en consola y ofrece un menú interactivo para facilitar la navegación y el uso de las funcionalidades.

#### Funcionalidades Principales

1. **Gestión de Clientes**
    - **Ingresar Clientes**: Permite agregar nuevos clientes a la lista.
    - **Lista de Clientes**: Muestra una lista de todos los clientes registrados.
    - **Actualizar Cliente**: Permite modificar la información de un cliente existente.
    - **Buscar Cliente**: Permite buscar un cliente por su código.
    - **Eliminar Cliente**: Permite eliminar un cliente de la lista.

2. **Gestión de Libros**
    - **Ingresar Libro**: Permite agregar nuevos libros al inventario.
    - **Lista de Libros**: Muestra una lista de todos los libros disponibles.
    - **Actualizar Libro**: Permite modificar la información de un libro existente.
    - **Buscar Libro**: Permite buscar un libro por su código.
    - **Eliminar Libro**: Permite eliminar un libro del inventario.

3. **Gestión de Ventas**
    - **Realizar Venta**: Permite registrar una nueva venta, actualizando el inventario de libros.
    - **Lista de Ventas**: Muestra una lista de todas las ventas realizadas.
    - **Actualizar Venta**: Permite modificar la información de una venta existente.
    - **Buscar Venta**: Permite buscar una venta por su código.
    - **Eliminar Venta**: Permite eliminar una venta registrada.

4. **Estadísticas**
    - **Ventas Totales por ISBN**: Calcula y muestra las ventas totales de un libro específico por su ISBN.
    - **Libros Más y Menos Vendidos**: Identifica y muestra el libro más vendido y el menos vendido.
    - **Venta Total de la Librería**: Calcula y muestra la cantidad total de ventas realizadas por la librería.
    - **Cliente con Mayor Compra por Venta**: Identifica y muestra el cliente con la mayor compra en una sola transacción.
    - **Cliente con Mayor Volumen de Compra Total**: Identifica y muestra el cliente con el mayor volumen de compras en total.

#### Cómo Ejecutar el Programa

1. **Instalación de Python**: Asegúrese de tener Python instalado en su sistema. Puede descargarlo desde [python.org](https://www.python.org/downloads/).
2. **Ejecución del Script**: Ejecute el script `libreria.py` desde la terminal o línea de comandos:
    ```sh
    python libreria.py
    ```

#### Uso del Menú Principal

El menú principal presenta las siguientes opciones:

1. **Clientes**: Para gestionar clientes.
2. **Libros**: Para gestionar libros.
3. **Ventas**: Para gestionar ventas.
4. **Estadísticas**: Para ver estadísticas de ventas.
5. **Salir**: Para salir del programa.

#### Ejemplo de Uso

1. **Agregar un Cliente**:
    - Seleccione la opción `1. Clientes` en el menú principal.
    - Seleccione `1. Ingresar Clientes` y proporcione el código y nombre del cliente.

2. **Agregar un Libro**:
    - Seleccione la opción `2. Libros` en el menú principal.
    - Seleccione `1. Ingresar Libro` y proporcione el código, título, precio y cantidad en stock del libro.

3. **Realizar una Venta**:
    - Seleccione la opción `3. Ventas` en el menú principal.
    - Seleccione `1. Realizar Venta` y proporcione el código del cliente, el código del libro y la cantidad vendida.

#### Consideraciones

- **Validaciones**: El sistema incluye validaciones para evitar duplicados y asegurar que los datos ingresados sean correctos.
- **Actualizaciones**: Las cantidades de libros en el inventario se actualizan automáticamente tras cada venta.
- **Estadísticas**: Las estadísticas se generan dinámicamente a partir de los datos de ventas y ayudan a entender el rendimiento de la librería.

Este sistema es una herramienta útil para gestionar eficientemente una librería, manteniendo un control detallado sobre clientes, inventarios y ventas, y proporcionando información valiosa para la toma de decisiones empresariales.
