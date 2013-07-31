
import sys


# Learning about arguments:
for arg in sys.argv:
    print arg

jsClassName = sys.argv[1]
print "className:"
print jsClassName


def saveToFile(_string, newFilePath):
    "Saves the string to a file."
    file = open(newFilePath, "w+")
    file.write(_string)
    file.close()


if jsClassName:
    pathToFile = jsClassName + ".js"
    print pathToFile
    saveToFile("//Sample Javascript Class:", pathToFile)


# Learning about python regex:
import re
