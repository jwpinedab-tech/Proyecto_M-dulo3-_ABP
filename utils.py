"""
Módulo de utilidades para el Sistema de Gestión de Proyectos Freelance.
Contiene funciones de validación y funciones recursivas.
"""


def validar_numero(mensaje):
    """
    Valida que el usuario ingrese un número entero positivo.
    Usa un bucle while y try-except para asegurar la entrada correcta.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario.
        
    Returns:
        int: Número entero positivo ingresado por el usuario.
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


def calcular_total_tareas_completadas(lista_proyectos):
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


def validar_estado(estado):
    """
    Valida que el estado ingresado sea uno de los permitidos.
    
    Args:
        estado (str): Estado a validar.
        
    Returns:
        bool: True si el estado es válido, False en caso contrario.
    """
    estados_validos = {"Pendiente", "En Progreso", "Finalizado"}
    return estado in estados_validos


def calcular_porcentaje_avance(tareas_completadas, horas_estimadas):
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

