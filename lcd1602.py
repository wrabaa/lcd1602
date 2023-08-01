from RPLCD.i2c import CharLCD
import time

# Replace 0x27 with the I2C address of your LCD module
lcd = CharLCD('PCF8574', 0x27)

try:
    # Display "Hello" on the first line of the LCD
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Hello")

    # Display "World!" on the second line of the LCD
    lcd.cursor_pos = (1, 0)
    lcd.write_string("World!")

    # Keep the message displayed until interrupted by the user
    while True:
        pass

except KeyboardInterrupt:
    # Clear the LCD before exiting
    lcd.clear()
    lcd.write_string("Exiting...")
