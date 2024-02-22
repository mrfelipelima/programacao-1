class Ponto2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y

    def isEqual(self):
        return self.x == self.y
    
    def returnAsString(self):
        return 