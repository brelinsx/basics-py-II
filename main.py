# Añade una colección de libros
from libreria import add_book, list_books, books_by_author, book_exists
book_collection = [
    add_book("1984", "Orwell"),
    add_book("Dune", "Herbert")
]
# Muestra la colección de libros creada
print(book_collection)
print(list_books(book_collection))
# Busca un libro por el autor
print(books_by_author(book_collection, "Orwell"))
# Verifica si un libro está disponible
print(book_exists(book_collection, "Dune"))