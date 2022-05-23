favorite_book=str(input())
book=str(input())
book_counter=0
true_counter=0
while book!="No More Books":
    book_counter+=1
    if favorite_book==book:
        book_counter-=1
        true_counter+=1
        print(f'You checked {book_counter} books and found it.')
        break
    book=str(input())
if true_counter==0:
    print(f'The book you search is not here!')
    print(f'You checked {book_counter} books.')