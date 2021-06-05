import ykman
import os

print("Welcome to the config generator!")
print("")

print("Please insert all YubiKeys you want to use and remove any extras..")
input("Press [ENTER] to continue..")

devices = ykman.list_all_devices()

if len(devices) == 0 :
    print("\nNo YubiKeys found..")
    input("Press [ENTER] to quit..")
    quit()

print("\n%d YubiKey(s) will be used." % (len(devices)))
input("Press [ENTER] to continue..")

if len(devices) > 1 :
    requireAll = input("\nRequire all devices to be inserted at the same time? y/N ").lower().strip() == "y"
else :
    requireAll = True

command = input("\nEnter the command to execute, when the YubiKey(s) are not inserted:\n").strip()

invert = input("\nShould be the conditions inverted? (Insert required YubiKey(s) to execute) y/N ").lower().strip() == "y"

if invert :
    requireOnce = not input("\nRequire the YubiKey(s) to be inserted at least once on start, before the command gets executed? (Not effected by invert, still needs the YubiKey(s) to be plugged in) Y/n ").lower().strip() == "n"
else :
    requireOnce = not input("\nRequire the YubiKey(s) to be inserted at least once on start, before the command gets executed? Y/n ").lower().strip() == "n"

try :
    checkTime = int(input("\nHow often should we check for the YubiKey(s) in seconds? (Recommended: 5) "))
except ValueError :
    checkTime = 5

waitForInsert = input("\nShould we wait for the condtions to be met again, before we execute the command? y/N ").lower().strip() == "y"

try :
    os.remove("config.ini")
except :
    pass

with open("config.ini", "a") as f :
    f.write("[config]\n")
    f.write("requireAll = " + str(requireAll) + "\n")
    f.write("yubikeys = " + str(len(devices)) + "\n")

    i = 0

    for device in devices :
        i += 1
        serial = str(device[1].serial)

        f.write("key%d = %s" % (i, serial) + "\n")
    
    f.write("command = " + command + "\n")
    f.write("checkTime = " + str(checkTime) + "\n")
    f.write("requireOnce = " + str(requireOnce) + "\n")
    f.write("waitForInsert = " + str(waitForInsert) + "\n")
    f.write("invert = " + str(invert) + "\n")

input("\nConfig created!\nPress [ENTER] to quit..")