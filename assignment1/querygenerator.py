class UserError(Exception):
    pass


class NonValidEntry(UserError):
    pass


def minmax(commandin):
    query = "SELECT * FROM employee"
    conditionalstring = ""
    optionIn = ""

    if (commandin == "age" or "sales" or "salary"):
        minselection = 0
        maxselection = 0
        while True:
            try:
                print()
                if(commandin == "age"):
                    optionIn = input("Enter the minimum age\n")
                elif(commandin == "sales"):
                    optionIn = input("Enter the minimum sales volume\n")
                elif(commandin == "salary"):
                    optionIn = input("Enter the minimum salary\
                                     in units of 1000\n")

                minselection = int(optionIn)
                if(minselection < 0):
                    raise NonValidEntry
                else:
                    break

            except ValueError:
                print("Please enter a integer 0 or greater")
            except NonValidEntry:
                print("Please enter a integer 0 or greater")

        while True:
            try:
                print()
                if(commandin == "age"):
                    print("The minium age is ", minselection)
                    optionIn = input("Enter the maximum age\n")
                elif(commandin == "sales"):
                    print("The minium sales volume is ", minselection)
                    optionIn = input("Enter the maximum sales volume\n")
                elif(commandin == "salary"):
                    print("The minium salary is $", minselection, "000")
                    optionIn = input("Enter the maximum\
                                     salary in units of 1000\n")
                maxselection = int(optionIn)
                if(maxselection < minselection):
                    raise NonValidEntry
                else:
                    break

            except ValueError:
                print("Please enter a integer 0 or greater")
            except NonValidEntry:
                print("Please enter a integer greater than the minimum")

        if(commandin == "age"):
            conditionalstring = " WHERE age > {} AND age < {}"\
                .format(minselection, maxselection)
        elif(commandin == "sales"):
            conditionalstring = " WHERE sales > {} AND sales < {}"\
                .format(minselection, maxselection)
        elif(commandin == "salary"):
            conditionalstring = " WHERE salary > {} AND salary < {}"\
                .format(minselection, maxselection)
    query += conditionalstring
    print(query)
    return query


def bmi():
    query = "SELECT * FROM employee"
    conditionalstring = ""
    conditions = ["u", "n", "o", "b"]
    while True:
        try:
            print()
            print("Current selected BMI conditions are -- ", end='')
            if ('u' in conditions):
                print("underweight, ", end='')
            if ('n' in conditions):
                print(" normal, ", end='')
            if ('o' in conditions):
                print(" overweight, ", end='')
            if ('b' in conditions):
                print(" obese.", end='')
            print()
            bmioptionIn = input("Enter corresponding value\
                                to add/remove query options:\
                                u underweight, n normal,\
                                o overweight,\
                                b obese\nOr enter f to finish\n")
            if(bmioptionIn in ['u', 'n', 'o', 'b', 'f']):
                if(bmioptionIn == 'f'):
                    break
                else:
                    if (bmioptionIn in conditions):
                        conditions.remove(bmioptionIn)
                    else:
                        conditions.insert(0, bmioptionIn)
            else:
                raise NonValidEntry

        except NonValidEntry:
            print("Please enter valid option")
    conditionalstring = " WHERE bmi = "
    check = False
    if('u' in conditions):
        conditionalstring += "'underweight' "
        check = True
    if('n' in conditions):
        if (check is True):
            conditionalstring += "OR bmi ="
        else:
            check = True
        conditionalstring += "'normal' "
    if('o' in conditions):
        if (check is True):
            conditionalstring += "OR bmi ="
        else:
            check = True
        conditionalstring += "'overweight' "
    if('b' in conditions):
        if (check is True):
            conditionalstring += "OR bmi= "
        conditionalstring += "'obese'"

    query += conditionalstring
    print(query)
    return query
