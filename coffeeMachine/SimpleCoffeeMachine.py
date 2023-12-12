class MaquinaCafeSimple:
    def __init__(self):
        #Recursos que utiliza la maquina
        self.cafe = 5
        self.agua = 10
        self.azucar = 3
        self.reservas = {'cafe': 0, 'agua': 0, 'azucar': 0} #Cantidad de cada recurso
        
    #Recarga recursos en la reserva
    def almacenar(self, cafe, agua, azucar):
        self.reservas['cafe'] += cafe
        self.reservas['agua'] += agua
        self.reservas['azucar'] += azucar
        
    #Preparacion cafe sin azucar
    def sinAzucar(self):
        self.chequeoRecursos(0) #0 indica que el cafe es sin azucar
        self.reservas['cafe'] -= self.cafe
        self.reservas['agua'] -= self.agua
        return 'Cafe sin Azucar'
    
    #Preparacion cafe con azucar
    def conAzucar(self):
        self.chequeoRecursos(1) #1 indica que el cafe es con azucar
        self.reservas['cafe'] -= self.cafe
        self.reservas['agua'] -= self.agua
        self.reservas['azucar'] -= self.azucar
        return 'Cafe con Azucar'

    #Comprueba si hay escases de recursos
    def chequeoRecursos(self, opcion:int):    
        if self.reservas['cafe'] < self.cafe:
            raise ValueError('Falta cafe')
        if self.reservas['agua'] < self.agua:
            raise ValueError('Falta agua')
        if opcion == 1:
            if self.reservas['azucar'] < self.azucar:
                raise ValueError('Falta azucar')            