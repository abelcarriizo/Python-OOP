class MaquinaCafePremium:
    def __init__(self):
        #Ingredientes que utiliza cada cafe
        self.capuccino = {'cafe': 10, 'leche': 90, 'azucar': 3}
        self.cafeAmericano = {'cafe': 20, 'agua': 80, 'azucar': 3}
        self.cafeCortado = {'cafe': 20, 'leche': 10, 'agua': 70, 'azucar': 3}
        self.cafeConLeche = {'cafe': 50, 'leche': 50, 'azucar': 3}
        
        self.reservas = {'cafe': 0, 'leche': 0, 'agua': 0, 'azucar': 0} #Cantidad de cada recurso
        
    #Recarga recursos en la reserva
    def almacenar(self, cafe, leche, agua, azucar):
        self.reservas['cafe'] += cafe
        self.reservas['leche'] += leche
        self.reservas['agua'] += agua
        self.reservas['azucar'] += azucar
        
    def prepararCapuccino(self):
        self.chequeoRecursos('capuccino', 1) #Indica el tipo de cafe y si lleva azucar
        
        self.reservas['cafe'] -= self.capuccino['cafe']
        self.reservas['leche'] -= self.capuccino['leche']
        self.reservas['azucar'] -= self.capuccino['azucar']
    
    def prepararCafeAmericano(self):
        self.chequeoRecursos('americano', 1) #Indica el tipo de cafe y si lleva azucar
        
        self.reservas['cafe'] -= self.cafeAmericano['cafe']
        self.reservas['agua'] -= self.cafeAmericano['agua']
        self.reservas['azucar'] -= self.cafeAmericano['azucar']
    
    def prepararCafeCortado(self):
        self.chequeoRecursos('cortado', 1) #Indica el tipo de cafe y si lleva azucar
        
        self.reservas['cafe'] -= self.cafeCortado['cafe']
        self.reservas['leche'] -= self.cafeCortado['leche']
        self.reservas['agua'] -= self.cafeCortado['agua']
        self.reservas['azucar'] -= self.cafeCortado['azucar']
        
    def prepararCafeConLeche(self):
        self.chequeoRecursos('leche', 1) #Indica el tipo de cafe y si lleva azucar
        
        self.reservas['cafe'] -= self.cafeConLeche['cafe']
        self.reservas['leche'] -= self.cafeConLeche['leche']
        self.reservas['azucar'] -= self.cafeConLeche['azucar']
    
    def chequeoRecursos(self, tipo:str, azucar:int):
        
        #Chequeo Capuccino y Cafe con Leche
        if tipo == 'capuccino' or tipo == 'leche':
            if self.reservas['cafe'] < self.capuccino['cafe']:
                raise ValueError('Falta cafe')
            if self.reservas['leche'] < self.capuccino['leche']:
                raise ValueError('Falta leche')
            if azucar == 1:
                if self.reservas['azucar'] < self.capuccino['azucar']:
                    raise ValueError('Falta azucar')
        
        #Chequeo Cafe Americano
        if tipo == 'americano':
            if self.reservas['cafe'] < self.cafeAmericano['cafe']:
                raise ValueError('Falta cafe')
            if self.reservas['agua'] < self.cafeAmericano['agua']:
                raise ValueError('Falta agua')
            if azucar == 1:
                if self.reservas['azucar'] < self.capuccino['azucar']:
                    raise ValueError('Falta azucar')
                
        #Chequeo Cafe Americano
        if tipo == 'cortado':
            if self.reservas['cafe'] < self.cafeCortado['cafe']:
                raise ValueError('Falta cafe')
            if self.reservas['leche'] < self.cafeCortado['leche']:
                    raise ValueError('Falta leche')
            if self.reservas['agua'] < self.cafeCortado['agua']:
                raise ValueError('Falta agua')
            if azucar == 1:
                if self.reservas['azucar'] < self.capuccino['azucar']:
                    raise ValueError('Falta azucar')