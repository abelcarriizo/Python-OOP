#Abel Carrizo
from repository import Repository as repo

class MemberService:
    
    #Añade miembros al repositorio
    def add_member(self, member):
        lastKey = 0
        for legajo in repo.membersList:
            lastKey = legajo
        lastKey += 1
        repo().membersList[lastKey] = member.__dict__
        return lastKey
    
    def update_member(self, legajo, member):
        if legajo not in repo.membersList:
            raise ValueError
        repo.membersList[legajo] = member.__dict__
        
    def delete_member(self, legajo):
        if legajo not in repo.membersList:
            raise ValueError
        del repo.membersList[legajo]