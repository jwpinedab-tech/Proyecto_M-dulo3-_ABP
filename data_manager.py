"""
Módulo de gestión de datos para el Sistema de Gestión de Proyectos.
Maneja las operaciones CRUD y las estructuras de datos principales.
"""

from typing import List, Dict, Optional, Any

# Lista constante pre-cargada con 3 proyectos de prueba de una agencia web
PROYECTOS = [
    {
        "id": 1,
        "nombre": "E-commerce Zapatillas",
        "cliente": "Nike",
        "estado": "En Progreso",
        "horas_estimadas": 120,
        "tareas_completadas": 5,
        "prioridad": ("Alta", 1)
    },
    {
        "id": 2,
        "nombre": "Landing Page",
        "cliente": "Abogado Perez",
        "estado": "Pendiente",
        "horas_estimadas": 10,
        "tareas_completadas": 0,
        "prioridad": ("Media", 2)
    },
    {
        "id": 3,
        "nombre": "Blog Corporativo",
        "cliente": "Tech Solutions",
        "estado": "Finalizado",
        "horas_estimadas": 40,
        "tareas_completadas": 40,
        "prioridad": ("Baja", 3)
    }
]

# Conjunto para validaciones rápidas de ID duplicados
IDS_EXISTENTES = {proyecto["id"] for proyecto in PROYECTOS}


def obtener_proyectos() -> List[Dict[str, Any]]:
    """
    Retorna la lista completa de proyectos.
    
    Returns:
        List[Dict[str, Any]]: Lista de diccionarios con información de proyectos.
    """
    return PROYECTOS.copy()


def agregar_proyecto(nuevo_proyecto: Dict[str, Any]) -> bool:
    """
    Agrega un nuevo proyecto a la lista validando que el ID no exista.
    
    Args:
        nuevo_proyecto (Dict[str, Any]): Diccionario con la información del proyecto.
        
    Returns:
        bool: True si se agregó exitosamente, False si el ID ya existe.
    """
    id_proyecto = nuevo_proyecto.get("id")
    
    if id_proyecto is None:
        return False
    
    # Validación rápida usando el conjunto
    if id_proyecto in IDS_EXISTENTES:
        return False
    
    # Agregar el proyecto a la lista
    PROYECTOS.append(nuevo_proyecto)
    
    # Actualizar el conjunto de IDs existentes
    IDS_EXISTENTES.add(id_proyecto)
    
    return True


def filtrar_por_estado(estado: str) -> List[Dict[str, Any]]:
    """
    Filtra los proyectos por estado.
    
    Args:
        estado (str): Estado a filtrar ("Pendiente", "En Progreso", "Finalizado").
        
    Returns:
        List[Dict[str, Any]]: Lista de proyectos que coinciden con el estado especificado.
    """
    return [proyecto for proyecto in PROYECTOS if proyecto.get("estado") == estado]


def obtener_proyecto_por_id(id_proyecto: int) -> Optional[Dict[str, Any]]:
    """
    Obtiene un proyecto específico por su ID.
    
    Args:
        id_proyecto (int): ID del proyecto a buscar.
        
    Returns:
        Optional[Dict[str, Any]]: Diccionario del proyecto si existe, None si no existe.
    """
    for proyecto in PROYECTOS:
        if proyecto.get("id") == id_proyecto:
            return proyecto
    return None

