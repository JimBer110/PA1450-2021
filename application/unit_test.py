import unittest
from Tests import test_importer
from Tests import test_api

def runTests():
    suite = unittest.TestLoader().loadTestsFromModule(test_importer)
    unittest.TextTestRunner().run(suite)

    suite = unittest.TestLoader().loadTestsFromModule(test_api)
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    runTests()
