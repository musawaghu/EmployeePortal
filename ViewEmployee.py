import PySimpleGUI as psg


class ViewEmployee:
    def __init__(self):
        screen = [[psg.Text("ID: ")],
                  [psg.Text("First Name:")],
                  [psg.Text("Last Name:")],
                  [psg.Text("Email: ")],
                  [psg.Text("Date of Birth: ")],
                  [psg.Text("Phone: ")],
                  [psg.Text("Address:")],
                  [psg.Text("Role ID:")],
                  [psg.Text("Status:")],
                  [psg.Button("Edit Profile")]
                  ]

        # Create the Window
        window = psg.Window("Employee Details", screen)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == psg.WIN_CLOSED:  # if user closes window, exit out of window
                break
            elif event == "Edit Profile":
                editScreen = [[psg.Text("ID: ")],
                              [psg.Text("First Name:"), psg.InputText()],
                              [psg.Text("Last Name:"), psg.InputText()],
                              [psg.Text("Email: "), psg.InputText()],
                              [psg.Text("Date of Birth: "), psg.InputText()],
                              [psg.Text("Phone: "), psg.InputText()],
                              [psg.Text("Address:"), psg.InputText()],
                              [psg.Text("Role ID:")],
                              [psg.Text("Status:")],
                              [psg.Button("Save")]]
                editWindow = psg.Window("Edit Profile", editScreen)
                while True:
                    event, values = editWindow.read()
                    if event == psg.WIN_CLOSED:  # if user closes window, exit out of window
                        break
                    elif event == "Save":
                        import requests
                        import json

                        headers = {
                            "Content-Type": "application/json",
                            "Connection": "keep-alive",
                        }

                        payload = {
                            "firstName": "Chad",
                            "roleID": "3"
                        }

                        try:
                            r = requests.patch('https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employee/2',
                                               data=json.dumps(payload), headers=headers)
                            print(r.status_code)
                        except requests.exceptions.HTTPError as err:
                            print(err)

                    editWindow.close()
        window.close()
