import uuid
from datetime import datetime

NOMBRE_DEL_CINE = "Films Proyect"  

peliculas = [
    {
        'titulo': 'Films',
        'tipo_publico': 'A',
        'tipo_sala': '3d',
        'hora_funcion': '20:00',
        'precio': 10.50
    },
    {
        'titulo': 'Toy Story',
        'tipo_publico': 'Infantil',
        'tipo_sala': 'Sala 2',
        'hora_funcion': '18:00',
        'precio': 8.00
    }
]
estado_asientos = {
    'Films': [[' ' for _ in range(10)] for _ in range(4)],
    'Toy Story': [[' ' for _ in range(10)] for _ in range(4)]
}

NUM_FILAS = 4
ASIENTOS_POR_FILA = 10

facturas = [
     {
        'Cliente': 'Usuario',
        'Pelicula': 'Films',
        'Tipo de Sala': ' Sala 1 3d',
        'hora_funcion': '7pm',
        'Aciento': 'F3,A7',
        'precio': 5.0
    },
    ]

cliente = []  # Inicializar cliente como una lista vacía
acompañantes_actual = []
pagos_registrados = []


def mostrar_menu_bienvenida():
    print("======================================")
    print("     FFFFFFF II LL      MM   MM SSSSS ")
    print("     FF      II LL      MMM MMM SS    ")
    print("     FFFFFFF II LL      MM M MM SSSSS ")
    print("     FF      II LL      MM   MM    SS ")
    print("     FF      II LLLLL   MM   MM SSSSS ")    
    print("======================================")
    print("    ¡Bienvenido a Films Proyect!      ")
    print("   ¡Creando Nuevas Experiencias!      ")
    print("   -----------------------------      ")
    print("            Menu Principal            ")
    print("   -----------------------------      ")
    print("1. Ingresar como Administrador")
    print("2. Iniciar como Cliente")
    print("3. Salir")
    print("-----------------------------")


def obtener_opcion():
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_administrador()
            return opcion
        elif opcion == "2":
            menu_cliente()
            return opcion
        elif opcion == "3":
            print("¡Gracias por visitarnos!")
            return opcion
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def iniciar_sesion_administrador():
    nombre_usuario_correcto = "adm"
    contrasena_correcta = "123"

    nombre_usuario = input("Ingrese el nombre de administrador: ")
    contrasena = input("Ingrese la contraseña: ")

    if nombre_usuario == nombre_usuario_correcto and contrasena == contrasena_correcta:
        menu_administrador()
    else:
        print("Credenciales incorrectas. Intente de nuevo.")
        return nombre_usuario 


def menu_administrador():
    while True:
        print("\n--- Menú del Administrador ---")
        print("1. Gestionar Películas")
        print("2. Gestionar Clientes por Asiento")
        print("3. Gestionar Facturas")
        print("4. Volver al Menú Principal") # Opción para volver atrás

        opcion_admin = input("Seleccione una opción: ")

        if opcion_admin == "1":
            gestionar_peliculas() # Llamamos a la función de gestión de películas
        elif opcion_admin == "2":
            gestionar_clientes_asiento() # Llamamos a la función de gestión de clientes por asiento
        elif opcion_admin == "3":
            gestionar_facturas() # Llamamos a la función de gestión de facturas
        elif opcion_admin == "4":
            mostrar_menu_bienvenida()
            
            
            break # Sale del bucle del menú de administrador
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def menu_cliente():
    while True:
        print("\n--- Menú de Cliente ---")
        print("1. Adquirir un Boleto")
        print("2. Volver al Menú Principal")

        opcion_cliente = input("Seleccione una opción: ")

        if opcion_cliente == "1":
            adquirir_boleto()
        elif opcion_cliente == "2":
            print("Volviendo al Menú Principal.")
            mostrar_menu_bienvenida()
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


def gestionar_peliculas():
    while True:
        print("\n--- Gestión de Películas ---")
        print("1. Ver Películas Disponibles")
        print("2. Crear Película")
        print("3. Editar Película")
        print("4. Eliminar Película")
        print("5. Volver al Menú del Administrador")

        opcion_peliculas = input("Seleccione una opción: ")

        if opcion_peliculas == "1":
            mostrar_peliculas()
        elif opcion_peliculas == "2":
            crear_pelicula()
        elif opcion_peliculas == "3":
            editar_pelicula()
        elif opcion_peliculas == "4":
            eliminar_pelicula()
        elif opcion_peliculas == "5":
            menu_administrador()
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def mostrar_peliculas():
    if not peliculas:
        print("Aún no hay películas disponibles.")
    else:
        print("\n--- Películas Disponibles ---")
        for i, pelicula in enumerate(peliculas):
            print(f"{i + 1}. Título: {pelicula['titulo']}")
            print(f"    Público: {pelicula['tipo_publico']}")
            print(f"    Sala: {pelicula['tipo_sala']}")
            print(f"    Hora: {pelicula['hora_funcion']}")
            print(f"    Precio: ${pelicula['precio']:.2f}")

mostrar_peliculas()

def crear_pelicula():
    print("\n--- Crear Nueva Película ---")
    titulo = input("Ingrese el título: ")
    tipo_publico = input("Ingrese el tipo de público (A, B, C, D): ").upper()
    tipo_sala = input("Ingrese el tipo de sala (2D, 3D, IMAX, etc.): ").upper()
    hora_funcion = input("Ingrese la hora de la función (HH:MM): ")
    precio = float(input("Ingrese el precio: "))
    nueva_pelicula = {
        "titulo": titulo,
        "tipo_publico": tipo_publico,
        "tipo_sala": tipo_sala,
        "hora_funcion": hora_funcion,
        "precio": precio
    }
    peliculas.append(nueva_pelicula)
    print(f"\nPelícula '{titulo}' creada exitosamente.")

def editar_pelicula():
    mostrar_peliculas()
    if not peliculas:
        return
    try:
        indice_editar = int(input("\nIngrese el número de la película que desea editar (o 0 para volver): ")) - 1
        if indice_editar == -1:
            return
        if 0 <= indice_editar < len(peliculas):
            pelicula_a_editar = peliculas[indice_editar]
            print(f"\n--- Editar Película: {pelicula_a_editar['titulo']} ---")
            titulo = input(f"Nuevo título ({pelicula_a_editar['titulo']}): ") or pelicula_a_editar['titulo']
            tipo_publico = input(f"Nuevo tipo de público ({pelicula_a_editar['tipo_publico']}): ").upper() or pelicula_a_editar['tipo_publico']
            tipo_sala = input(f"Nuevo tipo de sala ({pelicula_a_editar['tipo_sala']}): ").upper() or pelicula_a_editar['tipo_sala']
            hora_funcion = input(f"Nueva hora de la función ({pelicula_a_editar['hora_funcion']}): ") or pelicula_a_editar['hora_funcion']
            precio = input(f"Nuevo precio (${pelicula_a_editar['precio']:.2f}): ")
            precio = float(precio) if precio else pelicula_a_editar['precio']

            peliculas[indice_editar] = {
                "titulo": titulo,
                "tipo_publico": tipo_publico,
                "tipo_sala": tipo_sala,
                "hora_funcion": hora_funcion,
                "precio": precio
            }
            print(f"\nPelícula '{titulo}' editada exitosamente.")
        else:
            print("Número de película inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    
def eliminar_pelicula():
    mostrar_peliculas()
    if not peliculas:
        return

    try:
        indice_eliminar = int(input("\nIngrese el número de la película que desea eliminar (o 0 para volver): ")) - 1
        if indice_eliminar == -1:
            return
        if 0 <= indice_eliminar < len(peliculas):
            pelicula_eliminada = peliculas.pop(indice_eliminar)
            print(f"\nPelícula '{pelicula_eliminada['titulo']}' eliminada exitosamente.")
        else:
            print("Número de película inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def gestionar_clientes_asiento():
    while True:
        print("\n--- Gestión de Clientes por Asiento ---")
        print("1. Ver Asientos de una Película")
        print("2. Asignar Cliente a Asiento")
        print("3. Editar Cliente en Asiento")
        print("4. Eliminar Cliente de Asiento")
        print("5. Volver al Menú del Administrador")

        opcion_asientos = input("Seleccione una opción: ").lower()

        if opcion_asientos == "1":
            ver_asientos_pelicula()
        elif opcion_asientos == "2":
            titulo_pelicula = seleccionar_pelicula()
            if titulo_pelicula:
                asignar_cliente_asiento(titulo_pelicula)
        elif opcion_asientos == "3":
            titulo_pelicula = seleccionar_pelicula()
            if titulo_pelicula:
                editar_cliente_asiento(titulo_pelicula)
        elif opcion_asientos == "4":
            titulo_pelicula = seleccionar_pelicula()
            if titulo_pelicula:
                eliminar_cliente_asiento(titulo_pelicula)
        elif opcion_asientos == "5":
            menu_administrador()
            return
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def seleccionar_pelicula():
    if not peliculas:
        print("Aún no hay películas disponibles.")
        return None
    else:
        print("\n--- Seleccione una Película ---")
        for i, pelicula in enumerate(peliculas):
            print(f"{i + 1}. {pelicula['titulo']}")
        while True:
            try:
                opcion = int(input("Ingrese el número de la película: ")) - 1
                if 0 <= opcion < len(peliculas):
                    return peliculas[opcion]['titulo']
                else:
                    print("Número de película inválido.")
            except ValueError:
                print("Por favor, ingrese un número.")

def ver_asientos_pelicula():
    titulo_pelicula = seleccionar_pelicula()
    if titulo_pelicula:
        if titulo_pelicula in estado_asientos:
            print(f"\n--- Asientos de '{titulo_pelicula}' ---")
            for i, fila in enumerate(estado_asientos[titulo_pelicula]):
                print(f"Fila {i + 1}: ", end="")
                for asiento in fila:
                    print(f"[{asiento}]", end="")
                print()
        else:
            print(f"No se encontraron asientos para la película '{titulo_pelicula}'.")

def asignar_cliente_asiento(titulo_pelicula):
    if titulo_pelicula in estado_asientos:
        print(f"\n--- Asignar Cliente en '{titulo_pelicula}' ---")
        fila = int(input("Ingrese el número de fila (1-4): ")) - 1
        puesto = int(input("Ingrese el número de puesto (1-10): ")) - 1

        if 0 <= fila < 4 and 0 <= puesto < 10:
            if estado_asientos[titulo_pelicula][fila][puesto] == ' ':
                nombre_cliente = input("Ingrese el nombre completo del cliente (Nombre Apellido): ")
                iniciales = ''.join([parte[0].upper() for parte in nombre_cliente.split()])  # Obtener iniciales
                estado_asientos[titulo_pelicula][fila][puesto] = iniciales
                print(f"Cliente '{iniciales}' asignado a Fila {fila + 1}, Puesto {puesto + 1}.")
            else:
                print("El asiento ya está ocupado.")
        else:
            print("Número de fila o puesto inválido.")
    else:
        print(f"No se encontraron asientos para la película '{titulo_pelicula}'.")

def editar_cliente_asiento(titulo_pelicula):
    if titulo_pelicula in estado_asientos:
        print(f"\n--- Editar Cliente en '{titulo_pelicula}' ---")
        fila = int(input("Ingrese el número de fila (1-4): ")) - 1
        puesto = int(input("Ingrese el número de puesto (1-10): ")) - 1

        if 0 <= fila < 4 and 0 <= puesto < 10:
            if estado_asientos[titulo_pelicula][fila][puesto] != ' ':
                nuevo_nombre = input("Ingrese el nuevo nombre completo del cliente (Nombre Apellido): ")
                iniciales = ''.join([parte[0].upper() for parte in nuevo_nombre.split()])  # Obtener nuevas iniciales
                estado_asientos[titulo_pelicula][fila][puesto] = iniciales
                print(f"Cliente editado a '{iniciales}' en Fila {fila + 1}, Puesto {puesto + 1}.")
            else:
                print("El asiento está vacío. No se puede editar.")
        else:
            print("Número de fila o puesto inválido.")
    else:
        print(f"No se encontraron asientos para la película '{titulo_pelicula}'.")


def eliminar_cliente_asiento(titulo_pelicula):
    if titulo_pelicula in estado_asientos:
        print(f"\n--- Eliminar Cliente en '{titulo_pelicula}' ---")
        fila = int(input("Ingrese el número de fila (1-4): ")) - 1
        puesto = int(input("Ingrese el número de puesto (1-10): ")) - 1

        if 0 <= fila < 4 and 0 <= puesto < 10:
            if estado_asientos[titulo_pelicula][fila][puesto] != ' ':
                estado_asientos[titulo_pelicula][fila][puesto] = ' '
                print(f"Cliente eliminado de Fila {fila + 1}, Puesto {puesto + 1}.")
            else:
                print("El asiento ya está vacío.")
        else:
            print("Número de fila o puesto inválido.")
    else:
        print(f"No se encontraron asientos para la película '{titulo_pelicula}'.")

def gestionar_facturas():
    while True:
        print("\n--- Gestión de Facturas ---")
        print("1. Ver Facturas")
        print("2. Crear Factura")
        print("3. Editar Factura")
        print("4. Eliminar Factura")
        print("5. Volver al Menú del Administrador")

        opcion_facturas = input("Seleccione una opción: ")

        if opcion_facturas == "1":
            mostrar_facturas()
        elif opcion_facturas == "2":
            crear_factura()
        elif opcion_facturas == "3":
            editar_factura()
        elif opcion_facturas == "4":
            eliminar_factura()
        elif opcion_facturas == "5":
            menu_administrador()
            return  # Salir de la función
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def mostrar_facturas():
    if not facturas:
        print("Aún no hay facturas disponibles.")
    else:
        print("\n--- Facturas ---")
        for i, factura in enumerate(facturas):
            print(f"\nFactura #{i + 1}:")
            for clave, valor in factura.items():
                print(f"  {clave}: {valor}")
        
def crear_factura():
    print("\n--- Crear Nueva Factura ---")
    cliente = input("Ingrese el nombre del cliente: ")
    pelicula = input("Ingrese el título de la película: ")
    tipo_sala = input("Ingrese el tipo de sala: ")
    hora_funcion = input("Ingrese la hora de la función: ")
    asiento = input("Ingrese el número de asiento: ")
    monto_cancelado = float(input("Ingrese el monto cancelado: "))

    nueva_factura = {
        'Nombre del Cine': NOMBRE_DEL_CINE,
        'Cliente': cliente,
        'Película': pelicula,
        'Tipo de Sala': tipo_sala,
        'hora de la funcion': hora_funcion,
        'Aciento': asiento,
        'Monto Cancelado': monto_cancelado
    }
    facturas.append(nueva_factura)
    print("\nFactura creada exitosamente.")
    
def editar_factura():
    mostrar_facturas()
    if not facturas:
        return

    try:
        indice_editar = int(input("\nIngrese el número de la factura que desea editar (o 0 para volver): ")) - 1
        if indice_editar == -1:
            return
        if 0 <= indice_editar < len(facturas):
            factura_a_editar = facturas[indice_editar]
            print("\n--- Editar Factura ---")
            print(f"Editando factura para: {factura_a_editar['Cliente']}")

            pelicula_clave = 'Película' if 'Película' in factura_a_editar else 'Pelicula' # Intenta ambas claves

            cliente = input(f"Nuevo cliente ({factura_a_editar.get('Cliente', '')}): ") or factura_a_editar.get('Cliente')
            pelicula = input(f"Nueva película ({factura_a_editar.get(pelicula_clave, '')}): ") or factura_a_editar.get(pelicula_clave)
            tipo_sala = input(f"Nuevo tipo de sala ({factura_a_editar.get('Tipo de Sala', '')}): ") or factura_a_editar.get('Tipo de Sala')
            hora_funcion = input(f"Nueva hora de la función ({factura_a_editar.get('hora de la funcion', '')}): ") or factura_a_editar.get('hora de la funcion')
            asiento = input(f"Nuevo asiento ({factura_a_editar.get('Aciento', '')}): ") or factura_a_editar.get('Aciento')
            monto_cancelado = input(f"Nuevo monto cancelado ({factura_a_editar.get('Monto Cancelado', '')}): ")
            monto_cancelado = float(monto_cancelado) if monto_cancelado else factura_a_editar.get('Monto Cancelado')

            facturas[indice_editar] = {
                'Nombre del Cine': factura_a_editar.get('Nombre del Cine', NOMBRE_DEL_CINE), # Mantener el nombre del cine existente si está
                'Cliente': cliente,
                'Película': pelicula,
                'Tipo de Sala': tipo_sala,
                'hora de la funcion': hora_funcion,
                'Aciento': asiento,
                'Monto Cancelado': monto_cancelado
            }
            print("\nFactura editada exitosamente.")
        else:
            print("Número de factura inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        
        
def eliminar_factura():
    mostrar_facturas()
    if not facturas:
        return

    try:
        indice_eliminar = int(input("\nIngrese el número de la factura que desea eliminar (o 0 para volver): ")) - 1
        if indice_eliminar == -1:
            return
        if 0 <= indice_eliminar < len(facturas):
            factura_eliminada = facturas.pop(indice_eliminar)
            print("\nFactura eliminada exitosamente:")
            for clave, valor in factura_eliminada.items():
                print(f"  {clave}: {valor}")
        else:
            print("Número de factura inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        
def adquirir_boleto():
    from datetime import datetime

    global cliente
    global acompañantes_actual
    global estado_asientos
    global pagos_registrados


    # Obtener la hora actual
    hora_actual = datetime.now().hour

    # Solicitar datos del usuario
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))

    cliente_info = {"nombre": nombre, "apellido": apellido, "edad": edad} # Usar 'nombre', 'apellido', 'edad'
    cliente.append(cliente_info)

    # Lista para almacenar a todas las personas que verán la película
    personas = [cliente_info]
    acompañantes = [] # Aseguramos que la lista de acompañantes esté vacía para esta compra

    # Preguntar si viene solo o con acompañantes
    acompañantes_str = input("¿Viene con acompañantes? (sí/no): ").strip().lower()

    if acompañantes_str == 'sí':
        num_acompañantes = int(input("¿Cuántos acompañantes tiene?: "))
        for i in range(num_acompañantes):
            nombre = input(f"Ingrese el nombre del acompañante {i + 1}: ")
            apellido = input(f"Ingrese el apellido del acompañante {i + 1}: ")
            edad = int(input(f"Ingrese la edad del acompañante {i + 1}: "))
            acomp_info = {"nombre": nombre, "apellido": apellido, "edad": edad}
            acompañantes_actual.append(acomp_info)
            personas.append(acomp_info) # Añadir acompañantes a la lista de personas
    
    
    # Validación de edad y horario para todos (cliente y acompañantes)
    for persona in personas:
        if persona['edad'] <= 12:
            if not any(p['edad'] >= 18 for p in personas):
                print("Los niños menores de 12 años deben estar acompañados por un adulto.")
                return
            if hora_actual > 19:
                print("Los infantes no pueden adquirir un boleto después de las 7 PM.")
                return
        elif 13 <= persona['edad'] <= 17:
            if hora_actual > 19:
                print("Los adolescentes no pueden adquirir un boleto después de las 7 PM.")
                return
        elif 18 <= persona['edad'] < 21:
            print("Esta película es para adultos, no requieres de la edad reglamentaria.") # Esto parece un error en tu lógica anterior
            pass # Debería poder comprar si es mayor de 18

    # Seleccionar película
    pelicula_seleccionada = seleccionar_pelicula_para_cliente()
    if not pelicula_seleccionada:
        return

    # Seleccionar asientos
    num_boletos = 1 + len(acompañantes_actual)
    asientos_seleccionados = seleccionar_asientos(pelicula_seleccionada['titulo'], num_boletos)
    if not asientos_seleccionados:
        return

    # Mostrar confirmación de la compra
    print("\n--- Confirmación de Compra ---")
    print(f"Cliente: {cliente_info['nombre']} {cliente_info['apellido']}, Edad: {cliente_info['edad']}")
    if acompañantes_actual:
        print("Acompañantes:")
        for acomp in acompañantes_actual:
            print(f"{acomp['nombre']} {acomp['apellido']}, Edad: {acomp['edad']}")
    print(f"Película: {pelicula_seleccionada['titulo']}")
    print(f"Público: {pelicula_seleccionada['tipo_publico']}")
    print(f"Sala: {pelicula_seleccionada['tipo_sala']}")
    print(f"Hora: {pelicula_seleccionada['hora_funcion']}")
    print("Asientos:", ", ".join([f"F{a[0]},A{a[1]}" for a in asientos_seleccionados]))
    print(f"Precio por boleto: ${pelicula_seleccionada['precio']:.2f}")
    print(f"Total a pagar: ${pelicula_seleccionada['precio'] * num_boletos:.2f}")

    # Aquí podrías agregar la lógica para el pago y la generación de la factura
    # que incluya todos estos detalles. Por ahora, solo los mostramos.

    print("\n¡Boleto(s) adquirido(s) exitosamente!")

def seleccionar_pelicula_para_cliente():
    print("\n--- Películas Disponibles ---")
    for i, pelicula in enumerate(peliculas):
        print(f"{i + 1}. {pelicula['titulo']} - Precio: ${pelicula['precio']:.2f}")

    while True:
        try:
            opcion_pelicula = int(input("Seleccione el número de la película que desea ver: ")) - 1
            if 0 <= opcion_pelicula < len(peliculas):
                return peliculas[opcion_pelicula]
            else:
                print("Número de película inválido.")
        except ValueError:
            print("Por favor, ingrese un número.")
    return None

def mostrar_asientos(titulo_pelicula):
    if titulo_pelicula in estado_asientos:
        print(f"\n--- Asientos de '{titulo_pelicula}' ---")
        print("Leyenda: [ ] = Disponible, [XX] = Ocupado")
        for i, fila in enumerate(estado_asientos[titulo_pelicula]):
            print(f"Fila {i + 1}: ", end="")
            for j, asiento in enumerate(fila):
                print(f"[{asiento}]", end="")
            print()
    else:
        print(f"No se encontraron asientos para la película '{titulo_pelicula}'.")

def seleccionar_asientos(titulo_pelicula, num_personas):
    asientos_seleccionados = []
    mostrar_asientos(titulo_pelicula)
    print(f"\nSeleccione {num_personas} asientos.")
    for i in range(num_personas):
        while True:
            try:
                fila_num = int(input(f"Ingrese la fila para la persona {i + 1} (1-4): ")) - 1
                asiento_num = int(input(f"Ingrese el asiento para la persona {i + 1} (1-10): ")) - 1
                if 0 <= fila_num < 4 and 0 <= asiento_num < 10:
                    if estado_asientos[titulo_pelicula][fila_num][asiento_num] == ' ':
                        estado_asientos[titulo_pelicula][fila_num][asiento_num] = 'X' # Marcar como ocupado temporalmente
                        asientos_seleccionados.append((fila_num + 1, asiento_num + 1))
                        mostrar_asientos(titulo_pelicula)
                        break
                    else:
                        print("Este asiento ya está ocupado. Por favor, elija otro.")
                else:
                    print("Número de fila o asiento inválido.")
            except ValueError:
                print("Por favor, ingrese números válidos.")
    return asientos_seleccionados


def realizar_pago(cliente_info, monto_a_pagar):
    print("\n--- Proceso de Pago ---")
    print(f"Monto total a pagar: ${monto_a_pagar:.2f}")
    print("Formas de pago disponibles:")
    print("1. Divisa")
    print("2. Bolívares") 
    print("4. Zelle")
    print("5. Criptomoneda")

    while True:
        opcion_pago = input("Seleccione la forma de pago (1-5): ")
        if opcion_pago in ["1", "2", "3", "4", "5"]:
            monto_introducido = input(f"Ingrese el monto a pagar (${monto_a_pagar:.2f}): ")
            try:
                monto_introducido = float(monto_introducido)
                if monto_introducido >= monto_a_pagar:
                    print("Pago realizado con éxito.")
                    return True
                else:
                    print("El monto introducido es insuficiente.")
            except ValueError:
                print("Monto inválido. Por favor, ingrese un número.")
        else:
            print("Opción de pago inválida. Por favor, intente de nuevo.")
    return False

def registrar_pago(cliente_info, monto_pagado):
    now = datetime.now()
    fecha_hora_pago = now.strftime("%Y-%m-%d %H:%M:%S")
    datos_pagador = {}
    if cliente_info['edad'] >= 18:
        datos_pagador = {"nombre": cliente_info['nombre'], "apellido": cliente_info['apellido'], "edad": cliente_info['edad']}
    else:
        datos_pagador = {"nombre": cliente_info['nombre'], "apellido": cliente_info['apellido'], "edad": cliente_info['edad'], "nota": "Pago realizado por menor de edad"}

    pago = {
        "fecha_hora": fecha_hora_pago,
        "monto": monto_pagado,
        "pagador": datos_pagador
    }
    pagos_registrados.append(pago)
    print("\nRegistro de pago exitoso.")

def revertir_seleccion_asientos(titulo_pelicula, asientos):
    if titulo_pelicula in estado_asientos:
        for fila, asiento in asientos:
            estado_asientos[titulo_pelicula][fila - 1][asiento - 1] = ' '
        print("Selección de asientos revertida.")

def generar_factura(cliente, acompañantes, pelicula, asientos, monto_cancelado):
    numero_factura = str(uuid.uuid4())[:8].upper()
    factura = {
        'Número de Factura': numero_factura,
        'Nombre del Cine': NOMBRE_DEL_CINE,
        'Cliente': f"{cliente['nombre']} {cliente['apellido']}",
        'Edad del Cliente': cliente['edad'],
        'Acompañantes': [],
        'Título de la Película': pelicula['titulo'],
        'Público': pelicula['tipo_publico'],
        'Sala': pelicula['tipo_sala'],
        'Horario de la Función': pelicula['hora_funcion'],
        'Asientos': ", ".join([f"F{a[0]},A{a[1]}" for a in asientos]),
        'Monto Cancelado': f"${monto_cancelado:.2f}",
        'Fecha y Hora de Pago': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    if acompañantes:
        for acomp in acompañantes:
            factura['Acompañantes'].append(f"{acomp['nombre']} {acomp['apellido']} (Edad: {acomp['edad']})")

    imprimir_factura_final(factura)
    facturas.append(factura)

def imprimir_factura_final(factura):
    print("\n--- FACTURA ---")
    for clave, valor in factura.items():
        print(f"{clave}: {valor}")
    print("¡Gracias por su compra!")

def imprimir_factura_previa(cliente, acompañantes, pelicula, asientos, monto_total):
    print("\n--- Vista Previa de su Boleto ---")
    print(f"Nombre del Cine: {NOMBRE_DEL_CINE}")
    print(f"Cliente: {cliente['nombre']} {cliente['apellido']}, Edad: {cliente['edad']}")
    if acompañantes:
        print("Acompañantes:")
        for acomp in acompañantes:
            print(f"  {acomp['nombre']} {acomp['apellido']}, Edad: {acomp['edad']}")
    else:
        print("  Ninguno")
    print(f"Película: {pelicula['titulo']}")
    print(f"Público: {pelicula['tipo_publico']}")
    print(f"Sala: {pelicula['tipo_sala']}")
    print(f"Hora de Función: {pelicula['hora_funcion']}")
    print("Asientos:", ", ".join([f"F{a[0]},A{a[1]}" for a in asientos]))
    print(f"Monto Total a Pagar: ${monto_total:.2f}")
    print("Por favor, verifique que la información sea correcta antes de continuar con el pago.")

def main():
    mostrar_menu_bienvenida()
    opcion = obtener_opcion()

    if opcion == "1":
        iniciar_sesion_administrador() # Llama a la función a través del módulo
    elif opcion == "2":
        print("¡Bienvenido, Cliente!")
        menu_cliente()  # Llamar a la función menu_cliente()
    elif opcion == "3":
        print("¡Gracias por visitarnos!")

def obtener_opcion():
    while True:
        opcion = input("Por favor, seleccione una opción: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()