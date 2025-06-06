
import re

USUARIO_ADMIN = 'admin'
CONTRASENA_ADMIN = 'admin123'

usuarios = {
    USUARIO_ADMIN: {'password': CONTRASENA_ADMIN, 'rol': 'admin'}
}

def validar_contrasena(contrasena):
    if len(contrasena) < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
        return False
    if not re.search(r'[A-Za-z]', contrasena):
        print("La contraseña debe contener al menos una letra.")
        return False
    if not re.search(r'\d', contrasena):
        print("La contraseña debe contener al menos un número.")
        return False
    return True

def registrar_usuario():
    print("\n--- Registro de nuevo usuario ---")
    nombre_usuario = input("Elige un nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("Ese usuario ya existe. Intenta con otro.")
        return
    while True:
        contrasena = input("Elige una contraseña (mínimo 6 caracteres, letras y números): ")
        if validar_contrasena(contrasena):
            break
    usuarios[nombre_usuario] = {'password': contrasena, 'rol': 'usuario'}
    print(f"Usuario '{nombre_usuario}' registrado correctamente.\n")

def iniciar_sesion():
    print("\n--- Iniciar sesión ---")
    nombre_usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    if nombre_usuario not in usuarios:
        print("Usuario no encontrado.\n")
        return None
    if usuarios[nombre_usuario]['password'] != contrasena:
        print("Contraseña incorrecta.\n")
        return None
    print(f"Bienvenido {nombre_usuario}!\n")
    return nombre_usuario

def mostrar_menu_admin():
    while True:
        print("\n--- Menú ADMIN ---")
        print("1. Ver usuarios")
        print("2. Cambiar rol")
        print("3. Eliminar usuario")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            print("\nUsuarios registrados:")
            for usuario_actual, info_usuario in usuarios.items():
                print(f"- {usuario_actual} (rol: {info_usuario['rol']})")
        
        elif opcion == '2':
            usuario_cambiar = input("Usuario a cambiar rol: ")
            if usuario_cambiar not in usuarios:
                print("Usuario no encontrado.")
                continue
            if usuario_cambiar == USUARIO_ADMIN:
                print("No se puede cambiar el rol del admin principal.")
                continue
            nuevo_rol = input("Nuevo rol (admin/usuario): ")
            if nuevo_rol not in ['admin', 'usuario']:
                print("Rol inválido.")
                continue
            usuarios[usuario_cambiar]['rol'] = nuevo_rol
            print(f"Rol de '{usuario_cambiar}' cambiado a '{nuevo_rol}'.")
        
        elif opcion == '3':
            usuario_eliminar = input("Usuario a eliminar: ")
            if usuario_eliminar not in usuarios:
                print("Usuario no encontrado.")
                continue
            if usuario_eliminar == USUARIO_ADMIN:
                print("No se puede eliminar al admin principal.")
                continue
            del usuarios[usuario_eliminar]
            print(f"Usuario '{usuario_eliminar}' eliminado.")
        
        elif opcion == '4':
            print("Cerrando sesión de admin.\n")
            break
        
        else:
            print("Opción inválida.")

def mostrar_menu_usuario(nombre_usuario):
    while True:
        print(f"\n--- Menú Usuario ({nombre_usuario}) ---")
        print("1. Ver perfil")
        print("2. Cerrar sesión")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            print(f"Usuario: {nombre_usuario}")
            print(f"Rol: {usuarios[nombre_usuario]['rol']}")
        
        elif opcion == '2':
            print("Cerrando sesión.\n")
            break
        
        else:
            print("Opción inválida.")

def main():
    while True:
        print("=== Sistema de Usuarios ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            nombre_usuario = iniciar_sesion()
            if nombre_usuario:
                if usuarios[nombre_usuario]['rol'] == 'admin':
                    mostrar_menu_admin()
                else:
                    mostrar_menu_usuario(nombre_usuario)
        elif opcion == '3':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()