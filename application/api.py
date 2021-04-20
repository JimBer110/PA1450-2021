"""API Base class"""

class API:
    def __init__(self, data):
        self.data = data

    def getAlldata(self):
        tmp = []
        for i in range(len(self.data['cases'])):
            case = {}
            case['confirmed'] = self.data['cases'][i].getConfirmed()
            case['deaths'] = self.data['cases'][i].getDeaths()
            case['recovered'] = self.data['cases'][i].getRecovered()
            tmp.append(case)
        print(len(tmp))
        return {'cases': tmp}
