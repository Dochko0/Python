class Book:
    def __init__(self, title, author, price, count_chapters):
        self.title = title
        self.author = author
        self.price = self.set_price(price)
        #self.chapters = chapters
        self.count_chapters = count_chapters

    def set_price(self, price):
        price = float(price)
        if price > 0:
            return price
        raise Exception


book_list = []
while True:
    read_row = input()
    if read_row == 'on work':
        break
    try:
        details_book, chapters_str = read_row.split(' -> ')
        chapters = list(chapters_str.split(', '))
        title_book, author_book, price_book = details_book.split()
        isCorrect = True
        for x in book_list:
            if x.title == title_book:
                isCorrect = False
        if isCorrect == True:
            book_list.append(Book(title_book, author_book, price_book, len(chapters)))
            #book_list.append(Book(title_book, author_book, price_book, chapters, len(chapters)))
    except:
        continue

curr_price = 0
sold = []
while True:
    read_order = input()
    if read_order == 'end work':
        break
    isHaveBook = False
    for x in book_list:
        if x.title == read_order:
            isHaveBook = True
            curr_price += x.price
            sold.append(
                'SOLD: ' + x.title + ' with author ' + x.author + '. Chapters in the book ' + str(x.count_chapters))

    if isHaveBook == False:
        print('No such book here')

if len(sold) == 0:
    print('Bad day :(')
else:
    for i in sold:
        print(i)
    print(f'Money: {curr_price:.2f}')
