import keyboard

def onkeypress(event):
    print('You pressed: ', event.name)

keyboard.on_press(onkeypress)

while True:
    pass