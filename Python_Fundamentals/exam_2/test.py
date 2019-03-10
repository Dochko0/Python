class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price


book_dict = {}
book_name,book_author,book_price = input().split()
book_dict[Book(book_name,book_author,book_price)] = 1

# for i in range(0, 3):
#     book_name, book_author, book_price = input().split()
#     if book_name in book_dict:
#         book_dict[Book(book_name, book_author, book_price)] += 1
#     else:
#         book_dict[Book(book_name, book_author, book_price)] = 1

for x in book_dict:
    print(x.name + ' ' + x.author + ' ' + x.price)
    print(f'Quantity = {book_dict[x]}')



