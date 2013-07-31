import sys

# Getting our javascript class name
print sys.argv
if (sys.argv is False):
    print "Please provide className as first SHELL argument."
    sys.exit()
jsClassName = sys.argv[1]


print "Saving class File:"
print jsClassName


def getFileContents(pathToFile):
    file = open(pathToFile, "r+")
    justRead = file.read()
    file.close()
    return justRead


def saveToFile(_string, newFilePath):
    file = open(newFilePath, "w+")
    file.write(_string)
    file.close()

# Generates a simple class stube

# function within start and end strings


def generateJSFile(start, end, clasName):
    classString = "\n\tvar " + clasName + " = function(){\n\t};\n"
    return start + classString + end


# Saving Class file:


def saveClassFile(jsClassName):
    if jsClassName:
        pathToFile = jsClassName + ".js"
        print "Saved to:"
        print pathToFile
        start = getFileContents("start.js")
        end = getFileContents("end.js")
        generatedString = generateJSFile(start, end, jsClassName)
        saveToFile(generatedString, pathToFile)


saveClassFile(jsClassName)

