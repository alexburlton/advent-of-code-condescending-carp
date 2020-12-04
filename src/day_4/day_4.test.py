import unittest

from src.day_4.day_4 import *


def make_valid_passport(byr: str = '1920', iyr: str = '2010', eyr: str = '2020', hgt: str = '150cm', hcl: str = '#aaaaaa', ecl: str = 'amb', pid='012345678') -> PassportData:
    return PassportData(byr, iyr, eyr, hgt, hcl, ecl, pid)


class TestDay4(unittest.TestCase):

    def test_parse_passport(self):
        parsed = parse_passport('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm')
        self.assertEqual(parsed, PassportData(ecl='gry', pid='860033327', eyr='2020', hcl='#fffffd', byr='1937', iyr='2017', cid='147', hgt='183cm'))

    def test_parse_passport_2(self):
        parsed = parse_passport('hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm')
        self.assertEqual(parsed, PassportData(ecl='brn', pid='760753108', eyr='2024', hcl='#ae17e1', byr='1931', iyr='2013', hgt='179cm'))

    def test_is_valid_all_fields(self):
        self.assertTrue(is_valid(
            PassportData(byr='foo', iyr='foo', eyr='foo', hgt='foo', hcl='foo', ecl='foo', pid='foo', cid='foo')))

    def test_is_valid_missing_cid(self):
        self.assertTrue(is_valid(
            PassportData(byr='foo', iyr='foo', eyr='foo', hgt='foo', hcl='foo', ecl='foo', pid='foo')))

    def test_is_strict_valid_byr(self):
        self.assertTrue(is_strict_valid(make_valid_passport(byr='1920')))
        self.assertTrue(is_strict_valid(make_valid_passport(byr='2002')))

        self.assertFalse(is_strict_valid(make_valid_passport(byr='1919')))
        self.assertFalse(is_strict_valid(make_valid_passport(byr='2003')))
        self.assertFalse(is_strict_valid(make_valid_passport(byr='asfa')))

    def test_is_strict_valid_iyr(self):
        self.assertTrue(is_strict_valid(make_valid_passport(iyr='2010')))
        self.assertTrue(is_strict_valid(make_valid_passport(iyr='2020')))

        self.assertFalse(is_strict_valid(make_valid_passport(iyr='2009')))
        self.assertFalse(is_strict_valid(make_valid_passport(iyr='2021')))
        self.assertFalse(is_strict_valid(make_valid_passport(iyr='asfa')))

    def test_is_strict_valid_eyr(self):
        self.assertTrue(is_strict_valid(make_valid_passport(eyr='2020')))
        self.assertTrue(is_strict_valid(make_valid_passport(eyr='2030')))

        self.assertFalse(is_strict_valid(make_valid_passport(eyr='2019')))
        self.assertFalse(is_strict_valid(make_valid_passport(eyr='2031')))
        self.assertFalse(is_strict_valid(make_valid_passport(eyr='asfa')))

    def test_is_stric_valid_hgt(self):
        self.assertTrue(is_strict_valid(make_valid_passport(hgt='150cm')))
        self.assertTrue(is_strict_valid(make_valid_passport(hgt='193cm')))
        self.assertTrue(is_strict_valid(make_valid_passport(hgt='59in')))
        self.assertTrue(is_strict_valid(make_valid_passport(hgt='76in')))

        self.assertFalse(is_strict_valid(make_valid_passport(hgt='149cm')))
        self.assertFalse(is_strict_valid(make_valid_passport(hgt='194cm')))
        self.assertFalse(is_strict_valid(make_valid_passport(hgt='58in')))
        self.assertFalse(is_strict_valid(make_valid_passport(hgt='77in')))
        self.assertFalse(is_strict_valid(make_valid_passport(hgt='cm')))
        self.assertFalse(is_strict_valid(make_valid_passport(hgt='100')))
        self.assertFalse(is_strict_valid(make_valid_passport(hgt='100mm')))

    def test_is_strict_valid_hcl(self):
        self.assertTrue(is_strict_valid(make_valid_passport(hcl='#000000')))
        self.assertTrue(is_strict_valid(make_valid_passport(hcl='#999999')))
        self.assertTrue(is_strict_valid(make_valid_passport(hcl='#af09fa')))
        self.assertTrue(is_strict_valid(make_valid_passport(hcl='#abcdef')))

        self.assertFalse(is_strict_valid(make_valid_passport(hcl='0000000')))
        self.assertFalse(is_strict_valid(make_valid_passport(hcl='#bcdefg')))
        self.assertFalse(is_strict_valid(make_valid_passport(hcl='#00000z')))
        self.assertFalse(is_strict_valid(make_valid_passport(hcl='#000')))
        self.assertFalse(is_strict_valid(make_valid_passport(hcl='#abcde')))
        self.assertFalse(is_strict_valid(make_valid_passport(hcl='#abcdeff')))
        self.assertFalse(is_strict_valid(make_valid_passport(hcl='##abcde')))

    def test_is_strict_valid_ecl(self):
        self.assertTrue(is_strict_valid(make_valid_passport(ecl='amb')))
        self.assertTrue(is_strict_valid(make_valid_passport(ecl='blu')))
        self.assertTrue(is_strict_valid(make_valid_passport(ecl='brn')))
        self.assertTrue(is_strict_valid(make_valid_passport(ecl='gry')))
        self.assertTrue(is_strict_valid(make_valid_passport(ecl='grn')))
        self.assertTrue(is_strict_valid(make_valid_passport(ecl='hzl')))
        self.assertTrue(is_strict_valid(make_valid_passport(ecl='oth')))

        self.assertFalse(is_strict_valid(make_valid_passport(ecl='ylw')))

    def test_is_strict_valid_pid(self):
        self.assertTrue(is_strict_valid(make_valid_passport(pid='000000001')))
        self.assertTrue(is_strict_valid(make_valid_passport(pid='123456789')))
        self.assertFalse(is_strict_valid(make_valid_passport(pid='12345678')))
        self.assertFalse(is_strict_valid(make_valid_passport(pid='1234567899')))
        self.assertFalse(is_strict_valid(make_valid_passport(pid='12345678a')))
        self.assertFalse(is_strict_valid(make_valid_passport(pid='abcdefghi')))

    def test_not_valid_missing_mandatory_fields(self):
        self.assertFalse(is_valid(
            PassportData(iyr='foo', eyr='foo', hgt='foo', hcl='foo', ecl='foo', pid='foo', cid='foo')))
        self.assertFalse(is_valid(
            PassportData(byr='foo', eyr='foo', hgt='foo', hcl='foo', ecl='foo', pid='foo', cid='foo')))
        self.assertFalse(is_valid(
            PassportData(byr='foo', iyr='foo', hgt='foo', hcl='foo', ecl='foo', pid='foo', cid='foo')))
        self.assertFalse(is_valid(
            PassportData(byr='foo', iyr='foo', eyr='foo', hcl='foo', ecl='foo', pid='foo', cid='foo')))
        self.assertFalse(is_valid(
            PassportData(byr='foo', iyr='foo', eyr='foo', hgt='foo', ecl='foo', pid='foo', cid='foo')))
        self.assertFalse(is_valid(
            PassportData(byr='foo', iyr='foo', eyr='foo', hgt='foo', hcl='foo', pid='foo', cid='foo')))
        self.assertFalse(is_valid(
            PassportData(byr='foo', iyr='foo', eyr='foo', hgt='foo', hcl='foo', ecl='foo', cid='foo')))

    def test_count_valid_passports(self):
        self.assertEqual(count_valid_passports('day_4_example.txt'), 2)




if __name__ == '__main__':
    unittest.main()
