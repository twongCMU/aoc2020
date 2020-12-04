#!/usr/bin/python3

import re

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
            print(str(passport))
            if "byr" not in passport or int(passport["byr"])<1920 or int(passport["byr"])>2002:
                print("Bad byr")
                good = False
            if "iyr" not in passport or int(passport["iyr"])<2010 or int(passport["iyr"])>2020:
                print("Bad iyr")
                good = False
            if "eyr" not in passport or int(passport["eyr"])<2020 or int(passport["eyr"])>2030:
                print("Bad eyr")
                good = False
            
            if "hgt" not in passport:
                print("Bad hgt")
                good = False
            else:
                if passport["hgt"][-2:] != "cm" and passport["hgt"][-2:] != "in":
                    print("Bad hgt cm/in")
                    good = False
                if passport["hgt"][-2:] == "cm" and (int(passport["hgt"][:-2])<150 or int(passport["hgt"][:-2])>193):
                    print("Bad hgt cm")
                    good = False
                if passport["hgt"][-2:] == "in" and (int(passport["hgt"][:-2])<59 or int(passport["hgt"][:-2])>76):
                    print("Bad hgt in")
                    good = False
            
            if "hcl" not in passport:
                print("Bad hcl")
                good = False
            else:
                if not re.search("^#[0-9a-f]{6}$", passport["hcl"]):
                    print("Bad hcl num")
                    good = False
            if "ecl" not in passport:
                print("Bad ecl")
                good = False
            else:
                if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    print("Bad ecl val")
                    good = False
            if "pid" not in passport:
                good = False
                print("Bad pid")
            else:
                if not re.search("^\d{9}$", passport["pid"]):
                    print("Bad pid digit")
                    good = False
            passport = {}
            if good:
                count += 1
print("Good passport count was " + str(count))
