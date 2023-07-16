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
        count = get_pixel(1, "Count")
        health = get_pixel(2, "Health")
        mana = get_pixel(3, "Mana")
        target_health = get_pixel(4, "TargetHP")
        in_range = get_pixel(5, "In range")
        combat = get_pixel(6, "Combat")
        brain_freeze = get_pixel(7, "Brain Freeze")
        fingers_of_frost = get_pixel(8, "fof")
        slot1 = get_pixel(9, "slot1")
        slot2 = get_pixel(10, "slot2")
        slot3 = get_pixel(11, "slot3")
        slot4 = get_pixel(12, "slot4")
        slot5 = get_pixel(13, "slot5")
        slot6 = get_pixel(14, "slot6")
        slot7 = get_pixel(15, "slot7")
        slot8 = get_pixel(16, "slot8")
        slot9 = get_pixel(17, "slot9")
        slot10 = get_pixel(18, "slot10")
        slot11 = get_pixel(19, "slot11")
        slot12 = get_pixel(20, "slot12")
        debuff1 = get_pixel(21, "Debuff1")
        isdead = get_pixel(22, "isdead?")

        # if not combat:
            #     if frost_armor == 0:
            #         press('e', 'shift')

            #     if arcane_intellect == 0:
            #         press('q', 'shift')

        if target_health > 0 and in_range:
            if debuff1 and slot9:
                press('f')
                continue
            
        if target_health > 0 and in_range:
            if slot7:
                press('7')
                continue

            if debuff1 and slot9: # Winter's Chill + Comet Storm
                press('f')
                continue

            # if debuff1 and slot1: # ray of frost
            #     press('f')
            #     continue

            if fingers_of_frost:
                press('2')
                continue

            if brain_freeze:
                press('3')
                continue

            press('q')
    else:
        print("No world of warcraft window found.")
