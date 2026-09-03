import serial
import time
import pyautogui


# =====================================================
# SETTINGS
# =====================================================

SERIAL_PORT = "COM5" # CHANGE THIS
BAUD_RATE = 115200


# =====================================================
# CONNECT
# =====================================================

print("Connecting to Arduino...")

arduino = serial.Serial(
    SERIAL_PORT,
    BAUD_RATE,
    timeout=1
)

time.sleep(2)

print("Arduino connected!")
print("Controller running.")
print("--------------------------------")


# =====================================================
# COMMAND MAPPING
# =====================================================

def execute_command(command):

    command = command.strip()

    if not command:
        return

    print("Received:", command)


    # =================================================
    # JOYSTICK
    # =================================================

    if command == "VOL_UP":

        pyautogui.hotkey("ctrl", ".")


    elif command == "VOL_DOWN":

        pyautogui.hotkey("ctrl", ",")


    elif command == "TIMELINE_BACK":

        pyautogui.press("left")


    elif command == "TIMELINE_FORWARD":

        pyautogui.press("right")


    # =================================================
    # UNDO / REDO
    # =================================================

    elif command == "UNDO":

        pyautogui.hotkey("ctrl", "z")


    elif command == "REDO":

        pyautogui.hotkey("ctrl", "y")


    # =================================================
    # BUTTONS
    # =================================================

    elif command == "TRIM":

        # Temporary mapping
        pyautogui.press("q")


    elif command == "CUT":

        # CapCut Windows split
        pyautogui.hotkey("ctrl", "b")


    elif command == "COPY":

        pyautogui.hotkey("ctrl", "c")


    elif command == "DELETE":

        pyautogui.press("delete")


    # =================================================
    # PLAY / PAUSE
    # =================================================

    elif command == "PLAY_PAUSE":

        pyautogui.press("space")


# =====================================================
# MAIN LOOP
# =====================================================

try:

    while True:

        if arduino.in_waiting:

            command = arduino.readline().decode(
                "utf-8",
                errors="ignore"
            )

            execute_command(command)


except KeyboardInterrupt:

    print("\nController stopped.")


finally:

    arduino.close()