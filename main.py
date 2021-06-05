from os import system
import configparser
import ykman
import time

def foundRequiredYubiKeys(requiredYubiKeys, requireAll) :
    found = 0
    for device in ykman.list_all_devices() :
        serial = str(device[1].serial)
        if serial in requiredYubiKeys :
            found += 1

    if requireAll :
        return [found == len(requiredYubiKeys), found]
    else :
        return [found > 0, found]


config = configparser.ConfigParser()

try :
    config.read('config.ini')
    requireAll = config.get("config", "requireAll").lower() == "true"
    yubikeysCount = int(config.get("config", "yubikeys"))
    command = config.get("config", "command")
    checkTime = int(config.get("config", "checkTime"))
    requireOnce = config.get("config", "requireOnce").lower() == "true"
    waitForInsert = config.get("config", "waitForInsert").lower() == "true"
    invert = config.get("config", "invert").lower() == "true"
except :
    input("Config corrupted or not found.\nPress [ENTER] to quit..")
    quit()

yubikeys = []

for x in range(1, yubikeysCount + 1) :
    try :
        yubikeys.append(config.get("config", "key" + str(x)))
    except :
        input("Config corrupted.\nPress [ENTER] to quit..")
        quit()

print("Started!\n")

if requireOnce :
    print("Waiting for the required YubiKeys at least once before we start..")
    while True :
        if foundRequiredYubiKeys(yubikeys, requireAll) :
            print("Required YubiKeys found, starting..")
            break
        time.sleep(checkTime)

foundBefore = not invert

while True :
    output = foundRequiredYubiKeys(yubikeys, requireAll)
    if not invert :
        if not output[0] :
            if foundBefore or not waitForInsert :
                print("Required YubiKeys not found, executing command..")
                system(command)
                foundBefore = False
        else :
            if not foundBefore :
                foundBefore = True
                print("Required YubiKeys found, returning to normal..")
    else :
        if not output[0] :
            if foundBefore and output[1] == 0 :
                print("Required YubiKeys not found, returning to normal..")
                foundBefore = False
        else :
            if not foundBefore or not waitForInsert :
                foundBefore = True
                print("Required YubiKeys found, executing command..")
                system(command)
                foundBefore = True

    time.sleep(checkTime)