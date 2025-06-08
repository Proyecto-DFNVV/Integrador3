from usuarios import registrar_usuario, iniciar_sesion
from administrador import menu_admin
from estandar import menu_estandar 

def main():
    usuarios = {
        "Florencia": {"contraseña": "flor123", "rol": "admin"},
        "Valeria": {"contraseña": "valeria456", "rol": "estandar"},
        "Najla": {"contraseña": "najla789", "rol": "estandar"},
        "Daniela": {"contraseña": "daniela321", "rol": "estandar"},
        "Veronica": {"contraseña": "vero654", "rol": "estandar"}
    }

    while True:
        print("\n=== Menú Principal Biblioteca Virtual \"Con Tonada\" ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            usuario, rol = iniciar_sesion(usuarios)
            if rol == "admin":
                menu_admin(usuario, usuarios) 
            elif rol == "estandar":
                menu_estandar(usuario, usuarios) 
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

