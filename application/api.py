"""API Base class"""

class API:
    def __init__(self, data):
        self.data = data

    def getAllData(self):
        tmp = []
        for i in range(len(self.data['cases'])):
            case = {}
            case['country'] = self.data['cases'][i].getCountryRegion()
            case['province'] = self.data['cases'][i].getProvinceState()
            case['update'] = self.data['cases'][i].getLastUpdate()
            case['confirmed'] = self.data['cases'][i].getConfirmed()
            case['active'] = self.data['cases'][i].getActive()
            case['deaths'] = self.data['cases'][i].getDeaths()
            case['recovered'] = self.data['cases'][i].getRecovered()
            tmp.append(case)
        return {'cases': tmp}
