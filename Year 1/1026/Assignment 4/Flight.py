from Airport import *
class Flight:
    def __init__(self, flightNo, origAirport, destAirport):
        flightNo=str(flightNo)
        if isinstance(origAirport,Airport)==False or isinstance(destAirport,Airport)==False:
            raise TypeError("The origin and destination must be Airport objects")
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