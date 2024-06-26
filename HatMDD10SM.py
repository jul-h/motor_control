import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay
GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)			# enable warning from GPIO
AN1 = 12				# set pwm1 pin on MD10-hat
DIG1 = 26				# set dir1 pin on MD10-Hat
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
sleep(1)				# delay for 1 seconds
p1 = GPIO.PWM(AN1, 100)			# set pwm for M1

try:					
  while True:

   print "Forward"
   GPIO.output(DIG1, GPIO.LOW)          # set DIG1 as LOW, to control direction
   p1.start(100)                        # set speed for M1 at 100%
   sleep(2)                             #delay for 2 second

   print "Backward"
   GPIO.output(DIG1, GPIO.HIGH)         # set DIG1 as HIGH, to control direction
   p1.start(100)                        # set speed for M1 at 100%
   sleep(2)                             #delay for 2 second
                      
   print "STOP"
   GPIO.output(DIG1, GPIO.LOW)          # Direction can ignore
   p1.start(0)                          # set speed for M1 at 0%
   sleep(3)                             #delay for 3 second


except:					# exit programe when keyboard interupt
   p1.start(0)				# set speed to 0
					# Control+x to save file and exit
