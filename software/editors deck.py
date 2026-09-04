import serial
import time
import pyautogui

# SETTINGS
SERIAL_PORT = "COM5"
BAUD_RATE = 115200

# CONNECT
print("Connecting to Arduino...")

arduino = serial.Serial(
    SERIAL_PORT,
    BAUD_RATE,
    timeout=0.01
)

time.sleep(2)

print("Arduino connected!")
print("Controller running.")
print("--------------------------------")

# INSTRUCTION DISPLAY
def show_instruction(symbol, instruction):
    print(f"   {symbol} {instruction}")

# LCD
def update_lcd(instruction):
    message = "LCD," + instruction + "\n"
    arduino.write(
        message.encode("utf-8")
    )

# EXECUTE COMMAND
def execute_command(command):
    command = command.strip()
    if not command:
        return

    # TIMELINE BACK
    if command == "TIMELINE_BACK":
        pyautogui.press("left")
        show_instruction(
            "←","Timeline Back"
        )

    # TIMELINE FORWARD
    elif command == "TIMELINE_FORWARD":
        pyautogui.press("right")
        show_instruction(
            "→","Timeline Forward"
        )

    # TIMELINE STOP
    elif command == "TIMELINE_STOP":
        pass

    # TIMELINE ZOOM IN
    elif command == "ZOOM_IN":
        pyautogui.hotkey(
            "ctrl","shift","+"
        )
        show_instruction(
            "↑","Timeline Zoom In"
        )

    # ZOOM OUT
    elif command == "ZOOM_OUT":
        pyautogui.hotkey(
            "ctrl","-"
        )

        show_instruction(
            "↓","Timeline Zoom Out"
        )

    # TRIM
    elif command == "TRIM":
        pyautogui.press("q")
        show_instruction(
            "Trim"
        )

    # COPY
    elif command == "COPY":
        pyautogui.hotkey(
            "ctrl","c"
        )
        show_instruction(
            "Copy"
        )

    # PASTE
    elif command == "PASTE":
        pyautogui.hotkey(
            "ctrl","v"
        )
        show_instruction(
            "Paste"
        )

    # DELETE
    elif command == "DELETE":
        pyautogui.press("delete")
        show_instruction(
            "Delete"
        )

    # INTERACTIVE EDITING
    elif command == "INTERACTIVE_EDITING":
        pyautogui.hotkey(
            "ctrl","j"
        )
        show_instruction(
            "Interactive Editing"
        )

    # PLAY / PAUSE
    elif command == "JOY_SW":
        pyautogui.press("space")
        show_instruction(
            "Play / Pause"
        )

    # REHYDRATE
    elif command == "REHYDRATE":
        print("💧 Rehydration reminder!")

    # READY
    elif command == "EDITORS DECK READY":
        print("Arduino ready.")

# SERIAL PROCESSING
def process_serial():
    latest_timeline = None
    normal_commands = []

    while arduino.in_waiting:
        raw = arduino.readline().decode(
            "utf-8",
            errors="ignore"
        ).strip()

        if not raw:
            continue

        # TIMELINE
        if raw == "TIMELINE_BACK":
            latest_timeline = "TIMELINE_BACK"

        elif raw == "TIMELINE_FORWARD":
            latest_timeline = "TIMELINE_FORWARD"

        elif raw == "TIMELINE_STOP":
            latest_timeline = "TIMELINE_STOP"

        # OTHER COMMANDS
        else:
            normal_commands.append(raw)

    # NORMAL COMMANDS
    for command in normal_commands:
        execute_command(command)

    # LATEST TIMELINE COMMAND
    if latest_timeline is not None:
        execute_command(latest_timeline)

# MAIN LOOP
try:

    while True:
        process_serial()
        time.sleep(0.001)

except KeyboardInterrupt:
    print("\nController stopped.")

finally:
    arduino.close()
    print("Serial connection closed.")
