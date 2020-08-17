import buttons
import display
import utime
import vibra

active = True
Pattern = [
    [10, 50, 10, 50, 10, 50, 10, 50,],
    [20, 50, 20, 50, 20, 50, 20, 50,],
    [30, 50, 30, 50, 30, 50, 30, 50,],
    [10,100, 30,100, 40,100, 50,100, 60,90, 70,80], 
    [15,30,],
    [15,30, 10,30,], #5
    [10,10, 10,10, 10,10],
    [10,30, 10,30, 10,30, 10,30,],
    [10,30, 15,30, 20,30,],
    [10,90, 30,90, 50,90, 70,90, 50,90, 30,90], 
    [20,0, 20,0, 20,0], 
    [5,20, 5,20, 5,20, 5,20, 5,20], #11
    ]
number = 0

def vibrate():
    if active:
        slp = False
        for i in Pattern[number]:
            if not slp:
                vibra.vibrate(i)
                slp = True
            else:
                utime.sleep_ms(i)
                slp = False

def lvl(text):
    with display.open() as disp:
        disp.clear()
        disp.print(text)
        disp.update()
    utime.sleep_ms(100)

def main():
    utime.sleep_ms(100) #Debounce for select Switch in Main Menu
    global active
    global number
    while True:
        pressed = buttons.read(
            buttons.BOTTOM_LEFT | buttons.BOTTOM_RIGHT | buttons.TOP_RIGHT
        )

        if pressed & buttons.BOTTOM_LEFT:
            number = max(0, number -1)
            utime.sleep_ms(100)
            while buttons.read(buttons.BOTTOM_LEFT): pass
            utime.sleep_ms(100)

        if pressed & buttons.BOTTOM_RIGHT:
            number = min(11, number +1)
            utime.sleep_ms(100)
            while buttons.read(buttons.BOTTOM_RIGHT): pass
            utime.sleep_ms(100)

        if pressed & buttons.TOP_RIGHT:
            active = not active
            utime.sleep_ms(100)
            while buttons.read(buttons.BOTTOM_TOP_RIGHT): pass
            utime.sleep_ms(100)


        vibrate()
        lvl(str(number))
        
main()
