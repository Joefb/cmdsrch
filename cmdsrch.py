# cmdsrch Written by: Joe Burgess 2022
# cmdsrch accepts a txt file of linux commands and disply its basic function 
# This is designed to give a quick overview of linux commands

#!/usr/bin/python

import sys
import cmdDict


# Create lists
validCmds = []
invalidCmds = [] 

# Search dict for command 
def checkDict(word):
    for key in cmdDict.dict.keys():
        if key == word:
            return True
        
    return False

# Print all results 
def prntResults(): 
    print("Commands Found")
    print("########################################")
    for word in validCmds:
        print(word)

    print("")
    print("Commands not found")
    print("########################################")
    for word in invalidCmds:
        print(word)

# Open and parse txt file 
def parseFile(txtFile):
    with open(txtFile, 'r') as file:
        for line in file:
            for word in line.split():
                if checkDict(word) == True:
                    validCmds.append(word + ":" + cmdDict.dict[word]) 
                else:
                    invalidCmds.append(word + ": Command not found")

# Check single command
def chkCommand(cmd):
    if checkDict(cmd) == True:
        validCmds.append(cmd + ":" + cmdDict.dict[cmd])
    else:
        invalidCmds.append(cmd + ": Command not found")

# Print out help
def prntHelp():
    print("Usage: cmdsrch.py [Flag] [Option]")
    print("-h: Print help screen")
    print("-f file.txt: Search file.txt and display list of known coammnds")
    print("-c command: Search for single command and display results") 
    print("-p: Prints out dict")
    print("-a commandName \"command description\": Add command and description to dict")
    print("-r commandName: Remove command from dict")
    print("-e commandName \"new description\": Change command description in dict")
    sys.exit()

# Print out dict
def prntDict():
    for key,value in cmdDict.dict.items():
       print(key, ":", value) 
    sys.exit()

# Delete item from dict
def delItem(item):
    with open(cmdDict, 'a') as file:
        file.dict.pop(item)
    sys.exit()

# Check args 
def checkArgs():
    if len(sys.argv) == 1 or len(sys.argv) > 3 or sys.argv[1] == "-h":
        prntHelp()
    if sys.argv[1] == "-p":
        prntDict()
    # Need to figure out how to save data to cmdDict.py
    #if sys.argv[1] == "-r":
    #    delItem(sys.argv[2])
        #cmdDict.dict.pop(sys.argv[2])
        #sys.exit()
    if sys.argv[1] == "-f" and len(sys.argv) == 3:
        txtFile = sys.argv[2]
        parseFile(txtFile)
    elif sys.argv[1] == "-c" and len(sys.argv) == 3:
        chkCommand(sys.argv[2])
    else:
        prntHelp()


# Print results
#parseFile(txtFile)
checkArgs()
prntResults()
