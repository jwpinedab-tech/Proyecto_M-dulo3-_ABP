"""
Script de restauración de base de datos JSON.
Genera el archivo database.json con los datos iniciales del sistema.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path


def generar_fecha_inicio(dias_atras: int) -> str:
    """
    Genera una fecha de inicio reciente.
    
    Args:
        dias_atras (int): Días hacia atrás desde hoy.
        
    Returns:
        str: Fecha en formato ISO (YYYY-MM-DD).
    """
    fecha = datetime.now() - timedelta(days=dias_atras)
    return fecha.strftime("%Y-%m-%d")


def crear_base_datos_json():
    """
    Crea el archivo database.json con los datos iniciales del sistema.
    """
    # Estructura de la base de datos
    database = {
        "usuarios": {
            "admin": "1234",
            "jacqueline": "dev2025"
        },
        "proyectos": [
            {
                "id": 1,
                "nombre": "E-commerce Zapatillas",
                "cliente": "Nike",
                "estado": "En Progreso",
                "horas_estimadas": 120,
                "tareas_completadas": 5,
                "prioridad": ["Alta", 1],
                "fecha_inicio": generar_fecha_inicio(15),  # Hace 15 días
                "fecha_actualizacion": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "id": 2,
                "nombre": "Landing Page",
                "cliente": "Abogado Perez",
                "estado": "Pendiente",
                "horas_estimadas": 10,
                "tareas_completadas": 0,
                "prioridad": ["Media", 2],
                "fecha_inicio": generar_fecha_inicio(5),  # Hace 5 días
                "fecha_actualizacion": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "id": 3,
                "nombre": "Blog Corporativo",
                "cliente": "Tech Solutions",
                "estado": "Finalizado",
                "horas_estimadas": 40,
                "tareas_completadas": 40,
                "prioridad": ["Baja", 3],
                "fecha_inicio": generar_fecha_inicio(60),  # Hace 60 días
                "fecha_fin": generar_fecha_inicio(10),  # Finalizado hace 10 días
                "fecha_actualizacion": datetime.now().strftime("%Y-%m-%d")
            }
        ],
        "metadata": {
            "version": "1.0.0",
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_proyectos": 3,
            "total_usuarios": 2
        }
    }
    
    # Ruta del archivo JSON (en el directorio del proyecto)
    archivo_json = Path(__file__).parent / "database.json"
    
    try:
        # Escribir el archivo JSON con formato legible
        with open(archivo_json, 'w', encoding='utf-8') as f:
            json.dump(database, f, indent=4, ensure_ascii=False)
        
        print("=" * 70)
        print(" " * 15 + "✅ BASE DE DATOS RESTAURADA")
        print("=" * 70)
        print(f"\n📁 Archivo creado: {archivo_json}")
        print(f"\n📊 Resumen de datos restaurados:")
        print(f"   • Usuarios: {len(database['usuarios'])}")
        print(f"   • Proyectos: {len(database['proyectos'])}")
        print(f"\n👤 Usuarios restaurados:")
        for usuario, _ in database['usuarios'].items():
            print(f"   - {usuario}")
        print(f"\n📋 Proyectos restaurados:")
        for proyecto in database['proyectos']:
            print(f"   - ID {proyecto['id']}: {proyecto['nombre']} ({proyecto['cliente']})")
            print(f"     Estado: {proyecto['estado']} | Prioridad: {proyecto['prioridad'][0]}")
        print("\n" + "=" * 70)
        print("✅ Restauración completada exitosamente.\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error al crear el archivo JSON: {e}\n")
        return False


if __name__ == "__main__":
    crear_base_datos_json()

