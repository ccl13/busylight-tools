# PIP:
# python3 -m pip install busylight-for-humans

from busylight.lights import Light
light = Light.first_light()

color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
color_yellow = (255, 255, 0)

while True:
    code = input('Enter command: ')
    code = code.lower()

    if code == "":
        if light.color == color_green:
            light.on(color_red)
        else:
            light.on(color_green)
    elif code == "q":
        light.off()
        quit()
    elif code == "r":
        light.on(color_red)
    elif code == "g":
        light.on(color_green)
    elif code == "b":
        light.on(color_blue)
    elif code == "y":
        light.on(color_yellow)
    elif code == "o":
        light.off()
