class Book:
  def __init__(self,title, author, book_id):
    self.title = title
    self.author = author
    self.book_id = book_id
    self.is_issued = False

  def display_book(self):
    print("Title:",self.title)
    print("Author:",self.author)
    print("Book Id:",self.book_id)

    if self.is_issued:
       print("Status: Issued")
    else:
       print("Status: Available")

  def issue_book(self):
    if self.is_issued:
        print("Book Already Issued")
    else:
        self.is_issued = True
        print("Book Issued Successfully")

  def return_book(self):
    if self.is_issued == True:
       print("Book Returned")
       self.is_issued = False
    else:
       print("Book Already Available")


b1 = Book("Python Basics", "ABC", 101)
b2 = Book("AI Fundamentals", "XYZ", 102)
books = [b1,b2]

found = False
book_id = int(input("Enter a book id:"))
for book in books:
    if book.book_id == book_id:
      found = True
      print("Book Found")
      book.display_book()

if not found:
  print("Book not found")

b1.display_book()
b1.issue_book()
b1.display_book()
b1.return_book()
b1.display_book()