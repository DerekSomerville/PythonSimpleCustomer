import csv, os
class ReadCSVFile:

    def fixWorkingDirectory(self):
        currentWorkingDirectory = os.getcwd()
        while "test" in currentWorkingDirectory or "src" in currentWorkingDirectory:
            os.chdir("../")
            currentWorkingDirectory = os.getcwd()

    def getFileData(self,fileName):
        self.fixWorkingDirectory()
        fileData = []
        with open("resource/" + fileName, 'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines(self, fileName, numerOfLines):
        return getFileData(fileName)[-1 * numerOfLines]