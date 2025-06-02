# se creará el siguiente programa que permita llevar un registro de peliculas
import os

class catalogoPeliculas:
    def __init__(self, nombre):
        self.nombre = nombre + ".txt"

    def mostrar_menu(self):
        print("\n--- Menu de opciones ---")
        print("1. Agregar pelicula")
        print("2. Listar peliculas")
        print("3. Eliminar catalogo peliculas")
        print("4. Salir")

    def agregar_pelicula(self):
        nombre_pelicula= input("ingresa el nombre de la pelicula: ")
        with open(self.nombre, "a") as archivo:
             archivo.write(nombre_pelicula + "\n")
        print(f"Pelicula '{nombre_pelicula}' agregada correctamente.")

    def listar_peliculas(self):
        try:
            with open(self.nombre, "r") as archivo:
                peliculas= archivo.readlines()
                if peliculas:
                    print("\n--- Peliculas en el catalogo ---")
                    for i, pelicula in enumerate(peliculas):
                        print(f"{i+1}. {pelicula.strip()}")
                else:
                    print("el catalogo esta vacio.")
        except FileNotFoundError:
           print("el catalogo no existe.")

    def eliminar_catalogo(self):
        confirmacion= input("¿esta seguro de que desea eliminar el catalogo? (s/n):")
        if confirmacion.lower() == "s":
            try:
                os.remove(self.noombre)
                print("Catalogo eliminado correctamente.")
                return True
            except FileNotFoundError:
                print("el catalogo no existe")
        else:
            print("operacion cancelada.")
            return False
        
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opcion:")
            if opcion == "1":
                self.agregar_pelicula()
            elif opcion == "2":
                self.listar_peliculas()
            elif opcion == "3":
                if self.eliminar_catalogo():
                    break
            elif opcion == "4":
                print("usted ha salido del programa, gracias por participar, ¡vuelva pronto!")
                break
            else:
                print("opcion invalida. intentalo otra vez")

            

def main():
    nombre_catalogo= input("Por favor, ingresa un nombre para el catalogo de peliculas:")
    catalogo = catalogoPeliculas(nombre_catalogo)
    catalogo.ejecutar()


if __name__ == "__main__":
    main()
