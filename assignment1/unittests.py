import unittest
import model
import view

model = model.Model()
view = view.View()


def testModelLength():
    outputValue = model.loadfile("C:\TestFile.txt")
    return outputValue


def testViewFields():
    outputValue = view.dataFields
    return outputValue


class Assignment1Tests(unittest.TestCase):

    def test_listIsCorrectLength(self):
        self.assertIs(len(testModelLength()), 5)

    def test_viewDataFieldsCorrect(self):
        self.assertEquals(testViewFields(), ("EMPID", "Gender", "Age", "Sales",
                                             "BMI", "Salary", "Birthday"))
