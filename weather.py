#import libraries
from Adafruit_BMP085 import BMP085
import RPi.GPIO as GPIO
import time
import sys
# DHT sensor
import Adafruit_DHT
 
# LCD
import Adafruit_CharLCD as LCD
 
# Define sensor
sensor = Adafruit_DHT.DHT22
pin = 4

# Initialize BMP180 and use STANDARD mode (default value)
bmp = BMP085(0x77)
 
# Raspberry PI connections
#lcd_rs		= 26	# Older versions if not working change to 21
#lcd_en		= 19
#lcd_d4		= 13
#lcd_d5		= 6
#lcd_d6		= 5
#lcd_d7		= 11
#lcd_backlight	= 4
 
# Define some device constants
lcd_columns	= 16
lcd_rows	= 2
 
# Initialize the LCD
lcd = LCD.Adafruit_CharLCD()
 
while True:
	try:
		# Get values
                btemp1 = bmp.readTemperature()
                btemp = (btemp1 * 1.8) + 32
                balt = bmp.readAltitude(101500)
                bpress1 = bmp.readPressure()
                bpress = (bpress1 * .02952998751) / 100

		humidity, temperature1 = Adafruit_DHT.read_retry(sensor,pin)
                temperature = (temperature1 * 1.8) + 32
		temp = "{:0.1f}".format(temperature)
		hum = "{:0.1f}%".format(humidity)
                bt = "{:0.1f}".format(btemp)
                ba = "{:0.1f}".format(balt)
                bp = "{:0.2f}inHg".format(bpress)
		# clear lcd
		lcd.clear()
 
		# display temperature
		lcd.message ("Temperature:\n")
	
		# Mostrar a temperatura quase no final
		toMove = lcd_columns - len(temp)
		#lcd.set_cursor(toMove,1)
		lcd.message(temp + ' BMP - ')
                lcd.message(bt)
		time.sleep(5) # 5 second delay
		lcd.clear()

                # display pressure
                toMove = lcd_columns - len(temp)
                lcd.message(bp)
                time.sleep(5)  
                lcd.clear()

                # display altitude
                toMove = lcd_columns - len(temp)
                lcd.message(ba)
                time.sleep(5)
                lcd.clear() 

		# display humidity
		lcd.message ("Humidity:\n")
		toMove = lcd_columns - len(hum)
		#lcd.set_cursor(toMove,1)
		lcd.message (hum)
		time.sleep(5)
 
	except KeyboardInterrupt:
		lcd.clear()
		lcd.message("Adeus!")
		time.sleep(3)
		sys.exit()
