import os
def mostrar_menu():
    print("\nMenu de opciones:")
    print("1. Agregar pelicula")
    print("2. Listar peliculas")
    print("3. Eliminar catalogo peliculas")
    print("4. Salir")
def agregar_pelicula(nombre_catalogo):
    nombre_pelicula= input("ingresa el nombre de la pelicula: ")
    with open(nombre_catalogo, "a") as archivo:
        archivo.wrte(nombre_pelicula + "\n")
    print("Pelicula agregada correctamente.")

def listar_peliculas(nombre_catalogo):
    if os.path.exists(nombre_catalogo):
        with open(nombre_catalogo, "r") as archivo:
            peliculas= archivo.readlines()
            if peliculas:
                print("\nPeliculas en el catalogo:")
                for pelicula in peliculas:
                    print("-" + pelicula.strip())
            else:
                print("el catalogo esta vacio.")
    else:
        print("el catalogo no existe.")

def eliminar_catalogo(nombre_catalogo):
    confirmacion= input("¿esta seguro de que desea eliminar el catalogo? (s/n):")
    if confirmacion.lower() == "s":
        if os.path.exists(nombre_catalogo):
            os.remove(nombre_catalogo)
            print("catalogo eliminado correctamente.")
        else:
            print("operacion cancelada.")

def main():
    nombre_catalogo= input("ingrese el nombre del catalogo de peliculas:")
    if not os.path.exists(nombre_catalogo):
        with open(nombre_catalogo, "w") as archivo:
            print(f"catalogo '{nombre_catalogo}' creado.")
    else:
        print(f"catalogo '{nombre_catalogo}' abierto.")
    
    while True:
        mostrar_menu()
        opcion= input("seleccione una opcion: ")

        if opcion == "1":
            agregar_pelicula(nombre_catalogo)
        elif opcion == "2":
            listar_peliculas(nombre_catalogo)
        elif opcion == "3":
            eliminar_catalogo(nombre_catalogo)
        elif opcion == "4":
            print("salir del programa.")
            break
        else:
            print("opcion invalida. intente nuevamente")

if __name__ == "__main__":
    main()
