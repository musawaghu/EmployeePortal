import PySimpleGUI as psg

layout = [
    [psg.Text("Date"), psg.InputText(key='Date'),
     psg.CalendarButton("Select Date", close_when_date_chosen=True, target="Date", format='%Y:%m:%d', size=(10, 1))],
    [psg.Submit()]]

window = psg.Window("Calendar", layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == "Submit":
        psg.popup("This will display which employees have a shift on this day")  # this is a work in progress
window.close()
