
from frequency import Frequency

import unittest
import time

class TestFrequency(unittest.TestCase):

    def setUp(self):
        self.freq=Frequency(0.5)

    def test_frequency(self):
        # make sure the shuffled sequence does not lose any elements

        st=time.time()

        self.freq.start()

        print '2 seconds'

        self.freq.end()

        self.freq.start()

        print '2 seconds'

        self.freq.end()

        self.freq.start()

        print '2 seconds'

        self.freq.end()

        end=time.time()

        self.assertTrue( end - st >= 2*3 )

if __name__ == '__main__':
    unittest.main()