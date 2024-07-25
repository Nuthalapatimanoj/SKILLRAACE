class Book:
    def __init__(self, title, author, publisher, price, copies_sold):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._copies_sold = copies_sold

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def copies_sold(self):
        return self._copies_sold

    @copies_sold.setter
    def copies_sold(self, value):
        self._copies_sold = value

    def royalty(self):
        if self._copies_sold <= 500:
            return 0.10 * self._price * self._copies_sold
        elif self._copies_sold <= 1500:
            return (0.10 * self._price * 500) + (0.125 * self._price * (self._copies_sold - 500))
        else:
            return (0.10 * self._price * 500) + (0.125 * self._price * 1000) + (0.15 * self._price * (self._copies_sold - 1500))

class EBook(Book):
    def __init__(self, title, author, publisher, price, copies_sold, format):
        super().__init__(title, author, publisher, price, copies_sold)
        self._format = format

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        self._format = value

    def royalty(self):
        base_royalty = super().royalty()
        gst_deducted = base_royalty * 0.88 # Deducting 12% GST
        return gst_deducted

# Example usage
book_name = input("Enter book name:")
book_author = input("Enter book author:")
book_publisher = input("Enter book publisher:")
book_price=int(input("Enter book price"))
book_copies_sold=int(input("Enter number of copies_sold:"))
ebook_price=int(input("Enter ebook price"))
ebook_copies_sold=int(input("Enter number of ecopies_sold:"))
print("---BOOK DETAILS---\n","Name:",book_name,"Author:",book_author,"Publisher:",book_publisher,"Price:",book_price,"No_of_sold:",book_copies_sold)
print("---EBOOK DETAILS ---\n","Name:",book_name,"Author:",book_author,"Publisher:",book_publisher,"Price:",ebook_price,"No_of_sold:",ebook_copies_sold)
book =Book(book_name,book_author,book_publisher,book_price,book_copies_sold)
ebook = EBook(book_name,book_author,book_publisher,ebook_price,ebook_copies_sold, "PDF")

print(f"The royalty for the book is: {book.royalty()}")
print(f"The royalty for the ebook is: {ebook.royalty()}")
