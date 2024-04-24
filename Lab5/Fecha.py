class Fecha:

    def __init__(self, dd, mm,aa):
        self.dd = dd
        self.mm = mm
        self.yy = aa
        
    def setDia(self, dd):
        self.dd = dd
    def setMes(self, mm):
        self.mm = mm
    def setA(self, aa):
        self.yy = aa


    def getDia(self):
        return self.dd
    def getMes(self):
        return self.mm
    def getA(self):
        return self.yy
    

    def __str__(self):
        return f"{self.dd}-{self.mm}-{self.yy}"
    
