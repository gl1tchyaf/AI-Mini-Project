def normalCitizen(income):
    if 1 <= income <= 300000:
        print("Tax: ", (income*0))
    elif 300001 <= income <= 400000:
        print("Tax: ", (income*0.05))
    elif 400001 <= income <= 700000:
        print("Tax: ", (income*0.1))
    elif 700001 <= income <= 1100000:
        print("Tax: ", (income*0.15))
    elif 1100001 <= income <= 1600000:
        print("Tax: ", (income*0.2))
    else:
        print("Tax: ", (income*0.25))


def womenAndCitizenWithAgeGreaterThen65(income):
    if 1 <= income <= 350000:
        print("Tax: ", (income*0))
    elif 350001 <= income <= 450000:
        print("Tax: ", (income*0.05))
    elif 450001 <= income <= 750000:
        print("Tax: ", (income*0.1))
    elif 750001 <= income <= 1150000:
        print("Tax: ", (income*0.15))
    elif 1150001 <= income <= 1650000:
        print("Tax: ", (income*0.2))
    else:
        print("Tax: ", (income*0.25))


def Disabled(income):
    if 1 <= income <= 450000:
        print("Tax: ", (income*0))
    elif 450001 <= income <= 550000:
        print("Tax: ", (income*0.05))
    elif 550001 <= income <= 850000:
        print("Tax: ", (income*0.1))
    elif 850001 <= income <= 1250000:
        print("Tax: ", (income*0.15))
    elif 1250001 <= income <= 1750000:
        print("Tax: ", (income*0.2))
    else:
        print("Tax: ", (income*0.25))


def parentsOfDisabled(income):
    if 1 <= income <= 350000:
        print("Tax: ", (income*0.0))
    elif 350001 <= income <= 450000:
        print("Tax: ", (income*0.05))
    elif 450001 <= income <= 750000:
        print("Tax: ", (income*0.1))
    elif 750001 <= income <= 1150000:
        print("Tax: ", (income*0.15))
    elif 1150001 <= income <= 1650000:
        print("Tax: ", (income*0.20))
    else:
        print("Tax: ", (income*0.25))


def woundedFreedomFighters(income):
    if 1 <= income <= 475000:
        print("Tax: ", (income*0.0))
    elif 475001 <= income <= 575000:
        print("Tax: ", (income*0.05))
    elif 575001 <= income <= 875000:
        print("Tax: ", (income*0.1))
    elif 875001 <= income <= 1275000:
        print("Tax: ", (income*0.15))
    elif 1275001 <= income <= 1775000:
        print("Tax: ", (income*0.20))
    else:
        print("Tax: ", (income*0.25))


def main():
    while True:
        print("Enter your age: ")
        try:
            age = int(input())
        except ValueError:
            print("Please enter correct age")
            break

        print("Enter your Gender: ")
        print("1. Man: ")
        print("2. Women: ")
        try:
            gender = int(input())
        except ValueError:
            print("Please enter correct Gender")
            continue
        if gender != 1 and gender != 2:
            print("Please Enter 1 or 2")
            break

        print("Enter your Income: ")
        try:
            income = float(input())
        except ValueError:
            print("Please enter correct income")
            break

        print("Choose any criteria: ")
        print("1. Normal Citizen: ")
        print("2. Disabled: ")
        print("3. Parent of Disabled: ")
        print("4. Wounded Freedom Fighters: ")
        try:
            criteria = int(input())
        except ValueError:
            print("Please enter correct criteria")
            break

        if age > 65 or gender == 2:
            womenAndCitizenWithAgeGreaterThen65(income)
        else:
            if criteria == 1:
                normalCitizen(income)

            elif criteria == 2:
                Disabled(income)

            elif criteria == 3:
                parentsOfDisabled(income)

            elif criteria == 4:
                woundedFreedomFighters(income)

            else:
                print("Wrong Input")
        break


main()
