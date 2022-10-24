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
                  [psg.Text("Status:")]]

        # Create the Window
        window = psg.Window("Employee Details", screen)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == psg.WIN_CLOSED:  # if user closes window, exit out of window
                break

        window.close()
