#Abel Carrizo
from repository import Repository as repo

class BookService:
    
    def add_book(self, book):
        lastKey = 0
        for legajo in repo.booksList:
            lastKey = legajo
        lastKey += 1
        repo.booksList[lastKey] = book.__dict__
        return lastKey
    
    def update_book(self, bookKey, book_update):
        if bookKey not in repo.booksList:
            raise ValueError
        repo.booksList[bookKey] = book_update.__dict__
        
    def assign_book(self, id_book, member_legajo):
        if id_book not in repo.booksList:
            raise ValueError

        if member_legajo not in repo.membersList:
            raise ValueError

        repo.booksList[id_book]['_memberLegajo'] = member_legajo

    def delete_member(self, bookKey):
        if bookKey not in repo.booksList:
            raise ValueError
        del repo.booksList[bookKey]