"""API Base class"""
import datetime
import datetime_calendar
import recent_cases

class API:
    def __init__(self, data):
        self.data = data


    def reformatData(self, _case):
        case = {}
        case['country'] = _case.getCountryRegion()
        case['province'] = _case.getProvinceState()
        case['update'] = _case.getLastUpdate()
        case['confirmed'] = _case.getConfirmed()
        case['active'] = _case.getActive()
        case['deaths'] = _case.getDeaths()
        case['recovered'] = _case.getRecovered()
        return case


    def getAllData(self):
        tmp = []
        for i in range(len(self.data['cases'])):
            tmp.append(self.reformatData(self.data['cases'][i]))
        return {'cases': tmp}


    def getDataInTimespan(self, _from=None, _to=None):
        tmp = []

        if _from != None:
            _from = datetime.datetime.strptime(_from, "%Y-%m-%d")
        if _to != None:
            _to = datetime.datetime.strptime(_to, "%Y-%m-%d")

        for i in range(len(self.data['cases'])):
            if _from != None:
                if self.data['cases'][i].getLastUpdate() >= _from:
                    if _to != None:
                        if self.data['cases'][i].getLastUpdate() <= _to:
                            tmp.append(self.reformatData(self.data['cases'][i]))
                    else:
                        tmp.append(self.reformatData(self.data['cases'][i]))
            else:
                if _to != None:
                    if self.data['cases'][i] <= _to:
                        tmp.append(self.reformatData(self.data['cases'][i]))
                else:
                    tmp.append(self.reformatData(self.data['cases'][i]))

        tmp = sorted(tmp, key=lambda e: e['update'])

        return {'cases': tmp}


    def getCountries(self):
        tmp = {'countries': []}

        for key in self.data['countries'].keys():
            tmp['countries'].append(key)

        return tmp


    def getConfirmedCountryInTimespan(self, _from, _to):
        tmp = {}

        if _from != None:
            _from = datetime.datetime.strptime(_from, "%Y-%m-%d").strftime('%Y-%m-%d')
        if _to != None:
            _to = datetime.datetime.strptime(_to, "%Y-%m-%d").strftime('%Y-%m-%d')


        for key in self.data['countries'].keys():
            start = 0
            end = 0
            countryList = []
            for _key in self.data['countries'][key].keys():
                countryList += self.data['countries'][key][_key]
            for i in countryList:
                if self.data['cases'][i].getLastUpdate().strftime('%Y-%m-%d') == _from:
                    start += self.data['cases'][i].getConfirmed()
                if self.data['cases'][i].getLastUpdate().strftime('%Y-%m-%d') == _to:
                    end += self.data['cases'][i].getConfirmed()
            tmp[key] = end - start

        return tmp


    def getTotalCasesForCountryInTimespan(self, _from, _to, _country):
        tmp = {}
        _from = datetime.datetime.strptime(_from, "%Y-%m-%d")
        _to = datetime.datetime.strptime(_to, "%Y-%m-%d")

        for i in datetime_calendar.daterange(_from, _to):
            tmp[str(i.strftime('%Y-%m-%d'))] = 0
        if _country == "worldwide":
            for case in self.data['cases']:
                if case.getLastUpdate().strftime('%Y-%m-%d') in tmp.keys():
                    if case.getConfirmed() != None:
                        tmp[str(case.getLastUpdate().strftime('%Y-%m-%d'))] += case.getConfirmed()

        else:
            for case in self.data['cases']:
                if case.getCountryRegion() == _country:
                    if case.getLastUpdate().strftime('%Y-%m-%d') in tmp.keys():
                        tmp[str(case.getLastUpdate().strftime('%Y-%m-%d'))] += case.getConfirmed()
        return tmp

    def getListOfCountriesByNewCasesPerCap(self):
        result, countries = recent_cases.getListCountriesBasedOnNewCasesPerCapita()
        tmp = {'countries': []}
        for i in result:
            tmp['countries'].append((i, countries[i]))
        return tmp
