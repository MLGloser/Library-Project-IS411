from models import Book

def main():
    library = [
        Book("Под игото", "Иван Вазов", 1894, 25.00),
        Book("Тютюн", "Димитър Димов", 1951, 30.00),
        Book("Времеразделно", "Антон Дончев", 1964, 22.50)
    ]

    print("--- Списък с всички налични книги ---")
    for book in library:
        print(book.get_description())

    search_year = 1950
    print(f"\n--- Книги, издадени след {search_year} г. ---")
    for book in library:
        if book.year > search_year:
            print(f"Намерена: {book.title}")

    print("\n--- Промоция ---")
    print(library[0].apply_discount(10)) 

if __name__ == "__main__":
    main()
