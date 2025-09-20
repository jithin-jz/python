# 🔹 1. Book Class

# Create a class Book with attributes title, author, and price.

# Add a method get_info() that prints the book details.

# Create 3 books and display their information.

class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    # def get_info(self):
    #     print(f"Book name {self.title} author {self.author} and price {self.price}")

    def __str__(self) -> str:
        return f'Book name: {self.title}, author:{self.author},price: ${self.price}'

book1 = Book("The wild", "Androw", 100)
book2 = Book("Thought", "Abus", 199)
book3 = Book("Let it go", "jithin", 1000)

# book1.get_info()
# book2.get_info()
# book3.get_info()
print(book1,book2,book3,sep='\n')