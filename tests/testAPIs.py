import logging
import unittest

import StealthIM.apis.util
from StealthIM import logger


class TestUtil(unittest.TestCase):
    def test_ping(self):
        self.assertTrue(StealthIM.apis.util.ping("https://stim.cxykevin.top"))


if __name__ == '__main__':
    unittest.main()
