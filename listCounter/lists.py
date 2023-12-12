#Contar numeros repetidos de una lista
def searchNumbers(myList):
    repeated = dict() #Numeros repetidos almacenados 
    myList.sort()

    for number in myList: #Recorre la lista
        #Verificacion del numero
        if number in repeated:
            repeated[number] += 1
        if number not in repeated:
            repeated[number] = 1
    return repeated
        