import PySimpleGUI as psg


class CalendarView:
    def __init__(self):
        layout = [
            [psg.Text("Date"), psg.InputText(key='Date'),
             psg.CalendarButton("Select Date", close_when_date_chosen=True, target="Date", format='%m/%d/%y',
                                size=(10, 1))],
            [psg.Submit()]]

        window = psg.Window("Calendar", layout)

        while True:
            event, values = window.read()
            if event == psg.WIN_CLOSED:
                break
            if event == "Submit":
                import requests
                selectedDate = values['Date']
                idList = []
                nameList = []
                headers = {
                    "Content-Type": "application/json",
                    "Connection": "keep-alive",
                }
                try:
                    request = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/attendance/all")
                    jsonData = request.json()["Items"]
                    request2 = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
                    jsonData2 = request2.json()["Items"]
                    for data in jsonData:
                        if selectedDate == data["scheduledDate"]:
                            idList.append(data["employeeID"])
                            for data2 in jsonData2:
                                if data["employeeID"] == str(data2["id"]):
                                    nameList.append(data2["firstName"])
                except requests.exceptions.HTTPError as err:
                    print(err)
                joinedList = "\n".join("Employee: {}\tID: {}\n".format(x, y) for x, y in zip(nameList, idList))
                psg.popup("List of employees and their ID's scheduled for: " + selectedDate, joinedList)
        window.close()
