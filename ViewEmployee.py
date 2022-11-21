import PySimpleGUI as psg


class ViewEmployee:
    def __init__(self, firstName, id):
        import requests as requests
        import json
        self._firstName = firstName
        self._id = id

        headers = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",
        }
        try:
            request = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
            jsonData = request.json()["Items"]
            for data in jsonData:
                if firstName == data["firstName"] and (int(id) == data["id"]):
                    print(data["id"], data["firstName"], data["lastName"], data["email"])
                    if data["roleID"] == 1:
                        data["roleID"] = "Intern"
                    elif data["roleID"] == 2:
                        data["roleID"] = "Associate"
                    elif data["roleID"] == 3:
                        data["roleID"] = "Supervisor"
                    elif data["roleID"] == 4:
                        data["roleID"] = "Manager"
                    if data["roleID"] == 5:
                        data["roleID"] = "Executive"
                    screen = [[psg.Text("ID: "), psg.Text(data["id"])],
                              [psg.Text("First Name:"), psg.Text(data["firstName"])],
                              [psg.Text("Last Name:"), psg.Text(data["lastName"])],
                              [psg.Text("Email: "), psg.Text(data["email"])],
                              [psg.Text("Date of Birth: "), psg.Text(data["dob"])],
                              [psg.Text("Phone: "), psg.Text(data["phone"])],
                              [psg.Text("Address:"), psg.Text(data["address"])],
                              [psg.Text("Position:"), psg.Text(data["roleID"])],
                              [psg.Text("Status:"), psg.Text(data["status"])],
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
                                          [psg.Text("Position:")],
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
                                        "firstName": values[0],
                                        "roleID": "3"
                                    }

                                    try:
                                        r = requests.patch(
                                            'https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employee/2',
                                            data=json.dumps(payload), headers=headers)
                                        print(r.status_code)
                                    except requests.exceptions.HTTPError as err:
                                        print(err)

                                editWindow.close()
                    window.close()

        except requests.exceptions.HTTPError as err:
            print(err)

