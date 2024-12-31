from Flight import *
from Airport import *
class Aviation:
    def __init__(self):
        self._allAirports={}
        self._allFlights={}
        self._allCountries={}
    
    def getAllAirports(self):
        return self._allAirports
    def getAllFlights(self):
        return self._allFlights
    def getAllCountries(self):
        return self._allCountries
    def setAllAirports(self,allAirports):
        self._allAirports=dict(allAirports)
    def setAllFlights(self,allFlights):
        self._allFlights=dict(allFlights)
    def setAllCountries(self,allCountries):
        self._allCountries=dict(allCountries)
    
    def loadData(self, airportFile, flightFile, countriesFile):
        self._allAirports={}
        self._allFlights={}
        self._allCountries={}
        try:
            with open(countriesFile,"r", encoding='utf8') as cntryFile:
                cntryFile=cntryFile.read()
                cntryArray=cntryFile.split("\n")
                for line in cntryArray:
                    line=line.split(",")
                    cleanLine=[]
                    for word in line:
                        word=word.strip()
                        cleanLine.append(word)
                    self._allCountries[cleanLine[0]]=cleanLine[1]
            with open(airportFile,"r", encoding='utf8') as arprtFile:
                arprtFile=arprtFile.read()
                arprtArray=arprtFile.split("\n")
                for line in arprtArray:
                    if line=="":
                        continue
                    else:
                        line=line.split(",")
                        cleanLine=[]
                        for word in line:
                            word=word.strip()
                            cleanLine.append(word)
                        item=Airport(cleanLine[0],cleanLine[2],cleanLine[1],self._allCountries[cleanLine[1]])
                        self._allAirports[cleanLine[0]]=item
            with open(flightFile,"r", encoding='utf8') as fltFile:
                fltFile=fltFile.read()
                fltArray=fltFile.split("\n")
                for line in fltArray:
                    line=line.split(",")
                    cleanLine=[]
                    for word in line:
                        word=word.strip()
                        cleanLine.append(word)
                    originalAir=self._allAirports[cleanLine[1]]
                    destAir=self._allAirports[cleanLine[2]]
                    item=Flight(cleanLine[0],originalAir,destAir)
                    if cleanLine[1] in self._allFlights:
                        self._allFlights[cleanLine[1]].append(item)
                    else:
                        flightList=[]
                        flightList.append(item)
                        self._allFlights[cleanLine[1]]=flightList
            return True
        except:
            return False

    
    def getAirportByCode(self, code):
        try:
            return self._allAirports[code]
        except:
            return -1
    
    def findAllCityFlights(self, city):
        listCity=[]
        for item in self._allFlights:
            for flight in self._allFlights[item]:
                origAir=flight.getOrigin()
                destAir=flight.getDestination()
                if city==origAir.getCity() or city==destAir.getCity():
                    listCity.append(flight)
        return listCity
    
    def findFlightByNo(self,flightNo):
        for item in self._allFlights:
            for flight in self._allFlights[item]:
                if flightNo==flight.getFlightNumber():
                    return flight
        return -1
    
    def findAllCountryFlights(self, country):
        listCountry=[]
        for item in self._allFlights:
            for flight in self._allFlights[item]:
                origAir=flight.getOrigin()
                destAir=flight.getDestination()
                if country==origAir.getCountry() or country==destAir.getCountry():
                    listCountry.append(flight)
        return listCountry
    
    def findFlightBetween(self, origAirport, destAirport):
        possibleAirportsList=set()
        pointA=[]
        pointC=[]
        for item in self._allFlights:
            for flight in self._allFlights[item]:
                origAir=flight.getOrigin()
                destAir=flight.getDestination()
                if origAirport.getCode()==origAir.getCode() and destAirport.getCode()==destAir.getCode():
                    return "Direct Flight("+flight.getFlightNumber()+"): "+origAirport.getCode()+" to "+destAirport.getCode()
                elif origAirport.getCode()==origAir.getCode():
                    pointA.append(flight)
                    continue
                elif destAirport.getCode()==destAir.getCode():
                    pointC.append(flight)
                    continue
        while pointA!=[] and pointC!=[]:
            for flightFrom in pointA:
                flightFromDest=flightFrom.getDestination()
                for flightTo in pointC:
                    flightToOrigin=flightTo.getOrigin()
                    if flightFromDest.getCode()==flightToOrigin.getCode():
                        possibleAirportsList.add(flightFromDest.getCode())
            return possibleAirportsList
        return -1
    
    def findReturnFlight(self, firstFlight):
        firstFlightOrigin=firstFlight.getOrigin()
        firstFlightDest=firstFlight.getDestination()
        for item in self._allFlights:
            for flight in self._allFlights[item]:
                flightOrigin=flight.getOrigin()
                flightDest=flight.getDestination()
                if firstFlightOrigin.getCode()==flightDest.getCode() and firstFlightDest.getCode()==flightOrigin.getCode():
                    return flight
        return -1
    
    def findFlightsAcross(self, ocean):
        greenZone=["North America","South America"]
        redZone=["Asia","Australia"]
        blueZone=["Africa","Europe"]
        pacificList=set()
        atlanticList=set()
        if ocean=="Pacific":
            for item in self._allFlights:
                for flight in self._allFlights[item]:
                    flightOrigin=flight.getOrigin()
                    flightDest=flight.getDestination()
                    if flightOrigin.getContinent() in greenZone and flightDest.getContinent() in redZone:
                        pacificList.add(flight.getFlightNumber())
                    elif flightDest.getContinent() in greenZone and flightOrigin.getContinent() in redZone:
                        pacificList.add(flight.getFlightNumber())
            return pacificList
        elif ocean=="Atlantic":
            for item in self._allFlights:
                for flight in self._allFlights[item]:
                    flightOrigin=flight.getOrigin()
                    flightDest=flight.getDestination()
                    if flightOrigin.getContinent() in greenZone and flightDest.getContinent() in blueZone:
                        atlanticList.add(flight.getFlightNumber())
                    elif flightDest.getContinent() in greenZone and flightOrigin.getContinent() in blueZone:
                        atlanticList.add(flight.getFlightNumber())
            return atlanticList
        return -1