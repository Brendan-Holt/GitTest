import pymysql
import os
from querygenerator import minmax, bmi


class Model:
    'Contains assignment1 data'
    newQuery = ''

    def __init__(self):
        self.database = pymysql.connect("localhost", "root",
                                        "", "assignment1db")
        self.databaseCursor = self.database.cursor()

    def databaseClose(self):
        self.database.close()

    def databaseEmpty(self):
        self.databaseCursor.execute("DELETE FROM employee")

    def queryIn(self, commandin):
        if (commandin == "all"):
            self.databaseCursor.execute("""SELECT * FROM employee""")
        elif (commandin == "bmi"):
            self.newQuery = bmi()
            self.databaseCursor.execute(self.newQuery)
        elif (commandin == "age" or "sales" or "salary"):
            self.newQuery = minmax(commandin)
            self.databaseCursor.execute(self.newQuery)
        output = list(self.databaseCursor.fetchall())
        assert isinstance(output, object)
        return output

    def rebuild(self, buildfile):
        self.databaseEmpty()
        entryList = []
        lineList = open(buildfile).read().splitlines()
        for line in lineList:
            entryList.append(line.split(","))
        self.loaddatabase(entryList)

    def loadfile(self, realFilePath):
        entryList = []
        lineList = open(realFilePath).read().splitlines()
        for line in lineList:
            entryList.append(line.split(","))
        return entryList

    def loaddatabase(self, dataList):
        self.databaseEmpty()
        for item in dataList:
            self.databaseCursor.execute(
                """INSERT INTO employee (empid, gender, age, \
                sales, bmi, salary, \
                birthday) VALUES ('{}','{}','{}','{}','{}','{}','{}')"""
                .format(item[0], item[1], item[2], item[3], item[4],
                        item[5], item[6]))

    def addEmployee(self, dataList):
        self.databaseCursor.execute(
            """INSERT INTO employee (empid, gender, age, sales, bmi, salary, \
            birthday) VALUES ('{}','{}','{}','{}','{}','{}','{}')"""
            .format(dataList[0], dataList[1], dataList[2], dataList[3],
                    dataList[4], dataList[5], '1981-11-22'))

    def changeField(self, empidin, datafield, datavalue):
        self.databaseCursor.execute("""UPDATE employee SET {} = {} WHERE \
            empid = {}""".format(datafield, datavalue, empidin))

    def pie(self, commandIn):
        valueList = []
        valueList[:] = []

        if(commandIn == "sex"):
            self.databaseCursor.execute("""SELECT COUNT(gender) \
                FROM employee WHERE gender='F'""")
            data = self.databaseCursor.fetchone()
            value1 = int(data[0])
            self.databaseCursor.execute("""SELECT COUNT(gender) \
                FROM employee WHERE gender='M'""")
            data = self.databaseCursor.fetchone()
            value2 = int(data[0])
            valueList = [value1, value2]

        return valueList
