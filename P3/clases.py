class Servicio:
    def __init__(self, codigo, nombre, servicio, importe):
        self.codigo = codigo
        self.nombre = nombre
        self.servicio = servicio
        self.importe = importe

    def __str__(self):
        return f"Identificacion: {self.codigo} Cliente: {self.nombre} Servicio: {self.servicio} Importe: {self.importe}"
