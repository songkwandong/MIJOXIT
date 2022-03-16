'''

특수 메서드를 이용하여 len() 새롭게 메소드 다른 용도로 정의를 해보는
실습

'''

class Book:
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self) -> str:
        return f"제목: {self.title}, 저자: {self.author}, 페이지수: "\
            + f"{self.pages}"
    #len() 함수를 페이지수를 리턴하게끔 만듬.
    def len(self):
        return self.pages

if __name__ == "__main__":
    book = Book("파이썬", "코딩형", 874)
    print(book)
    print(f"책의 페이지 수:{book.len()}")