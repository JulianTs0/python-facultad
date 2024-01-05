class Pantalon:
    def __init__(self, codigo, nombre, largo, cintura, tela, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.largo = largo
        self.cintura = cintura
        self.tela = tela
        self.stock = stock

    def __str__(self):
        telas = ("Jean", "Gabardina", "Denim")
        return f"Codigo: {self.codigo} Nombre: {self.nombre} Largo: {self.largo} " \
               f"Cintura: {self.cintura} Tela: {telas[self.tela - 1]} Stock: {self.stock}"
