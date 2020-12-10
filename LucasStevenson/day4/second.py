'''
https://adventofcode.com/2020/day/4#part2
'''
with open("input.txt") as f:
    arr = []
    string = ""
    for line in f:
        if line.strip():  # if there is no blank line
            string += line.rstrip() + " "
        else:
            arr.append(string)
            string = ""
    arr.append(string)

passports = []
for i in arr:
    keys = {}
    for j in i.split():
        key, val = j.split(":")[0], j.split(":")[1]
        if key != "cid":
            keys[key] = val
    passports.append(keys)


def checkPassport(obj):
    if (len(obj) < 7):
        return False

    # put all the conditions into variables. Split up the conditions into different variables to keep it somewhat neat
    conditions1 = int(obj["byr"]) >= 1920 and int(obj["byr"]) <= 2002 and int(obj["iyr"]) >= 2010 and int(
        obj["iyr"]) <= 2020 and int(obj["eyr"]) >= 2020 and int(obj["eyr"]) <= 2030

    conditions2 = False
    if obj["hgt"][-2:] == "in":
        conditions2 = int(obj["hgt"][:-2]) >= 59 and int(obj["hgt"][:-2]) <= 76
    elif obj["hgt"][-2:] == "cm":
        conditions2 = int(
            obj["hgt"][:-2]) >= 150 and int(obj["hgt"][:-2]) <= 193

    conditions3 = len((obj["pid"])) == 9 and obj["ecl"] in [
        "amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and obj["hcl"][0] == "#" and len(obj["hcl"]) == 7

    if conditions1 and conditions2 and conditions3:
        for i in obj["hcl"][1:]:
            if i not in ["0", "1", "2", '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                return False
        return True
    return False


validCount = 0
for passport in passports:
    if checkPassport(passport):
        validCount += 1
print(validCount)
