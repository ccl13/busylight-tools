# PIP:
# python3 -m pip install busylight-for-humans
# python3 -m pip install PySimpleGUI

import PySimpleGUI as sg
from busylight.lights import Light

light = Light.first_light()

color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
color_yellow = (255, 255, 0)


# Define the layout of the window
layout = [
    [sg.Button('Red', size=(30, 7)), sg.Button('Green', size=(30, 7))],
    [sg.Button('Switch', size=(60, 7))],
]

# Create the window
window = sg.Window('Busy Light', layout, size=(600, 270),
                   auto_size_text=True)

# Event loop to handle button clicks
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Red':
        light.on(color_red)
    elif event == 'Green':
        light.on(color_green)
    elif event == 'Switch':
        if light.color == color_green:
            light.on(color_red)
        else:
            light.on(color_green)

# Release
light.off()

# Close the window
window.close()
