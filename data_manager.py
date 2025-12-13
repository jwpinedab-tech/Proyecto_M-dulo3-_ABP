"""
Módulo de gestión de datos para el Sistema de Gestión de Proyectos.
Maneja las operaciones CRUD y las estructuras de datos principales.
"""

# Lista constante pre-cargada con 10 proyectos de una agencia de desarrollo web
PROYECTOS = [
    {
        "id": 1,
        "nombre": "Landing Page Turismo",
        "cliente": "Andes Travel SpA",
        "estado": "En Progreso",
        "horas_estimadas": 40,
        "tareas_completadas": 20,
        "prioridad": ("Alta", 1)
    },
    {
        "id": 2,
        "nombre": "E-commerce Repostería",
        "cliente": "Dulces & Tentaciones",
        "estado": "Pendiente",
        "horas_estimadas": 80,
        "tareas_completadas": 0,
        "prioridad": ("Media", 2)
    },
    {
        "id": 3,
        "nombre": "Script Automatización Excel",
        "cliente": "Consultora Finanzas",
        "estado": "Finalizado",
        "horas_estimadas": 10,
        "tareas_completadas": 10,
        "prioridad": ("Alta", 1)
    },
    {
        "id": 4,
        "nombre": "Integración Webpay",
        "cliente": "Tienda Zapatos CL",
        "estado": "En Progreso",
        "horas_estimadas": 20,
        "tareas_completadas": 15,
        "prioridad": ("Alta", 1)
    },
    {
        "id": 5,
        "nombre": "Mantenimiento Servidor",
        "cliente": "Clínica Dental Sonrisas",
        "estado": "Finalizado",
        "horas_estimadas": 5,
        "tareas_completadas": 5,
        "prioridad": ("Baja", 3)
    },
    {
        "id": 6,
        "nombre": "API Django REST Framework",
        "cliente": "Startup TechCL",
        "estado": "En Progreso",
        "horas_estimadas": 60,
        "tareas_completadas": 35,
        "prioridad": ("Alta", 1)
    },
    {
        "id": 7,
        "nombre": "Scraper Python para Datos",
        "cliente": "Agencia Marketing Digital",
        "estado": "Pendiente",
        "horas_estimadas": 25,
        "tareas_completadas": 0,
        "prioridad": ("Media", 2)
    },
    {
        "id": 8,
        "nombre": "Dashboard Flask con Gráficos",
        "cliente": "Empresa Logística",
        "estado": "Finalizado",
        "horas_estimadas": 45,
        "tareas_completadas": 45,
        "prioridad": ("Media", 2)
    },
    {
        "id": 9,
        "nombre": "Bot Telegram con Python",
        "cliente": "Tienda Online Ropa",
        "estado": "En Progreso",
        "horas_estimadas": 30,
        "tareas_completadas": 18,
        "prioridad": ("Alta", 1)
    },
    {
        "id": 10,
        "nombre": "Migración Base de Datos",
        "cliente": "Corporación Retail",
        "estado": "Pendiente",
        "horas_estimadas": 50,
        "tareas_completadas": 5,
        "prioridad": ("Baja", 3)
    }
]

# Conjunto para validaciones rápidas de ID duplicados
IDS_EXISTENTES = {proyecto["id"] for proyecto in PROYECTOS}


def obtener_proyectos():
    """
    Retorna la lista completa de proyectos.
    
    Returns:
        list: Lista de diccionarios con información de proyectos.
    """
    return PROYECTOS.copy()


def agregar_proyecto(nuevo_proyecto):
    """
    Agrega un nuevo proyecto a la lista validando que el ID no exista.
    
    Args:
        nuevo_proyecto (dict): Diccionario con la información del proyecto.
        
    Returns:
        bool: True si se agregó exitosamente, False si el ID ya existe.
    """
    id_proyecto = nuevo_proyecto.get("id")
    
    # Validación rápida usando el conjunto
    if id_proyecto in IDS_EXISTENTES:
        return False
    
    # Agregar el proyecto a la lista
    PROYECTOS.append(nuevo_proyecto)
    
    # Actualizar el conjunto de IDs existentes
    IDS_EXISTENTES.add(id_proyecto)
    
    return True


def filtrar_por_estado(estado):
    """
    Filtra los proyectos por estado.
    
    Args:
        estado (str): Estado a filtrar ("Pendiente", "En Progreso", "Finalizado").
        
    Returns:
        list: Lista de proyectos que coinciden con el estado especificado.
    """
    return [proyecto for proyecto in PROYECTOS if proyecto["estado"] == estado]


def obtener_proyecto_por_id(id_proyecto):
    """
    Obtiene un proyecto específico por su ID.
    
    Args:
        id_proyecto (int): ID del proyecto a buscar.
        
    Returns:
        dict or None: Diccionario del proyecto si existe, None si no existe.
    """
    for proyecto in PROYECTOS:
        if proyecto["id"] == id_proyecto:
            return proyecto
    return None

