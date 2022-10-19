import PySimpleGUI as psg

# Our content inside our screen
screen = [[psg.Text("Enter the employee you wish to view: "), psg.InputText()],
          [psg.Button("Submit")]]

# Create the Window
window = psg.Window("View Employee", screen)

event, values = window.read()

if event == psg.WIN_CLOSED:  # if user closes window, exit out of window
    window.close()

if event == "Submit":
    employeeDetailScreen = [[psg.Text("Employee: "), psg.Text(values[0])],
                            [psg.Text("Age: ")],  # Going to fetch these details from our database/dictionary. Not sure how yet.
                            [psg.Text("Email: ")],
                            [psg.Text("Phone Number: ")],
                            [psg.Text("Position: ")]]

    employeeDetailWindow = psg.Window("Viewing Employee Details", employeeDetailScreen).read()
    window.close()

window.close()
