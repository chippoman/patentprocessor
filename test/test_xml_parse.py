#!/usr/bin/env python

import unittest
import imp
from yaml import load, dump

import xml_patent

#imp.load_source("xml_patent", "./")

class TestXMLParse(unittest.TestCase):

    def setUp(self):
        self.foo = 'bar'

    def test_dummy(self):
        assert(1 == 1)

if __name__ == '__main__':
    unittest.main()
