import PySimpleGUI as psg
from CalendarView import *
from ViewEmployee import *


def main():
    import requests
    import json
    from datetime import datetime
    from datetime import timedelta

    # Creating our login window for user to input
    LoginScreen = [[psg.Text("First Name:", size=(10, 1), justification="left"), psg.Input()],
                   [psg.Text("ID:", size=(10, 1), justification="left"), psg.Input()],
                   [psg.Button("Login", pad=(115, 25))]]

    LoginScreenWindow = psg.Window("Employee Login", LoginScreen, size=(300, 150))

    while True:
        # reading user's input and saving it to variables
        event, values = LoginScreenWindow.read()
        saved_fn = values[0]
        saved_id = values[1]
        # if user clicks on the "X" button, loop breaks and window ends
        if event == psg.WIN_CLOSED:
            break
        elif event == "Login":
            break

    LoginScreenWindow.close()

    # Code for finding BiWeekly Payments
    employeeID = saved_id  # set to whatever employee you want
    foundEmployee = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employee?id={}".format(employeeID))
    #print("Employee role ID:")
    #print(foundEmployee.json()["Item"]["roleID"])
    roleID = foundEmployee.json()["Item"]["roleID"]
    # Now that we have the role ID, let's find the employee's hourly rate
    foundRole = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/roles")
    hourlyRate = 0
    for item in foundRole.json()["Items"]:
        if item["id"] == roleID:
            hourlyRate = item["payRate"]
            break
    #print("Found hourly rate:")
    #print(hourlyRate)

    # Now we have our employee's hourly rate, let's find all the attendance records and payment records for the past 2 weeks

    # Get today's date, and date from 2 weeks ago
    todayDate = datetime.today().strftime('%m/%d/%Y')
    tod = datetime.now()
    d = timedelta(days=14)
    a = tod - d
    twoWeeksAgo = a.strftime('%m/%d/%Y')
    #print(todayDate)
    #print(twoWeeksAgo)

    paymentsCount = 0
    foundPayments = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/payments")
    for payment in foundPayments.json()["Items"]:
        if payment["employeeID"] == employeeID:
            paymentsCount += 1
    #print("Total payment records for employee:")
    #print(paymentsCount)

    # Multiply all by 8 hours and hourly rate to get total number of working hours payment
    preTaxIncome = paymentsCount * 8 * hourlyRate

    # Cut out 8% for income tax
    incomeTax = 0.08 * preTaxIncome

    # Final Payment
    postTaxBiweeklyPayment = preTaxIncome - incomeTax
    #print("Biweekly payment:")
    #print(postTaxBiweeklyPayment)
    # Main Menu Screen
    MainMenuScreen = [[psg.Button("Profile", pad=(0, 15))],
                      [psg.Button("View Shift", pad=(0, 15))],
                      [psg.Text("Your Biweekly Payment: $" + str(postTaxBiweeklyPayment))]
                      ]

    MenuWindow = psg.Window("Employee Menu", MainMenuScreen, size=(300, 150), element_justification="c")

    while True:
        event, values = MenuWindow.read()
        if event == psg.WIN_CLOSED:
            break
        elif event == "Profile":
            # Calling ViewEmployee class to show the employee's details, and passing in the variables from above
            ViewEmployee(saved_fn, saved_id)
        elif event == "View Shift":
            # calling CalendarView to show employee's shifts and co-workers on that specific shift
            CalendarView()

    MenuWindow.close()


main()
