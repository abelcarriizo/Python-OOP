def palindromes(word='str'):
    letters = '' #Letras almacenadas
    count = len(word) -1

    for x in range(len(word)): #Recorre la palabra
        letters += word[count]
        count -= 1
    #Verificación de la palabra    
    if word == letters: 
        return True
    else:
        return False

if __name__ == '__main__':
    p = palindromes('ana')
    print(p)
