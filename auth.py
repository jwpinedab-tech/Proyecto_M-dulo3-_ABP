"""
Módulo de autenticación para el Sistema de Gestión de Proyectos.
Maneja el login de usuarios con validación de credenciales.
"""

# Base de datos simulada de usuarios (diccionario usuario: contraseña)
USUARIOS = {
    "admin": "1234",
    "jacqueline": "dev2025"
}

# Número máximo de intentos permitidos
MAX_INTENTOS = 3


def mostrar_encabezado():
    """
    Muestra un encabezado visual ASCII para el sistema de autenticación.
    """
    print("\n" + "=" * 60)
    print(" " * 10 + "╔═══════════════════════════════╗")
    print(" " * 10 + "║   SISTEMA DE AUTENTICACIÓN    ║")
    print(" " * 10 + "║   Agencia Desarrollo Web     ║")
    print(" " * 10 + "╚═══════════════════════════════╝")
    print("=" * 60 + "\n")


def login():
    """
    Función de login que solicita credenciales al usuario.
    Permite máximo 3 intentos antes de denegar el acceso.
    Usa break si el usuario acierta.
    
    Returns:
        str or None: Nombre de usuario si el login es exitoso, None si falla.
    """
    mostrar_encabezado()
    
    intentos = 0
    
    while intentos < MAX_INTENTOS:
        print(f"Intento {intentos + 1} de {MAX_INTENTOS}")
        print("-" * 60)
        
        usuario = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()
        
        # Validar credenciales
        if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
            print("\n" + "=" * 60)
            print(f"✅ ¡Bienvenido, {usuario}!")
            print("=" * 60 + "\n")
            break  # Salir del bucle si el usuario acierta
        
        intentos += 1
        
        if intentos < MAX_INTENTOS:
            print(f"\n❌ Credenciales incorrectas. Te quedan {MAX_INTENTOS - intentos} intento(s).\n")
        else:
            print("\n" + "=" * 60)
            print("❌ Acceso denegado. Has agotado todos los intentos.")
            print("=" * 60 + "\n")
            return None
    
    # Retornar el usuario si el login fue exitoso
    return usuario

