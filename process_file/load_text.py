#!/usr/bin/python
# Argument format:  SourceFile, TargetFile

# Imports:
import sys,os

# Functions:
def processFile(processFile, targetFile):
    try:
        source = open(sourceFile)
    except:
        print("Error opening",sourceFile,"for processing.")
        sys.exit(2)

    with open(targetFile,"a") as target:
        for line in source:
            target.write(line)

    source.close()

# Vars

# External Documentation
if len(sys.argv) == 1:
    print("The syntax for using this command is load_text <sourceFile> <targetFile>")
    print("A \".\" wildcard may be used in place of the sourcefile to process all txt files.")
    print("This process is non-destructive so provide a new target file or data will be appended to the existing one.")
    sys.exit()

# Arguments and File Setup
try:
    sourceFile = sys.argv[1]
    targetFile = sys.argv[2]
except:
    print("Please provide source and target files for procesing.")
    sys.exit(2)

sourceList = []
if sourceFile != ".":
    sourceList.append(sourceFile)
else:
    for file in os.scandir():
        if not file.is_dir() and file.name[-4:] == ".txt":
            sourceList.append(file.name)

# Read/Convert
for file in sourceList:
    print("Processing",file)
    processFile(file,targetFile)

print("Finished processing all files.")