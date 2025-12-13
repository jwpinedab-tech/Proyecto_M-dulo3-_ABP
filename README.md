# 🚀 Sistema de Gestión de Proyectos - Agencia de Desarrollo Web

Sistema de gestión de proyectos desarrollado en Python para agencias de desarrollo web. Permite gestionar proyectos, clientes, estados y generar reportes de productividad.

## 📋 Características

- ✅ **Autenticación de usuarios** con sistema de login seguro
- 📊 **Gestión de proyectos** con CRUD completo
- 🔍 **Filtrado por estado** (Pendiente, En Progreso, Finalizado)
- 📈 **Reportes de productividad** con cálculos recursivos
- 🎨 **Interfaz de consola** intuitiva y profesional
- 🔒 **Validación de datos** robusta
- 📝 **Código modularizado** siguiendo PEP 8

## 🛠️ Tecnologías

- **Python 3.7+**
- **Biblioteca estándar de Python** (sin dependencias externas)

## 📁 Estructura del Proyecto

```
proyecto_gestion_proyectos/
├── main.py           # Punto de entrada y menú principal
├── auth.py           # Módulo de autenticación (Login)
├── data_manager.py   # Gestión de datos (CRUD y estructuras)
├── utils.py          # Validaciones y funciones recursivas
├── reports.py        # Generación de reportes con f-strings
├── requirements.txt # Dependencias del proyecto
├── .gitignore       # Archivos a ignorar en Git
└── README.md        # Este archivo
```

## 🚀 Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/sistema-gestion-proyectos.git
cd sistema-gestion-proyectos
```

2. **Verificar Python:**
```bash
python --version  # Debe ser 3.7 o superior
```

3. **Ejecutar el programa:**
```bash
python main.py
```

## 👤 Credenciales de Acceso

El sistema viene con usuarios pre-configurados:

| Usuario      | Contraseña |
|--------------|------------|
| `admin`      | `1234`     |
| `jacqueline` | `dev2025`  |

## 📖 Uso

### 1. Iniciar Sesión
Al ejecutar el programa, se solicitarán credenciales. Tienes 3 intentos para ingresar correctamente.

### 2. Menú Principal
Una vez autenticado, podrás acceder a las siguientes opciones:

1. **Ver Proyectos** - Muestra todos los proyectos en formato de tabla
2. **Agregar Proyecto** - Permite agregar un nuevo proyecto al sistema
3. **Filtrar por Estado** - Filtra proyectos por su estado actual
4. **Reporte de Productividad** - Muestra estadísticas generales usando cálculo recursivo
5. **Salir** - Cierra la aplicación

### 3. Proyectos Pre-cargados

El sistema incluye 3 proyectos de prueba:

- **E-commerce Zapatillas** (Nike) - En Progreso
- **Landing Page** (Abogado Perez) - Pendiente
- **Blog Corporativo** (Tech Solutions) - Finalizado

## 🏗️ Arquitectura

### Módulos

- **`main.py`**: Controlador principal que orquesta el flujo de la aplicación
- **`auth.py`**: Maneja la autenticación de usuarios con validación de credenciales
- **`data_manager.py`**: Gestiona las operaciones CRUD sobre los proyectos
- **`utils.py`**: Contiene funciones de validación y cálculo recursivo
- **`reports.py`**: Genera reportes formateados para visualización

### Estructuras de Datos Utilizadas

- **Listas**: Almacenamiento de proyectos
- **Diccionarios**: Estructura de datos de cada proyecto
- **Tuplas**: Prioridades (nombre, nivel)
- **Conjuntos**: Validación rápida de IDs existentes
- **Recursividad**: Cálculo de total de tareas completadas

## 🧪 Requisitos del Sistema

- Python 3.7 o superior
- Sistema operativo: Windows, Linux o macOS
- Terminal/Consola para ejecución

## 📝 Características Técnicas

- ✅ Código siguiendo **PEP 8**
- ✅ **Type hints** para mejor documentación
- ✅ **Docstrings** completos en todas las funciones
- ✅ Manejo de errores con **try-except**
- ✅ Validación de entrada de usuario
- ✅ Manejo de **KeyboardInterrupt** para salida graceful
- ✅ Funciones recursivas para cálculos
- ✅ Modularización profesional

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Sistema desarrollado para gestión de proyectos de agencias de desarrollo web.

## 🐛 Reportar Problemas

Si encuentras algún problema o tienes sugerencias, por favor abre un issue en el repositorio.

## 🔄 Versión

**Versión actual:** 1.0.0

---

⭐ Si te gusta este proyecto, ¡dale una estrella!

