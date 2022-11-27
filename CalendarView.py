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
                headers = {
                    "Content-Type": "application/json",
                    "Connection": "keep-alive",
                }
                try:
                    request = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/attendance/all")
                    jsonData = request.json()["Items"]
                    for data in jsonData:
                        if selectedDate == data["scheduledDate"]:
                            idList.append(data["id"])
                            print(data["id"])

                except requests.exceptions.HTTPError as err:
                    print(err)
                psg.popup("This will display which employees have a shift on this day", selectedDate, *idList)
        window.close()
