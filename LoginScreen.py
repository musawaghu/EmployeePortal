# This is the login screen for employees
# Remember to install PySimpleGui and import

import PySimpleGUI as psg

#Our content inside our screen
screen = [[psg.Text('Username: '), psg.InputText()],
          [psg.Text('Password:'), psg.InputText()],
          [psg.Button('Login')]]

# Create the Window
window = psg.Window('Employee Login', screen)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED: # if user closes window
        break
    print(values[0], " has successfully logged in.")

window.close()
