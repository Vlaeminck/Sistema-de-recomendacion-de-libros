class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion


def agregar_libro(lista_libros):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    puntuacion = float(input("Ingrese la puntuación del libro: "))
    nuevo_libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado con éxito.")


def buscar_por_genero(lista_libros):
    genero = input("Ingrese el género a buscar: ")
    libros_encontrados = [libro.titulo for libro in lista_libros if libro.genero.lower() == genero.lower()]
    if libros_encontrados:
        print(f"Libros encontrados en el género '{genero}':")
        for titulo in libros_encontrados:
            print(f"- {titulo}")
    else:
        print(f"No se encontraron libros en el género '{genero}'.")


def recomendar_libro(lista_libros):
    genero = input("Ingrese el género de interés: ")
    libros_genero = [libro for libro in lista_libros if libro.genero.lower() == genero.lower()]
    if libros_genero:
        libro_recomendado = max(libros_genero, key=lambda x: x.puntuacion)
        print(f"Recomendación para el género '{genero}':")
        print(f"Título: {libro_recomendado.titulo}")
        print(f"Autor: {libro_recomendado.autor}")
        print(f"Puntuación: {libro_recomendado.puntuacion}")
    else:
        print(f"No hay libros disponibles en ese género '{genero}'.")


def main():
    lista_libros = []

    while True:
        print("\n--- Sistema de Recomendación de Libros ---")
        print("1. Agregar Libro")
        print("2. Buscar Libros por Género")
        print("3. Recomendar Libro")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_libro(lista_libros)
        elif opcion == "2":
            buscar_por_genero(lista_libros)
        elif opcion == "3":
            recomendar_libro(lista_libros)
        elif opcion == "4":
            print("Gracias por usar el Sistema de Recomendación de Libros. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
