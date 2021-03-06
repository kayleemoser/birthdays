#!/usr/bin/env

#libraries
import sys
import unittest
import lob
from datetime import datetime, timedelta
#my modules
import birthday


##################
# Tests for Lib  #
##################

class TestContactClass(unittest.TestCase):

    def setUp(self):
        self.user = birthday.Contact("Harry Potter","07-31","4 Privet Drive","Little Whinging","Surrey","55555")

    def testCreateContact(self):
        self.assertEqual(self.user.name,"Harry Potter")
        self.assertEqual(self.user.birthday,"07-31")
        self.assertEqual(self.user.street,"4 Privet Drive")
        self.assertEqual(self.user.city,"Little Whinging")
        self.assertEqual(self.user.state,"Surrey")


class TestStateAbbreviation(unittest.TestCase):
    
    def testLowerCase(self):
        self.assertEqual(birthday.state_abbreviation("california"),"CA")
    
    def testCapitalizedCase(self):
        self.assertEqual(birthday.state_abbreviation("California"),"CA")

    def testUpperCase(self):
        self.assertEqual(birthday.state_abbreviation("CALIFORNIA"),"CA")

    def testWrongSpelling(self):
        self.assertFalse(birthday.state_abbreviation("californa"))


class Test3DayDate(unittest.TestCase):

    def testDate(self):
        #test with an old date
        date = datetime.strptime("02-09","%m-%d") #create datetime object from chosen date string
        future = birthday.futureBirthdays(date)
        self.assertEqual(future,"02-12")


if __name__ == '__main__':
    unittest.main()
