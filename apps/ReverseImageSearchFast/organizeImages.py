import os, os.path, sys

baseFolder = sys.argv[1]


# create folders
def createFolder(folder):
    if not os.path.exists(baseFolder +"/"+ folder):
        os.makedirs(baseFolder +"/"+ folder)

createFolder("val")
createFolder("test")
createFolder("train")

# Count files
nFiles = len([name for name in os.listdir(baseFolder) if os.path.isfile(baseFolder+"/"+name)])

# Put files in folder
fileCounter = 0
for name in os.listdir(baseFolder):
    filePath = baseFolder+"/"+name
    if os.path.isfile(filePath):
        if (fileCounter < int(0.33*nFiles)):
            os.rename(filePath, baseFolder+"/val/"+name)
        elif (fileCounter < int(0.66*nFiles)):
            os.rename(filePath, baseFolder+"/train/"+name)
        else:
            os.rename(filePath, baseFolder+"/test/"+name)

        fileCounter = fileCounter + 1
