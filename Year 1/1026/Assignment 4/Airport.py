class Airport:
    def __init__(self, code, city, country, continent):
        self._code=code
        self._city=city
        self._country=country
        self._continent=continent
    def __repr__(self):
        return self._code+" ("+self._city+", "+self._country+")"
    def getCode(self):
        return self._code
    def getCity(self):
        return self._city
    def setCity(self, city):
        self._city=city
    def getCountry(self):  
        return self._country
    def setCountry(self, country):
        self._country=country
    def getContinent(self):  
        return self._continent
    def setContinent(self, continent):
        self._continent=continent