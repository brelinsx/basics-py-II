"""
--------------------------- FUNCIONES ---------------------------
En este taller aprenderás a crear funciones en Python, desde las básicas hasta las que retornan valores, manejo de errores y excepciones, y su uso en clases.
"""


"""
--- Ejercicio 1: Función para Agregar Libros ---
Crea una función llamada `agregar_libro` que acepte dos parámetros, `titulo` y `autor`,
y que retorne un diccionario con el título y el autor del libro.
"""

# Escribe tu código aquí
# Prueba la función con algunos valores
def add_book(title, author):
    return {"title": title, "author": author}
"""
--- Ejercicio 2: Función para Listar Libros ---
Crea una función llamada `listar_libros` que acepte una lista de diccionarios `libros` y 
que retorne una lista con los títulos de los libros.
"""

# Escribe tu código aquí
def list_books(books):
    titles = []
    for book in books:
        titles.append(book["title"])
    return titles
# Prueba la función con algunos valores

print(list_books([{"title": "1984", "author": "Orwell"}]))

"""
--- Ejercicio 3: Función para Buscar Libros ---
Crea una función llamada `buscar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne el diccionario del libro que coincida con el título, o `None` si no se encuentra.
"""

# Escribe tu código aquí
def find_book(books, title):
    for book in books:
        if book["title"] == title:
            return book
    return None
# Prueba la función con algunos valores
book_collection = [
    {"title": "1984", "author": "Orwell"},
    {"title": "Dune", "author": "Herbert"}
]
print(find_book(book_collection, "Dune"))
print(find_book(book_collection, "Harry Potter"))
"""
--- Ejercicio 4: Manejo de Errores ---
Crea una función llamada `quitar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que intente quitar el libro con el título especificado. Si no se encuentra el libro, maneja el error adecuadamente.
"""

# Escribe tu código aquí
def remove_book(books, title):
    try:
        book = find_book(books, title)
        if book is None:
            raise ValueError(f"Book '{title}' not found")
        books.remove(book)
        return books
    except ValueError as error:
        print(error)
        return books
# Prueba la función con algunos valores
print(remove_book(book_collection.copy(), "Dune"))
print(remove_book(book_collection.copy(), "Harry Potter"))

"""
--- Ejercicio 5: Función que Retorna un Diccionario ---
Crea una función llamada `crear_inventario` que acepte una lista de diccionarios `libros` y 
que retorne un diccionario con la cantidad de libros por autor.
"""

# Escribe tu código aquí
def create_inventory(books):
    inventory = {}
    for book in books:
        author = book["author"]
        inventory[author] = inventory.get(author, 0) + 1
    return inventory
# Prueba la función con algunos valores
print(create_inventory(book_collection))
print(create_inventory([
    {"title": "1984", "author": "Orwell"},
    {"title": "Animal Farm", "author": "Orwell"},
    {"title": "Dune", "author": "Herbert"}
]))
"""
--- Ejercicio 6: Función que Retorna una Lista ---
Crea una función llamada `libros_por_autor` que acepte una lista de diccionarios `libros` y un `autor` y 
que retorne una lista con los títulos de los libros escritos por el autor especificado.
"""

# Escribe tu código aquí
def books_by_author(books, author):
    titles = []
    for book in books:
        if book["author"] == author:
            titles.append(book["title"])
    return titles
# Prueba la función con algunos valores
print(books_by_author(book_collection, "Orwell"))
"""
--- Ejercicio 7: Función que Retorna un Booleano ---
Crea una función llamada `existe_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne `True` si el libro existe en la lista, y `False` en caso contrario.
"""

# Escribe tu código aquí
def book_exists(books, title):
    return find_book(books, title) is not None
# Prueba la función con algunos valores
print(book_exists(book_collection, "Dune"))
print(book_exists(book_collection, "Harry Potter"))
