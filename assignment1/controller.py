import sys
import model
import view
import pickle
import os


class UserError(Exception):
    pass


class NonValidEntry(UserError):
    pass


class NonValidArgument(UserError):
    pass


class NonValidPath(UserError):
    pass


def main():
    controller = Controller(True, sys.argv)
    controller.go()


class Controller:
    'Controller for assignment1'
    model = model.Model()
    view = view.View()
    dataList = []
    realFilePath = os.path.dirname(os.path.realpath(sys.argv[0]))

    def __init__(self, runController, options):
        self.runController = runController
        while True:
            try:
                if (len(sys.argv) == 1):
                    print()
                    break
                elif(sys.argv[1] == 'build'):
                    buildFile = sys.argv[2]
                    if (os.path.isfile(buildFile)):
                        self.model.rebuild(buildFile)
                        print()
                        break
                    else:
                        raise NonValidPath
                else:
                    raise NonValidArgument

            except NonValidArgument:
                print("The Argument ", sys.argv[1], " does not exist")
                sys.exit()
            except NonValidPath:
                print("The file ", sys.argv[2], "does not exist")
                sys.exit()

    def go(self):
        while (self.runController):
            commandIn = \
                self.view.getInput("Enter (press h for help, e to exit) ")
            if (commandIn == 'e'):
                self.model.databaseClose()
                sys.exit()
            elif (commandIn == 'h'):
                self.view.printHelp(os.path.dirname
                                    (os.path.realpath(sys.argv[0])))
            elif (commandIn in
                  ['all', 'id', 'gender',
                   'age', 'sales', 'bmi', 'salary', 'birthday']):
                self.view.displayOutput(self.model.queryIn(commandIn))
                while True:
                    try:
                        while (commandIn not in ['change', 'save', 'c']):
                            commandIn = self.view.\
                                getInput("Enter change to Change,"
                                         "save to Save to text file,"
                                         "c to return to Main ")
                            if (commandIn == 'save'):
                                fileName = "/files/" + self.view.\
                                    getInput("Give a name for the"
                                             " file to be saved as") + ".txt"
                                saveFile = open(os.path.dirname
                                                (os.path.realpath
                                                 (sys.argv[0])) +
                                                fileName, "w")
                                saveFile.write(self.view.fileData)
                                saveFile.close()
                                break
                            elif(commandIn == 'change'):
                                empid = self.view.\
                                    getInput("Enter the Employee"
                                             " ID to be changed")
                                datafield = self.view.\
                                    getInput("Enter the field to"
                                             "be changed")
                                datavalue = self.view.\
                                    getInput("Enter the value to"
                                             "change the field to")
                                self.model.changeField(empid,
                                                       datafield, datavalue)
                                print()
                        break
                    except ValueError:
                        print ("Please enter valid option")

            elif (commandIn == 'load'):
                realFilePath = os.path.\
                    dirname(os.path.realpath
                            (sys.argv[0])) + "/files/dbFile.txt"
                self.model.loaddatabase(self.model.loadfile(realFilePath))
                self.view.displayOutput(self.model.queryIn('all'))

            elif(commandIn == 'pwd'):
                print()

            elif (commandIn == 'pickle'):
                realFilePath = os.path.\
                    dirname(os.path.realpath
                            (sys.argv[0]))+"/files/pickle.dat"
                pickleData = self.model.queryIn('all')
                pickleOut = open(realFilePath, "wb")
                pickle.dump(pickleData, pickleOut)
                pickleOut.close()

            elif (commandIn == 'unpickle'):
                realFilePath = os.path.\
                    dirname(os.path.realpath
                            (sys.argv[0])) + "/files/pickle.dat"
                pickleIn = open(realFilePath, "rb")
                pickleData = pickle.load(pickleIn)
                pickleIn.close()
                data = []
                for item in pickleData:
                    data.append(item[1:8])
                self.model.loaddatabase(data)
                self.view.displayOutput(self.model.queryIn('all'))

            elif (commandIn == 'empty'):
                self.model.databaseEmpty()

            elif (commandIn == "pie"):
                dataList = []
                dataList[:] = []
                while True:
                    try:
                        commandIn = input("Show pie graph by 'age',"
                                          "'sex', 'bmi', 'sales' or 'salary'")
                        if(commandIn in ['age',
                           'sex', 'bmi', 'sales', 'salary']):
                            dataList = self.model.pie(commandIn)
                            break
                        else:
                            raise NonValidEntry
                    except NonValidEntry:
                        print ("Please make a selection from the following")

                self.view.displayPie(commandIn, dataList)

            elif (commandIn == "insert"):
                insertList = ['', '', '', '', '', '']
                insertList[0] = input("Enter Employee ID")
                insertList[1] = input("Enter Employee Sex")
                insertList[2] = input("Enter Employee age")
                insertList[3] = input("Enter Employee sales")
                insertList[4] = input("Enter Employee BMI")
                insertList[5] = input("Enter Employee Salary")
                self.model.addEmployee(insertList)


if __name__ == "__main__":
    main()
