"""
Módulo de utilidades para el Sistema de Gestión de Proyectos.
Contiene funciones de validación y funciones recursivas.
"""

# Constantes para estados y prioridades
ESTADOS_VALIDOS = {"Pendiente", "En Progreso", "Finalizado"}
PRIORIDADES_VALIDAS = {"Alta": 1, "Media": 2, "Baja": 3}


def validar_numero(mensaje: str) -> int:
    """
    Valida que el usuario ingrese un número entero positivo.
    Usa un bucle while y try-except para asegurar la entrada correcta.
    Maneja KeyboardInterrupt para salir gracefully.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario.
        
    Returns:
        int: Número entero positivo ingresado por el usuario.
        
    Raises:
        KeyboardInterrupt: Si el usuario presiona Ctrl+C.
    """
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("❌ Por favor, ingresa un número positivo mayor que cero.")
        except ValueError:
            print("❌ Por favor, ingresa un número entero válido.")
        except KeyboardInterrupt:
            print("\n\n⚠️ Operación cancelada por el usuario.")
            raise


def calcular_total_tareas_completadas(lista_proyectos: list) -> int:
    """
    Función recursiva que calcula el total de tareas completadas
    de todos los proyectos en la lista.
    
    REQUISITO: No usa bucles for ni la función sum().
    
    Args:
        lista_proyectos (list): Lista de diccionarios de proyectos.
        
    Returns:
        int: Total de tareas completadas en todos los proyectos.
    """
    # Caso base: lista vacía
    if not lista_proyectos:
        return 0
    
    # Caso recursivo: suma el primer elemento y llama recursivamente al resto
    primer_proyecto = lista_proyectos[0]
    tareas_primer_proyecto = primer_proyecto.get("tareas_completadas", 0)
    resto_proyectos = lista_proyectos[1:]
    
    return tareas_primer_proyecto + calcular_total_tareas_completadas(resto_proyectos)


def validar_estado(estado: str) -> bool:
    """
    Valida que el estado ingresado sea uno de los permitidos.
    
    Args:
        estado (str): Estado a validar.
        
    Returns:
        bool: True si el estado es válido, False en caso contrario.
    """
    return estado in ESTADOS_VALIDOS


def calcular_porcentaje_avance(tareas_completadas: int, horas_estimadas: int) -> float:
    """
    Calcula el porcentaje de avance de un proyecto basado en tareas completadas.
    
    Args:
        tareas_completadas (int): Número de tareas completadas.
        horas_estimadas (int): Total de horas estimadas del proyecto.
        
    Returns:
        float: Porcentaje de avance (0-100).
    """
    if horas_estimadas == 0:
        return 0.0
    
    porcentaje = (tareas_completadas / horas_estimadas) * 100
    return min(porcentaje, 100.0)  # Limitar a máximo 100%


def validar_prioridad(prioridad: str) -> tuple:
    """
    Valida y normaliza una prioridad ingresada.
    
    Args:
        prioridad (str): Nombre de la prioridad (Alta/Media/Baja).
        
    Returns:
        tuple: Tupla con (nombre_prioridad, nivel_prioridad).
    """
    prioridad_normalizada = prioridad.strip().capitalize()
    if prioridad_normalizada not in PRIORIDADES_VALIDAS:
        return ("Media", 2)  # Valor por defecto
    
    return (prioridad_normalizada, PRIORIDADES_VALIDAS[prioridad_normalizada])

