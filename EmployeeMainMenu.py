import PySimpleGUI as psg
from CalendarView import *
from ViewEmployee import *


def main():
    import requests
    import json
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
            # the following code will validate the input and see if the employee exists in the database. It has some
            # errors, so its WIP. We call the API, and run a loop to search the employee, and print out if its a
            # valid entry or not
            """headers = {
                "Content-Type": "application/json",
                "Connection": "keep-alive",
            }
            try:
                request = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees") 
                jsonData = request.json()["Items"]
                for data in jsonData:
                    if saved_fn == data["firstName"] and (int(saved_id) == data["id"]):
                        print("if input is correct", saved_id, saved_fn)
                        psg.popup("has successfully logged in")
                        break
                    else:
                        print("if input is wrong", saved_id, saved_fn)
                        psg.popup("Incorrect Name and ID")
                        break

            except requests.exceptions.HTTPError as err:
                print(err)"""
            break
    LoginScreenWindow.close()

    MainMenuScreen = [[psg.Button("Profile", pad=(0, 15))],
                      [psg.Button("View Shift", pad=(0, 15))]
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
