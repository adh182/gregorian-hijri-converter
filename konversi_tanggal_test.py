from HijriahMasehiKonverter import HijriahKeMasehi, MasehiKeHijriah
import unittest

class Test(unittest.TestCase):

	def test_hijri_1(self):
		year = 1421
		month = 1
		day = 1
		expected = "2000/4/6"
		test = HijriahKeMasehi(year, month, day)
		self.assertEqual(test.convert_to_gregorian(), expected)

	def test_hijri_2(self):
		year = 1444
		month = 10
		day = 12
		expected = "2023/5/3"
		test = HijriahKeMasehi(year, month, day)
		self.assertEqual(test.convert_to_gregorian(), expected)

	def test_hijri_3(self):
		year = 1342
		month = 2
		day = 29
		expected = "1923/10/11"
		test = HijriahKeMasehi(year, month, day)
		self.assertEqual(test.convert_to_gregorian(), expected)

	def test_gregorian_1(self):
		year = 1991
		month = 8
		day = 13
		expected = "1412/2/2"
		test = MasehiKeHijriah(year, month, day)
		self.assertEqual(test.convert_to_hijriah(), expected)

	def test_gregorian_2(self):
		year = 2000
		month = 28
		day = 1
		expected = "1423/1/22"
		test = MasehiKeHijriah(year, month, day)
		self.assertEqual(test.convert_to_hijriah(), expected)

	def test_gregorian_3(self):
		year = 2020
		month = 1
		day = 15
		expected = "1441/5/19"
		test = MasehiKeHijriah(year, month, day)
		self.assertEqual(test.convert_to_hijriah(), expected)

unittest.main()