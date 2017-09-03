import matplotlib.pyplot as plt
import os


class View:
    'View Functions'
    dataFields = ("EMPID", "Gender", "Age",
                  "Sales", "BMI", "Salary", "Birthday")
    fileData = ""

    def getInput(self, prompt):
        commandIn = input(prompt)
        return commandIn

    def displayOutput(self, output):
        fileData = ""
        for object in self.dataFields:
            print (object, " "*(15-len(object)), end='')
            self.fileData += object + " "*(15-len(object))
        self.fileData += "\n"
        print ()

        for item in output:
            for object in item[1:8]:
                object = str(object)
                print (object, " "*(15-len(object)), end='')
                self.fileData += object+" "*(15-len(object))
            self.fileData += "\n"
            print ()

    def displayPie(self, dataGroup, dataList):
        colours = ['c', 'm', 'r', 'k']

        if(dataGroup == 'sex'):
            label = ['Male', 'Female']
            graphTitle = "Employees by sex"

        plt.pie(dataList, labels=label, colors=colours, startangle=90)
        plt.title(graphTitle)
        plt.show()

    def printHelp(self, helpPath):
        helpfile = open(helpPath+"\helpfile.txt")
        str = helpfile.read()
        print("", str)
