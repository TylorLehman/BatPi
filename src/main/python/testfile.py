# Tylor Lehman
# BatPi
# testfile.py

from Echolocate import getSample
from time import sleep


def testfile
   step_size = 10 # change pulse width by 10*10us = 100us or 0.1ms in each step
   dont_buffer = 0 # don't buffer writes to avoid flushes
   samparray = [0 for i in range(float(100)/step_size)] #float bc remainder
   li = 0 # Loop counter
   with open('/dev/servoblaster', "w", dont_buffer ) as servo_blaster_device:
      for pulse_width in range(100,200,step_size):
         cmd = "0=" + str(pulse_width) + "\n"
         print cmd
         servo_blaster_device.write(cmd)
         samparray[li] = getSample()
         sleep(.25) # This might be way too big of a sleep
   print (li)
