import PySimpleGUI as psg


class LoginScreen:
    def __init__(self):
        # Our content inside our screen
        screen = [[psg.Text("Username:"), psg.InputText()],
                  [psg.Text("Password:"), psg.InputText()],
                  [psg.Button("Login")]]

        # Create the Window
        window = psg.Window("Employee Login", screen)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == psg.WIN_CLOSED:  # if user closes window, exit out of window
                break
            elif event == "Login":
                psg.popup(values[0], "has successfully logged in.")
                break

        window.close()
