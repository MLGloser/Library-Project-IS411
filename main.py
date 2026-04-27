from models import Book

def main():
    # Създаваме списък с обекти от класа Book
    library = [
        Book("Под игото", "Иван Вазов", 1894, 25.00),
        Book("Тютюн", "Димитър Димов", 1951, 30.00),
        Book("Времеразделно", "Антон Дончев", 1964, 22.50)
    ]

    print("--- Списък с всички налични книги ---")
    for book in library:
        print(book.get_description())

    # Търсене на книги след определена година (условно изражение)
    search_year = 1950
    print(f"\n--- Книги, издадени след {search_year} г. ---")
    for book in library:
        if book.year > search_year:
            print(f"Намерена: {book.title}")

    # Прилагане на отстъпка за конкретна книга (използване на метод)
    print("\n--- Промоция ---")
    print(library[0].apply_discount(10)) # 10% отстъпка за първата книга

if __name__ == "__main__":
    main()