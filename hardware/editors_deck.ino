#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// =====================================================
// PIN DEFINITIONS
// =====================================================

const int JOY_X  = A0;
const int JOY_Y  = A1;
const int JOY_SW = 6;

const int BUTTON_1 = 2;
const int BUTTON_2 = 3;
const int BUTTON_3 = 4;
const int BUTTON_4 = 5;

// =====================================================
// JOYSTICK CALIBRATION
// =====================================================

const int CENTER_X = 506;
const int CENTER_Y = 511;

const int DEADZONE = 150;

// =====================================================
// TIMING
// =====================================================

const unsigned long ACTION_DELAY = 250;
const unsigned long DOUBLE_PRESS_TIME = 400;
const unsigned long GESTURE_TIME = 500;

unsigned long lastJoyAction = 0;

// =====================================================
// LCD
// =====================================================

LiquidCrystal_I2C lcd(0x27, 16, 2);

// =====================================================
// BUTTON STATE
// =====================================================

bool lastButtonState[4] = {
  HIGH, HIGH, HIGH, HIGH
};

unsigned long lastButtonPress[4] = {
  0, 0, 0, 0
};

// =====================================================
// LCD DISPLAY
// =====================================================

void showLCD(const char* action) {

  lcd.setCursor(0, 0);
  lcd.print("00:00/00:00    ");

  lcd.setCursor(0, 1);
  lcd.print("                ");

  lcd.setCursor(0, 1);
  lcd.print("> ");
  lcd.print(action);
}

// =====================================================
// SEND COMMAND
// =====================================================

void sendCommand(const char* command) {

  Serial.println(command);
  showLCD(command);
}

// =====================================================
// BUTTON HANDLER
// =====================================================

void checkButton(int index, int pin, const char* command) {

  bool currentState = digitalRead(pin);

  // Button just pressed
  if (lastButtonState[index] == HIGH &&
      currentState == LOW) {

    unsigned long now = millis();

    // Double press
    if (now - lastButtonPress[index] <= DOUBLE_PRESS_TIME) {

      sendCommand("PLAY_PAUSE");

      // Reset so triple-click doesn't trigger another double
      lastButtonPress[index] = 0;
    }

    // Single press
    else {

      sendCommand(command);

      lastButtonPress[index] = now;
    }
  }

  lastButtonState[index] = currentState;
}

// =====================================================
// JOYSTICK
// =====================================================

void checkJoystick() {

  unsigned long now = millis();

  if (now - lastJoyAction < ACTION_DELAY) {
    return;
  }

  int x = analogRead(JOY_X);
  int y = analogRead(JOY_Y);

  int dx = x - CENTER_X;
  int dy = y - CENTER_Y;

  // ---------------------------------------------------
  // JOYSTICK BUTTON
  // ---------------------------------------------------

  if (digitalRead(JOY_SW) == LOW) {

    sendCommand("JOY_SW");

    lastJoyAction = now;

    delay(200);
    return;
  }

  // ---------------------------------------------------
  // CENTER
  // ---------------------------------------------------

  if (abs(dx) < DEADZONE &&
      abs(dy) < DEADZONE) {

    return;
  }

  // ---------------------------------------------------
  // HORIZONTAL MOVEMENT
  // ---------------------------------------------------

  if (abs(dx) > abs(dy)) {

    if (dx < -DEADZONE) {

      sendCommand("TIMELINE_BACK");

      lastJoyAction = now;
      return;
    }

    if (dx > DEADZONE) {

      sendCommand("TIMELINE_FORWARD");

      lastJoyAction = now;
      return;
    }
  }

  // ---------------------------------------------------
  // VERTICAL MOVEMENT
  // ---------------------------------------------------

  else {

    if (dy < -DEADZONE) {

      // Check whether user immediately moves right/left
      delay(80);

      int newX = analogRead(JOY_X);
      int newDx = newX - CENTER_X;

      if (newDx > DEADZONE) {

        sendCommand("REDO");
      }

      else if (newDx < -DEADZONE) {

        sendCommand("UNDO");
      }

      else {

        sendCommand("VOL_UP");
      }

      lastJoyAction = millis();
      return;
    }

    if (dy > DEADZONE) {

      sendCommand("VOL_DOWN");

      lastJoyAction = now;
      return;
    }
  }
}

// =====================================================
// SETUP
// =====================================================

void setup() {

  Serial.begin(115200);

  // Joystick
  pinMode(JOY_SW, INPUT_PULLUP);

  // Buttons
  pinMode(BUTTON_1, INPUT_PULLUP);
  pinMode(BUTTON_2, INPUT_PULLUP);
  pinMode(BUTTON_3, INPUT_PULLUP);
  pinMode(BUTTON_4, INPUT_PULLUP);

  // LCD
  lcd.init();
  lcd.backlight();

  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Editors Deck");

  lcd.setCursor(0, 1);
  lcd.print("Ready!");

  delay(1500);

  lcd.clear();

  Serial.println("EDITORS DECK READY");
}

// =====================================================
// LOOP
// =====================================================

void loop() {

  // Joystick
  checkJoystick();

  // Buttons
  checkButton(0, BUTTON_1, "TRIM");
  checkButton(1, BUTTON_2, "CUT");
  checkButton(2, BUTTON_3, "COPY");
  checkButton(3, BUTTON_4, "DELETE");

}