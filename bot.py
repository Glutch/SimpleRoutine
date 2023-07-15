from tools import get_pixel, clear, press
import keyboard
import win32gui

def check_exit_hotkey():
    if keyboard.is_pressed('F2'): #knapp för att avsluta bot
        print("avslutar...")
        quit()

def get_active_window_title():
    window_handle = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window_handle)


clear()

while True:
    check_exit_hotkey()
    if get_active_window_title() == "World of Warcraft":
        health = get_pixel(1, "Health")
        mana = get_pixel(2, "Mana")
        target_health = get_pixel(3, "TargetHP")
        in_range = get_pixel(4, "In range")
        combat = get_pixel(5, "Combat")
        brain_freeze = get_pixel(6, "Brain Freeze")
        fingers_of_frost = get_pixel(7, "fof")
        slot1 = get_pixel(8, "slot1")
        slot2 = get_pixel(9, "slot2")
        slot3 = get_pixel(10, "slot3")
        slot4 = get_pixel(11, "slot4")
        slot5 = get_pixel(12, "slot5")
        slot6 = get_pixel(13, "slot6")
        slot7 = get_pixel(14, "slot7")
        slot8 = get_pixel(15, "slot8")
        slot9 = get_pixel(16, "slot9")
        slot10 = get_pixel(17, "slot10")
        slot11 = get_pixel(18, "slot11")
        slot12 = get_pixel(19, "slot12")
        debuff1 = get_pixel(20, "Debuff1")

        # if not combat:
            #     if frost_armor == 0:
            #         press('e', 'shift')

            #     if arcane_intellect == 0:
            #         press('q', 'shift')

        if target_health > 0 and in_range:
            if debuff1 and slot9:
                press('f')
                continue

            if fingers_of_frost:
                press('2')
                continue

            if brain_freeze:
                press('3')
                continue

        press('q')

    # global_cd = slot1