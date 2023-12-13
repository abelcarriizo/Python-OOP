class Compress:
    def __init__(self):
        self.texto = ''
        self.values = dict()
        self.compressed = list()
    
    def compress(self, archivo):
        texto = archivo.split(' ')
        
        #Añade cada palabra del texto a una lista
        palabras = list()
        for palabra in texto:
            if palabra not in palabras:
                palabras.append(palabra)
            
        #A partir de la cantidad de palabras generamos los indices
        indices = list()
        for palabra in palabras:
            indices.append(palabras.index(palabra)+1)
            
        #Crea diccionario de indices para cada persona.
        for i in range(len(palabras)):
            self.values[palabras[i]] = indices[i]
            
        #Agrega cada palabra a su indice
        for palabra in texto:
            self.compressed.append(self.values[palabra])
            
        return self.compressed, self.values
            
    def uncompress(self, compressed, values):
        
        for valorcito in compressed:
            for llave, valor in values.items():
                if valorcito == valor:
                    self.texto += llave + " "
        return self.texto.rstrip()       
    
if __name__=='__main__':
    compress = Compress()  
    