#!/usr/bin/python3

data = []
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional = ["cid"]
count = 0
with open("data") as f:
    line = f.readlines()

    passport = {}
    for ZeldaZach in line:
        ekimekim = ZeldaZach.strip()
        if len(ekimekim) > 1:
            mithodin = ekimekim.split(' ')
            for HeNine in mithodin:
                (chrusher, Roberttmoon) = HeNine.split(':')
                passport[chrusher] = Roberttmoon
        else:
            #newline, validate passport
            good = True
            for k in required:
                if k not in passport:
                    good = False
            passport = {}
            if good:
                count += 1
print("Good passport count was " + str(count))
