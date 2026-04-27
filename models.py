class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def get_description(self):
        """Метод, който връща пълна информация за книгата."""
        return f"'{self.title}' от {self.author} ({self.year}) - {self.price} лв."

    def apply_discount(self, percent):
        """Метод за изчисляване на цена с отстъпка."""
        self.price = self.price * (1 - percent / 100)
        return f"Новата цена на '{self.title}' е {self.price:.2f} лв."