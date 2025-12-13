"""
Módulo de reportes para el Sistema de Gestión de Proyectos.
Genera reportes formateados usando f-strings con alineación.
"""


def mostrar_tabla(lista_proyectos):
    """
    Muestra una tabla formateada de proyectos usando f-strings con alineación.
    Encabezados: ID, Cliente, Proyecto, Estado, Progreso %
    
    Args:
        lista_proyectos (list): Lista de diccionarios con información de proyectos.
    """
    if not lista_proyectos:
        print("\n❌ No hay proyectos para mostrar.\n")
        return
    
    # Encabezado de la tabla
    print("\n" + "=" * 100)
    print(f"{'ID':<5} | {'Cliente':<25} | {'Proyecto':<30} | {'Estado':<15} | {'Progreso %':<10}")
    print("=" * 100)
    
    # Filas de datos
    for proyecto in lista_proyectos:
        id_proyecto = proyecto.get("id", "N/A")
        cliente = proyecto.get("cliente", "N/A")
        nombre = proyecto.get("nombre", "N/A")
        estado = proyecto.get("estado", "N/A")
        
        # Calcular porcentaje de avance (Progreso %)
        tareas_completadas = proyecto.get("tareas_completadas", 0)
        horas_estimadas = proyecto.get("horas_estimadas", 1)
        porcentaje_avance = (tareas_completadas / horas_estimadas * 100) if horas_estimadas > 0 else 0
        porcentaje_avance = min(porcentaje_avance, 100.0)
        
        # Formatear con f-strings y alineación
        print(f"{id_proyecto:<5} | {cliente:<25} | {nombre:<30} | {estado:<15} | {porcentaje_avance:>6.1f}%")
    
    print("=" * 100 + "\n")


def mostrar_reporte_productividad(lista_proyectos, total_tareas):
    """
    Muestra un reporte de productividad con estadísticas generales.
    
    Args:
        lista_proyectos (list): Lista de proyectos.
        total_tareas (int): Total de tareas completadas calculado recursivamente.
    """
    print("\n" + "=" * 60)
    print(" " * 15 + "📊 REPORTE DE PRODUCTIVIDAD")
    print("=" * 60)
    
    total_proyectos = len(lista_proyectos)
    proyectos_finalizados = len([p for p in lista_proyectos if p["estado"] == "Finalizado"])
    proyectos_en_progreso = len([p for p in lista_proyectos if p["estado"] == "En Progreso"])
    proyectos_pendientes = len([p for p in lista_proyectos if p["estado"] == "Pendiente"])
    
    print(f"\n{'Total de Proyectos:':<30} {total_proyectos:>5}")
    print(f"{'Proyectos Finalizados:':<30} {proyectos_finalizados:>5}")
    print(f"{'Proyectos en Progreso:':<30} {proyectos_en_progreso:>5}")
    print(f"{'Proyectos Pendientes:':<30} {proyectos_pendientes:>5}")
    print(f"{'Total Tareas Completadas:':<30} {total_tareas:>5}")
    
    print("\n" + "=" * 60 + "\n")


def mostrar_detalle_proyecto(proyecto):
    """
    Muestra el detalle completo de un proyecto.
    
    Args:
        proyecto (dict): Diccionario con información del proyecto.
    """
    print("\n" + "=" * 60)
    print(" " * 15 + "📋 DETALLE DEL PROYECTO")
    print("=" * 60)
    
    porcentaje_avance = (proyecto["tareas_completadas"] / proyecto["horas_estimadas"] * 100) if proyecto["horas_estimadas"] > 0 else 0
    porcentaje_avance = min(porcentaje_avance, 100.0)
    
    prioridad_nombre, prioridad_num = proyecto.get("prioridad", ("N/A", 0))
    
    print(f"\n{'ID:':<25} {proyecto.get('id', 'N/A')}")
    print(f"{'Nombre:':<25} {proyecto.get('nombre', 'N/A')}")
    print(f"{'Cliente:':<25} {proyecto.get('cliente', 'N/A')}")
    print(f"{'Estado:':<25} {proyecto.get('estado', 'N/A')}")
    print(f"{'Horas Estimadas:':<25} {proyecto.get('horas_estimadas', 0)}")
    print(f"{'Tareas Completadas:':<25} {proyecto.get('tareas_completadas', 0)}")
    print(f"{'Porcentaje de Avance:':<25} {porcentaje_avance:.1f}%")
    print(f"{'Prioridad:':<25} {prioridad_nombre} (Nivel {prioridad_num})")
    
    print("\n" + "=" * 60 + "\n")

