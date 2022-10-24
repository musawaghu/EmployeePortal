import PySimpleGUI as psg

from LoginScreen import *
from CalendarView import *
from ViewEmployee import *


def main():
    LoginScreen()
    MainMenuScreen = [[psg.Button("Profile")],
                      [psg.Button("View Shift")]
                      ]

    MenuWindow = psg.Window("Employee Menu", MainMenuScreen)

    while True:
        event, values = MenuWindow.read()
        if event == psg.WIN_CLOSED:  # if user closes window, exit out of window
            break
        elif event == "Profile":
            ViewEmployee()
        elif event == "View Shift":
            CalendarView()

    MenuWindow.close()


main()
