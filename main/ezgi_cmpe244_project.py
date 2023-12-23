# from RPi import GPIO
import numpy as np
import sys
import time
import board
import Jetson.GPIO as GPIO
import busio
# import digitalio
import adafruit_lsm303dlh_mag
import adafruit_lsm303_accel
import math

GPIO.setwarnings(False)
GPIO.cleanup()

# print("Content-type:text/html\r\n\r\n")

############## Get user input

if len(sys.argv) > 1:
    angle = int(sys.argv[1])
    direction = sys.argv[2]
else:
    angle = 15
    direction = "clockwise"

if direction == "clockwise":
    dir = True
else:
    dir = False


############## Setup PWM

freq = 10
duty_cycle = 2

pwm_pin = 15 
dir_pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwm_pin,GPIO.OUT)
GPIO.setup(dir_pin,GPIO.OUT)
p = GPIO.PWM(pwm_pin, freq)


############## Setup I2C

# i2c = board.I2C() 
i2c = busio.I2C(board.SCL, board.SDA)
mag_sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
#acc_sensor = adafruit_lsm303_accel.LSM303_Accel(i2c)

##############

def compute_angle():
    
    mag_x, mag_y, mag_z = mag_sensor.magnetic
    # acc_x, acc_y, acc_z = acc_sensor.acceleration

    print('Magnetometer (gauss): ({0:10.3f}, {1:10.3f}, {2:10.3f})'.format(mag_x, mag_y, mag_z))
    # print('<p>Acceleration (m/s^2): ({0:10.3f}, {1:10.3f}, {2:10.3f})</p>'.format(acc_x, acc_y, acc_z))        

    x_offset = 50
    y_offset = -41
    z_offset = -9

    angle = np.arctan2(mag_y - y_offset, mag_z - z_offset)

    if angle > 0:
        angle  = angle * (180 / math.pi)
    else:
        angle = (angle + 2 * math.pi) * (180 / math.pi);

    print(f"Angle [degree]: {angle}")

 
    return angle   


print(f"Spinning {angle} degrees in {direction} direction...")

print("")
print("*** Before ***")

angle_1 = compute_angle()


GPIO.output(dir_pin,dir)

p.start(duty_cycle)
time.sleep(int(angle/1.8)/freq)
p.stop()

# for i in range(int(360/1.8)):
#     GPIO.output(pwm_pin,True)
#     time.sleep(0.1)
#     GPIO.output(pwm_pin,False)
#     time.sleep(0.1)


print("")
print("*** After ***")

angle_2 = compute_angle()

print("")
print(f"=> Angular displacement [degree]: {angle_2-angle_1}")
print("")


time.sleep(1)


GPIO.cleanup([pwm_pin, dir_pin])



