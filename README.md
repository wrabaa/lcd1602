Step-by-Step Guide: Setting up 16x2 LCD Screen on Raspberry Pi with "Hello, World!" Display

Step 1: Assemble the 16x2 LCD Screen

Assemble the 16x2 LCD module with the I2C interface.
Connect the LCD module to the Raspberry Pi using the I2C interface as follows:

 LCD VCC to Raspberry Pi 5V (Pin 2).
        
LCD GND to Raspberry Pi GND (Pin 6 or Pin 9).
        
LCD SDA to Raspberry Pi SDA (Pin 3).
        
LCD SCL to Raspberry Pi SCL (Pin 5).

Step 2: Detect the LCD Module and Get Its I2C Address

Power on your Raspberry Pi and open the terminal.
Ensure the I2C tools are installed by running:

    sudo apt update
    sudo apt install i2c-tools

 Scan for I2C devices connected to the Raspberry Pi by running:

    sudo i2cdetect -y 1

Look for the LCD module's I2C address (usually 0x27 or 0x3F) in the output. Make sure it is correctly detected.

Step 3: Enable Necessary Interfaces

To configure the Raspberry Pi settings, run the following command:

    sudo raspi-config
    
Use the arrow keys to navigate and select "Interfacing Options."
Select "I2C" and choose "Yes" to enable the I2C interface.
Select "SPI" and choose "Yes" to enable the SPI interface (required for some LCD modules).
Select "GPIO" and choose "Yes" to enable the GPIO interface.
If prompted to reboot, select "Yes" to apply the changes and reboot your Raspberry Pi.

Step 4: Install the Necessary LCD Library

Open the terminal on your Raspberry Pi.
Run the following command to install the RPLCD library:

    sudo pip3 install RPLCD

Step 5: Clone the GitHub Repository

On your Raspberry Pi, open the terminal.
Clone the GitHub repository containing the "Hello, World!" Python script for the 16x2 LCD:

    git clone https://github.com/w.rabaa/lcd1602.git

Step 6: Navigate to the Project Directory
Change to the lcd1602 directory where the Python script is located:

    cd lcd1602

List the files in the directory:

    ls

You will find the lcd1602.py file in the list.

Step 7: Run the "Hello, World!" Code

Run the "Hello, World!" code using the following command:

    python3 lcd1602.py

The "Hello, World!" message should now be continuously displayed on the LCD screen.

Step 8: Exit the Program

To exit the program, press Ctrl + C in the terminal.

Congratulations! You have now successfully set up the 16x2 LCD screen on your Raspberry Pi, verified its functionality, and displayed a continuous "Hello, World!" message on it
