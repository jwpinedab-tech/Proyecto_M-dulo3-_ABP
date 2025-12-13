"""
Sistema de Gestión de Proyectos para Agencia de Desarrollo Web
Punto de entrada principal del sistema.

Autor: Sistema de Gestión de Proyectos
Versión: 1.0
"""

from auth import login
from data_manager import (
    obtener_proyectos,
    agregar_proyecto,
    filtrar_por_estado,
    IDS_EXISTENTES
)
from utils import (
    validar_numero,
    calcular_total_tareas_completadas,
    ESTADOS_VALIDOS,
    PRIORIDADES_VALIDAS,
    validar_prioridad
)
from reports import (
    mostrar_tabla,
    mostrar_reporte_productividad
)


def mostrar_encabezado_principal():
    """
    Muestra el encabezado principal del sistema.
    """
    print("\n" + "=" * 70)
    print(" " * 10 + "🚀 SISTEMA DE GESTIÓN DE PROYECTOS")
    print(" " * 15 + "Agencia de Desarrollo Web")
    print("=" * 70 + "\n")


def mostrar_menu():
    """
    Muestra el menú principal de opciones.
    """
    print("-" * 70)
    print(" " * 20 + "MENÚ PRINCIPAL")
    print("-" * 70)
    print("1. Ver Proyectos")
    print("2. Agregar Proyecto")
    print("3. Filtrar por Estado")
    print("4. Reporte de Productividad")
    print("5. Salir")
    print("-" * 70)


def opcion_ver_todos_proyectos():
    """
    Muestra todos los proyectos en formato de tabla.
    """
    print("\n📋 VER PROYECTOS")
    proyectos = obtener_proyectos()
    mostrar_tabla(proyectos)


def opcion_agregar_proyecto():
    """
    Permite al usuario agregar un nuevo proyecto.
    Pide datos y usa agregar_proyecto de data_manager.
    """
    print("\n➕ AGREGAR PROYECTO")
    print("-" * 70)
    
    # Solicitar datos del proyecto
    id_proyecto = validar_numero("ID del proyecto: ")
    
    # Validar que el ID no exista
    if id_proyecto in IDS_EXISTENTES:
        print(f"\n❌ El ID {id_proyecto} ya existe. Por favor, usa otro ID.\n")
        return
    
    nombre = input("Nombre del proyecto: ").strip()
    cliente = input("Cliente: ").strip()
    
    print(f"\nEstados disponibles: {', '.join(sorted(ESTADOS_VALIDOS))}")
    estado = input("Estado: ").strip()
    
    # Validar estado
    if estado not in ESTADOS_VALIDOS:
        print(f"\n❌ Estado inválido. Usando 'Pendiente' por defecto.\n")
        estado = "Pendiente"
    
    horas_estimadas = validar_numero("Horas estimadas: ")
    tareas_completadas = validar_numero("Tareas completadas: ")
    
    print(f"\nPrioridades: {', '.join([f'{k} ({v})' for k, v in PRIORIDADES_VALIDAS.items()])}")
    prioridad_input = input("Prioridad (Alta/Media/Baja): ").strip()
    prioridad_nombre, prioridad_num = validar_prioridad(prioridad_input)
    
    # Crear diccionario del proyecto
    nuevo_proyecto = {
        "id": id_proyecto,
        "nombre": nombre,
        "cliente": cliente,
        "estado": estado,
        "horas_estimadas": horas_estimadas,
        "tareas_completadas": tareas_completadas,
        "prioridad": (prioridad_nombre, prioridad_num)
    }
    
    # Agregar el proyecto
    if agregar_proyecto(nuevo_proyecto):
        print(f"\n✅ Proyecto '{nombre}' agregado exitosamente.\n")
    else:
        print(f"\n❌ Error al agregar el proyecto. El ID ya existe.\n")


def opcion_filtrar_por_estado():
    """
    Permite filtrar proyectos por estado.
    Pide estado y muestra tabla filtrada.
    """
    print("\n🔍 FILTRAR POR ESTADO")
    print("-" * 70)
    print(f"Estados disponibles: {', '.join(sorted(ESTADOS_VALIDOS))}")
    
    estado = input("Ingresa el estado a filtrar: ").strip()
    
    if estado not in ESTADOS_VALIDOS:
        print(f"\n❌ Estado inválido. Por favor, ingresa uno de los estados válidos.\n")
        return
    
    proyectos_filtrados = filtrar_por_estado(estado)
    
    if proyectos_filtrados:
        print(f"\n📋 Proyectos con estado '{estado}':")
        mostrar_tabla(proyectos_filtrados)
    else:
        print(f"\n❌ No se encontraron proyectos con estado '{estado}'.\n")


def opcion_reporte_productividad():
    """
    Muestra el reporte de productividad.
    Usa la función recursiva de utils.py para mostrar el total de tareas realizadas.
    """
    print("\n📊 REPORTE DE PRODUCTIVIDAD")
    print("-" * 70)
    
    proyectos = obtener_proyectos()
    
    # Usar la función recursiva para calcular el total de tareas completadas
    total_tareas = calcular_total_tareas_completadas(proyectos)
    
    mostrar_reporte_productividad(proyectos, total_tareas)


def menu_principal():
    """
    Función principal que maneja el menú y las opciones del sistema.
    Maneja KeyboardInterrupt para salir gracefully.
    """
    mostrar_encabezado_principal()
    
    try:
        while True:
            mostrar_menu()
            opcion = input("Selecciona una opción (1-5): ").strip()
            
            if opcion == "1":
                opcion_ver_todos_proyectos()
            elif opcion == "2":
                opcion_agregar_proyecto()
            elif opcion == "3":
                opcion_filtrar_por_estado()
            elif opcion == "4":
                opcion_reporte_productividad()
            elif opcion == "5":
                print("\n" + "=" * 70)
                print(" " * 20 + "👋 ¡Hasta luego!")
                print("=" * 70 + "\n")
                break
            else:
                print("\n❌ Opción inválida. Por favor, selecciona una opción del 1 al 5.\n")
    except KeyboardInterrupt:
        print("\n\n⚠️ Operación cancelada. ¡Hasta luego!\n")


def main():
    """
    Función principal del programa.
    Ejecuta el login y, si es exitoso, inicia el menú principal.
    Maneja KeyboardInterrupt para salir gracefully.
    """
    try:
        usuario = login()
        
        if usuario:
            menu_principal()
        else:
            print("❌ No se pudo autenticar. El sistema se cerrará.\n")
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa interrumpido por el usuario. ¡Hasta luego!\n")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}\n")
        print("Por favor, contacta al administrador del sistema.\n")


if __name__ == "__main__":
    main()

