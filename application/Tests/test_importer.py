import os
import unittest
import importer
import shutil
import case

class TestImporter(unittest.TestCase):

    def test_import(self):

        os.rename("covid_case_data", "covid_case_data.bak")
        os.mkdir("covid_case_data/")
        shutil.copy("Tests/example files/01-01-2020.csv", "covid_case_data/")

        data = importer.importData()

        shutil.rmtree("covid_case_data")
        os.rename("covid_case_data.bak", "covid_case_data")

        self.assertEqual(type(data), dict)

        self.assertEqual(type(data['cases']), list)

        self.assertEqual(len(data['cases']), 4)

        self.assertEqual(type(data['countries']), dict)

        self.assertEqual(type(data['cases'][0]), case.Case)

        self.assertEqual(data['cases'][0].getCountryRegion(), "Tunisia")

