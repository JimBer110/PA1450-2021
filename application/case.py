class Case:
    def __init__(self,fips,admin2,provinceState,countryRegion,lastUpdate,lat,long_,confirmed,deaths,recovered,active,combinedKey,incidentRate,caseFatalityRatio):
        self.fips = fips
        self.admin2 = admin2
        self.provinceState = provinceState
        self.countryRegion = countryRegion
        self.lastUpdate = lastUpdate
        self.lat = lat
        self.long_ = long_
        self.confirmed = confirmed
        self.deaths = deaths
        self.recovered = recovered
        self.active = active
        self.combinedKey = combinedKey
        self.incidentRate = incidentRate
        self.caseFatalityRatio = caseFatalityRatio
    
    def getFips(self):
        return self.fips
    def getAdmin2(self):
        return self.admin2
    def getProvinceState(self):
        return self.provinceState
    def getCountryRegion(self):
        return self.countryRegion
    def getLastUpdate(self):
        return self.lastUpdate  
    def getLat(self):
        return self.lat
    def getLong(self):
        return self.long_
    def getConfirmed(self):
        return self.confirmed
    def getDeaths(self):
        return self.deaths
    def getRecovered(self):
        return self.recovered
    def getActive(self):
        return self.active
    def getCombinedKey(self):
        return self.combinedKey
    def getIncidentRate(self):
        return self.incidentRate
    def getCaseFatalityRatio(self):
        return self.caseFatalityRatio
  
