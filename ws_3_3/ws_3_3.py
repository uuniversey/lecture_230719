

from book import decrease_book


def rental_book(name, pre_book):
    return print(f'{name}님이 {pre_book}권의 책을 대여하였습니다.')


name = '홍길동'
book_num = 3
pre_book = decrease_book(book_num)


print('남은 책의 수 :', str(pre_book))
rental_book(name, book_num)


