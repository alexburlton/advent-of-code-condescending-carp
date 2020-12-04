import re
from dataclasses import dataclass
from typing import List, Optional

from utils import read_text_list, count_where

mandatory_fields: List[str] = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_eye_colors: List[str] = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


@dataclass
class PassportData:
    byr: Optional[str] = None
    iyr: Optional[str] = None
    eyr: Optional[str] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[str] = None
    cid: Optional[str] = None


def count_valid_passports(file_name: str) -> int:
    f = open(file_name, "r")
    raw_passports = f.read().split('\n\n')
    f.close()

    parsed_passports = [parse_passport(data) for data in raw_passports]
    return count_where(is_valid, parsed_passports)


def count_strict_valid_passports(file_name: str) -> int:
    f = open(file_name, "r")
    raw_passports = f.read().split('\n\n')
    f.close()

    parsed_passports = [parse_passport(data) for data in raw_passports]
    return count_where(is_strict_valid, parsed_passports)


def parse_passport(passport_data: str) -> PassportData:
    stripped_new_lines: str = passport_data.replace('\n', ' ')
    fields = stripped_new_lines.split(' ')
    passport = PassportData()
    for field in fields:
        name_and_value = field.split(':')
        setattr(passport, name_and_value[0], name_and_value[1])
    return passport


def is_valid(data: PassportData) -> bool:
    fields_present = [getattr(data, field) is not None for field in mandatory_fields]
    return all(fields_present)


def is_strict_valid(data: PassportData) -> bool:
    if not is_valid(data):
        return False

    return data.byr.isnumeric() and 1920 <= int(data.byr) <= 2002\
        and data.iyr.isnumeric() and 2010 <= int(data.iyr) <= 2020\
        and data.eyr.isnumeric() and 2020 <= int(data.eyr) <= 2030\
        and is_valid_height(data.hgt)\
        and is_valid_hair_color(data.hcl)\
        and data.ecl in valid_eye_colors\
        and len(data.pid) == 9 and data.pid.isnumeric()


def is_valid_height(hgt: str) -> bool:
    split = re.split('(\D+)', hgt)

    if len(split) < 2:
        return False

    value: str = split[0]
    if not value.isnumeric():
        return False

    units: str = split[1]
    if units == 'cm':
        return 150 <= int(value) <= 193
    elif units == 'in':
        return 59 <= int(value) <= 76
    else:
        return False


def is_valid_hair_color(hcl: str) -> bool:
    return re.match('^#([a-f0-9]{6})$', hcl) is not None


if __name__ == '__main__':
    print(count_valid_passports('day_4.txt'))
    print(count_strict_valid_passports('day_4.txt'))

