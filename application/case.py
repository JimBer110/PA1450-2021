class Case:

    def __init__(self):
        self.form = None
        #self.fips = None
        #self.admin2 = None
        self.provinceState = None
        self.countryRegion = None
        self.lastUpdate = None
        #self.lat = None
        #self.long_ = None
        self.confirmed = None
        self.deaths = None
        self.recovered = None
        self.active = None
        #elf.combinedKey = None
        #elf.incidentRate = None
        #elf.caseFatalityRatio = None
        #elf.IncidenceRate = None


    def getForm(self):
        return self.form
    #def getFips(self):
    #    return self.fips
    #def getAdmin2(self):
    #    return self.admin2
    def getProvinceState(self):
        return self.provinceState
    def getCountryRegion(self):
        return self.countryRegion
    def getLastUpdate(self):
        return self.lastUpdate
    #def getLat(self):
    #    return self.lat
    #def getLong(self):
    #    return self.long_
    def getConfirmed(self):
        return self.confirmed
    def getDeaths(self):
        return self.deaths
    def getRecovered(self):
        return self.recovered
    def getActive(self):
        return self.active
    #def getCombinedKey(self):
    #    return self.combinedKey
    #def getIncidentRate(self):
    #    return self.incidentRate
    #def getCaseFatalityRatio(self):
    #    return self.caseFatalityRatio
    #def getIncidenceRate(self):
    #    return self.caseIncidenceRate

    def setForm(self,form):
        self.form=form
    #def setFips(self,fips):
    #    self.fips=fips
    #def setAdmin2(self,admin2):
    #    self.admin2=admin2
    def setProvinceState(self,provinceState):
        self.provinceState=provinceState
    def setCountryRegion(self,countryRegion):
        self.countryRegion=countryRegion
    def setLastUpdate(self,lastUpdate):
        self.lastUpdate=lastUpdate
    #def setLat(self,lat):
    #    self.lat=lat
    #def setLong(self,long_):
    #    self.long_=long_
    def setConfirmed(self,confirmed):
        self.confirmed=confirmed
    def setDeaths(self,deaths):
        self.deaths=deaths
    def setRecovered(self,recovered):
        self.recovered=recovered
    def setActive(self,active):
        self.active=active
    #def setCombinedKey(self,combinedKey):
    #    self.combinedKey=combinedKey
    #def setIncidentRate(self,incidentRate):
    #    self.incidentRate=incidentRate
    #def setCaseFatalityRatio(self,caseFatalityRatio):
    #    self.caseFatalityRatio=caseFatalityRatio
    #def setIncidenceRate(self,IncidenceRate):
    #    self.IncidenceRate=IncidenceRate
