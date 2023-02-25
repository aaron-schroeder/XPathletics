import adspackage

import unittest


class TestDummy(unittest.TestCase):

  def test_my_func(self):
    self.assertIsNone(adspackage.my_func(), None)