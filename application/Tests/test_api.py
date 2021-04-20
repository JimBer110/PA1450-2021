import unittest
import api
import case
from datetime import datetime

class TestApi(unittest.TestCase):

    def test_api(self):

        tmp = case.Case()
        tmp.setCountryRegion("US")
        tmp.setLastUpdate(datetime.fromisoformat('2021-04-02 04:20:36'))
        tmp.setConfirmed(1000)
        tmp.setDeaths(10)
        tmp.setRecovered(500)
        tmp.setActive(490)
        tmp.setProvinceState("Alabama")

        data = {'cases' : [tmp],
                'countries' : None}

        apiObject = api.API(data)

        result = apiObject.getAllData()


        self.assertEqual(result['cases'][0]['country'], tmp.getCountryRegion())
        self.assertEqual(result['cases'][0]['province'], tmp.getProvinceState())
        self.assertEqual(result['cases'][0]['update'], tmp.getLastUpdate())
        self.assertEqual(result['cases'][0]['confirmed'], tmp.getConfirmed())
        self.assertEqual(result['cases'][0]['active'], tmp.getActive())
        self.assertEqual(result['cases'][0]['deaths'], tmp.getDeaths())
        self.assertEqual(result['cases'][0]['recovered'], tmp.getRecovered())
