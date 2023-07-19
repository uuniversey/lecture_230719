

number_of_book = 100

def decrease_book(num):
    global number_of_book
    exist_book = number_of_book - num
    return print('남은 책의 수 : ', exist_book)

name = '홍길동'
book_num = 3

decrease_book(book_num)
from ws_3_3.ws_3_3 import rental_book
