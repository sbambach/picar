#RTK-000-001 Basis
#Licensed under the GNU GPL V3 License
#(C) Ryanteck LTD. 2014
#Contributors: Ryan Walmsley, Michael Horne
from time import sleep #We will need to sleep the code at points
import RPi.GPIO as GPIO #Import the GPIO library as GPIO

#Setup GPIO
GPIO.setmode(GPIO.BCM) # Set the numbers to Broadcom Mode
GPIO.setwarnings(False) # Ignore any errors

#Assign variables to pins
m1a = 17
m1b = 18
m2a = 22
m2b = 23

#Setup the outputs
GPIO.setup(m1a,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(m1b,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(m2a,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(m2b,GPIO.OUT) #Set 23 as output (Motor 2 B)
print("Ended without any errors")

#Start selftest
GPIO.output(m1a, True)
sleep(1)
GPIO.output(m1a, False)
sleep(1)
GPIO.output(m1b, True)
sleep(1)
GPIO.output(m1b, False)
sleep(1)
GPIO.output(m2a, True)
sleep(1)
GPIO.output(m2a, False)
sleep(1)
GPIO.output(m2b, True)
sleep(1)
GPIO.output(m2b, False)


