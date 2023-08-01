from RPLCD.i2c import CharLCD
import time

# Replace 0x27 with the I2C address of your LCD module
lcd = CharLCD('PCF8574', 0x27)

try:
    # Display "Hello, World!" on the LCD
    lcd.write_string("Hello, World!")

    # Wait for 5 seconds
    time.sleep(5)

    # Clear the LCD
    lcd.clear()

except KeyboardInterrupt:
    # Clear the LCD before exiting
    lcd.clear()
    lcd.write_string("Exiting...")
