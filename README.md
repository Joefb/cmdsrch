# cmdsrch
## Quickly get an overview of linux commands

Linux has large amount of commands. While hardware hacking and obtaining root shells on IoT devices I found myself
Google searching for commands I was not familiar with to get an overview of what the command did. 
Due to the large amount of linux commands this took quite a bit of time. I wanted a quick way to get an overview
of the different commands.   

cmdsrch will take in a text file of linux commands, parse the file and give an overview of what the command does. You can also
feed it a single command. For instance when you ls a bin directory you can copy and paste the output or redirect the 
output into a text file then run cmdsrch on the file.

### Usage: python cmdsrch.py -Flag Option 
* Flags:
* -h: Prints help
* -p: Prints out dictionary of commands
* -f txtFile.txt: Searches dictionary for the commands in the txtFile.txt and displays results
* -c command: Searches dictionary the given command

* Examples:
* python3 cmdsrch.py -f myTxtFile.txt
* python3 cmdsearch -f ~/Documents/myTxtFile.txt
* python3 cmdsearch -c dir
* python3 cmdsrch -p

### The Dictionary File
The dictionary is by no means a complete list of all commands. I am still building the dictionary and adding new commands when
I come accross them.

The dictionary file cmdDict.py can be edited to add more commands or remove commands you may know.
