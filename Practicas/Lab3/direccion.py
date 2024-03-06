class Direccion:
    def __init__(
        self,
        calle: str,
        nomenclatura: str,
        barrio: str,
        ciudad: str,
        edificio: str,
        apto: str,
    ):
        self.calle = calle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad
        self.edificio = edificio
        self.apto = apto

    def setCalle(self, calle: str):
        self.calle = calle

    def setNomenclatura(self, nomenclatura: str):
        self.nomenclatura = nomenclatura

    def setBarrio(self, barrio: str):
        self.barrio = barrio

    def setCiudad(self, ciudad: str):
        self.ciudad = ciudad

    def setEdificio(self, edificio: str):
        self.edificio = edificio

    def setApt(self, apto: str):
        self.apto = apto

    def getCalle(self):
        return self.calle

    def getNomenclatura(self):
        return self.nomenclatura

    def getBarrio(self):
        return self.barrio

    def getCiudad(self):
        return self.ciudad

    def getEdificio(self):
        return self.edificio

    def getApto(self):
        return self.apto

    def __str__(self):
        return f"{self.calle} {self.nomenclatura} {self.barrio} {self.ciudad} {self.edificio} {self.apto}"
