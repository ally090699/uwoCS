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

class Flight:
    def __init__(self, flightNo, origAirport, destAirport):
        flightNo=str(flightNo)
        if isinstance(origAirport,Airport)==False or isinstance(destAirport,Airport)==False:
            raise TypeError("The origin and destination arguments must be Airport objects")
        elif flightNo[0].isupper()==False or flightNo[1].isupper()==False or flightNo[2].isupper()==False or flightNo[3].isdigit()==False or flightNo[4].isdigit()==False or flightNo[5].isdigit()==False:
            raise TypeError("The flight number format is incorrect")
        self._flightNo=flightNo
        self._origin=origAirport
        self._destination=destAirport
    def getFlightNumber(self):  
        return self._flightNo
    def getOrigin(self):
        return self._origin
    def getDestination(self):
        return self._destination
    def isDomesticFlight(self):
        return self._origin.getCountry()==self._destination.getCountry()
    def setOrigin(self,origin):
        self._origin=origin
    def setDestination(self,destination):
        self._destination=destination
    
    def __repr__(self):
        return "Flight("+self._flightNo+"): "+self._origin.getCity()+" -> "+self._destination.getCity()+" ["+("domestic" if self.isDomesticFlight() else "international")+"]"
    def __eq__(self, other):
        if isinstance(other,Flight)==False:
            return False
        elif self._origin==other.getOrigin() and self._destination==other.getDestination():
            return True

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
##############################################################

# from Aviation import Aviation

avi = Aviation()

flightsFileName = "flights.txt"

def equals (expected, student):
    expected = expected.replace(" ", "")
    expected = expected.replace("\t", "")
    expected = expected.lower()
    student = student.replace(" ", "")
    student = student.replace("\t", "")
    student = student.lower()
    return expected == student

#----- keep the code above this line uncommented ----------


# --------------- Test 1 - Airport methods ---------------

# a1 = Airport("YXU", "London", "Canada","North America")
# a2 = Airport("ABC", "Madrid", "Spain","Europe")
# a2.setCity("Athens")
# a2.setCountry("Greece")
# t1 = a1.getCode() == "YXU" and a1.getCity() == "London" and a1.getCountry() == "Canada"
# t2 = a2.getCode() == "ABC" and a2.getCity() == "Athens" and a2.getCountry() == "Greece"
# t3 = equals("YXU (London, Canada)", a1.__repr__()) and equals("ABC (Athens, Greece)", a2.__repr__())
# print('t1=',t1)
# print('t2=',t2)
# print('t2=',t3)
# if t1 and t2 and t3:
#     print("Test 1 Passed. (Airport methods)")
# else:
#     print("Test 1 Failed. (Airport methods)")


# --------------- Test 2 - Flight methods ---------------
# a1 = Airport("YXU", "London", "Canada","North America")
# a2 = Airport("ABC", "Athens", "Greece","Europe")
# f1 = Flight("ABC123", a1, a2)
# f2 = Flight("BCS101", Airport("ABQ", "Albuquerque", "United States","North America"), Airport("OMA", "Omaha", "United States","North America"))
# f3 = Flight("XYZ321", a1, a2)
# t1 = f1.getFlightNumber() == "ABC123" and f1.getOrigin() == a1 and f1.getDestination() == a2
# t2 = f1 != f2 and f1 == f3
# t3 = equals("Flight(ABC123): London -> Athens [international]", f1.__repr__()) and equals("Flight(BCS101): Albuquerque -> Omaha [domestic]", f2.__repr__())
# t4 = not(f1.isDomesticFlight()) and f2.isDomesticFlight()
#
# if t1 and t2 and t3 and t4:
#     print("Test 2 Passed. (Flight methods)")
# else:
#     print("Test 2 Failed. (Flight methods)")



# --------------- Test 3 - Exceptions ---------------
# a1 = Airport("YXU", "London", "Canada","North America")
# a2 = Airport("ABC", "Athens", "Greece","Europe")
# t1 = not(avi.loadData("junk.txt", "stuff.txt","random name . nothing"))
# t2 = len(avi._allAirports) == 0
# t3 = t4 = False
# try:
#     Flight("PNT175", "Toronto", "New York")
# except TypeError as e:
#     if e.__str__().strip().lower() == "the origin and destination arguments must be airport objects":
#         t3 = True
# try:
#     t4 = Flight("12#$cv", a1, a2)
# except TypeError as e:
#     if e.__str__().strip().lower() == "the flight number format is incorrect":
#         t4 = True
# if t1 and t2 and t3 and t4:
#     print("Test 3 Passed. (Exceptions)")
# else:
#     print("Test 3 Failed. (Exceptions)")


# --------------- Test 4 - loadData() ---------------

# t1 = avi.loadData("airports.txt", flightsFileName, "countries.txt")
# total = 0
# for i in avi._allFlights:
#     total += len(avi._allFlights[i])

# if t1 and len(avi._allAirports) == 37 and total == 60:
#     print("Test 4 Passed. (loadData())")
# else:
#     print("Test 4 Failed. (loadData())")


# # --------------- Test 5 - getAirportByCode() ---------------

# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# t1 = avi.getAirportByCode("ORD")

# if isinstance(t1, Airport) and t1.getCity() == "Chicago":
#     print("Test 5 Passed. (getAirportByCode())")
# else:
#     print("Test 5 Failed. (getAirportByCode())")



# # --------------- Test 6 - findAllCityFlights() ---------------

# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# cf = avi.findAllCityFlights("Toronto")
# cfs = ""
# for f in cf:
#     cfs += f.getFlightNumber() + " "
# t1 = isinstance(cf,list) and len(cf) == 6
# acodes = ['MCK533','QGC143','KPP582','CUN974','CFE916','AOK874 ']
# total = 0
# for a in acodes:
#     if a in cfs:
#         total += 1
# t2 = total == 6

# if t1 and t2:
#     print("Test 6 Passed. (findAllCityFlights())")
# else:
#     print("Test 6 Failed. (findAllCityFlights())")


# # --------------- Test 7 - findAllCountryFlights() ---------------

# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# cf = avi.findAllCountryFlights("Brazil")
# cfs = ""
# for f in cf:
#     cfs += f.getFlightNumber() + " "
# t1 = isinstance(cf,list) and len(cf) == 4
# acodes = ['YZF667','XGY802','MOO674','FFC468 ']
# total = 0
# for a in acodes:
#     if a in cfs:
#         total += 1
# t2 = total == 4

# if t1 and t2:
#     print("Test 7 Passed. (findAllCountryFlights())")
# else:
#     print("Test 7 Failed. (findAllCountryFlights())")


# # --------------- Test 8 - findFlightBetween() ---------------

# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# f1 = avi.findFlightBetween(avi.getAirportByCode("PVG"), avi.getAirportByCode("YOW"))
# f2 = avi.findFlightBetween(avi.getAirportByCode("LAX"), avi.getAirportByCode("DTW"))
# t1 = equals(f1, "Direct Flight(MTN376): PVG to YOW")
# t2 = f2 == -1

# if t1 and t2:
#     print("Test 8 Passed. (findFlightBetween())")
# else:
#     print("Test 8 Failed. (findFlightBetween())")


# # --------------- Test 9 - findFlightBetween() ---------------

# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# f1 = avi.findFlightBetween(avi.getAirportByCode("LAX"), avi.getAirportByCode("MIA"))
# t1 = isinstance(f1, set) and "CPT" in f1

# if t1:
#     print("Test 9 Passed. (findFlightBetween())")
# else:
#     print("Test 9 Failed. (findFlightBetween())")



# # --------------- Test 10 - findReturnFlight() ---------------

# # LOD619,MEX,LAX
# # LOX618,LAX,MEX

# # USO770,MEX,CPT
# # USO771,CPT,MEX

# #EKR896,SFO,YHZ

# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# f1 = avi.findFlightByNo('LOD619')
# f2 = avi.findFlightByNo('USO770')
# f3 = avi.findFlightByNo('EKR896')
# t1 = avi.findReturnFlight(f1)
# t1 = avi.findReturnFlight(t1)
# t2 = avi.findReturnFlight(f2)
# t2 = avi.findReturnFlight(t2)
# t3 = avi.findReturnFlight(f3)

# if f1 == t1 and f2 == t2 and t3 == -1:
#     print("Test 10 Passed. (findReturnFlight())")
# else:
#     print("Test 10 Failed. (findReturnFlight())")



# # --------------- Test 11 - findFlightsAcross() ---------------
# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# res=avi.findFlightsAcross('Atlantic')
# if res == {'XJX595', 'LJC201', 'DAJ762', 'MDW532', 'YZF667', 'JAG578', 'JKQ130', 'JHW048', 'YFZ738', 'CUN974', 'NIA196', 'VKG041', 'VIP930', 'YOF338', 'USO770', 'USO771'}:
#     print("Test 11 Passed. (findFlightsAcross('Atlantic'))")
# else:
#     print("Test 11 Failed. (findFlightsAcross('Atlantic'))")

# --------------- Test 12 - findFlightsAcross() ---------------
# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# res=avi.findFlightsAcross('Pacific')
# if res == {'MTN376', 'QMG091', 'VDT680', 'CSY487', 'YOI104', 'TYV528', 'KPP582', 'CSX772', 'ERO171', 'PGY075', 'YVF322', 'EYS649'}:
#     print("Test 12 Passed. (findFlightsAcross('Pacific'))")
# else:
#     print("Test 12 Failed. (findFlightsAcross('Pacific'))")
