search_book = input()
num_book = int(input())
count_books = 0

while num_book > 0:
    curr_book = input()

    if curr_book == search_book:
        print(f'You checked {count_books} books and found it.')
        break

    num_book -= 1
    count_books += 1

if num_book == 0:
    print(f'The book you search is not here!')
    print(f'You checked {count_books} books.')
