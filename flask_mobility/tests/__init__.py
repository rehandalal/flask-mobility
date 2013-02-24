import unittest

from flask_mobility.tests.test_decorators import DecoratorsTestCase
from flask_mobility.tests.test_mobility import MobilityTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MobilityTestCase))
    suite.addTest(unittest.makeSuite(DecoratorsTestCase))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
