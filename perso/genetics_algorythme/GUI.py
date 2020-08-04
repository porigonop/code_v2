#!/usr/bin/env python
# https://github.com/PySimpleGUI/PySimpleGUI
import PySimpleGUI as sg
import random
import sys


class GUI:
    window = sg.Window('word matching engine')
    def __init__(self):
        layout = [
            [sg.Text('value to match:'), sg.Text(' ', key='-VALUE TO MATCH-')],
            [sg.Text('Best individual'), sg.Text(' ', key='-BEST INDIVIDUAL-')],
            [sg.Button('next generation')]
        ]
        self.window.layout(layout)
        self.window.finalize()



if __name__ == '__main__':
    gui = GUI()
