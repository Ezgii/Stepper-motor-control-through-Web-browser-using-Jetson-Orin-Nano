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
import matplotlib.pyplot as plt

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

freq = 100
duty_cycle = 2

pwm_pin = 15 
dir_pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwm_pin,GPIO.OUT)
GPIO.setup(dir_pin,GPIO.OUT)
# p = GPIO.PWM(pwm_pin, freq)


############## Setup I2C

i2c = board.I2C() 
# i2c = busio.I2C(board.SCL, board.SDA)
mag_sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
#acc_sensor = adafruit_lsm303_accel.LSM303_Accel(i2c)

##############

GPIO.output(dir_pin,True)

readings = []
for i in range(int(360/1.8)):
    GPIO.output(pwm_pin,True)
    time.sleep(0.01)
    GPIO.output(pwm_pin,False)
    time.sleep(0.01)

    mag_x, mag_y, mag_z = mag_sensor.magnetic
    readings.append([mag_x, mag_y, mag_z])


x_coords = [point[0] for point in readings]
y_coords = [point[1] for point in readings]
z_coords = [point[2] for point in readings]


fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

ax.scatter(x_coords, y_coords, z_coords)
plt.show()

print(f"min x = {min(x_coords):.3f}, max x = {max(x_coords):.3f}, x offset = {((min(x_coords)+max(x_coords))/2):.3f}")
print(f"min y = {min(y_coords):.3f}, max y = {max(y_coords):.3f}, y offset = {((min(y_coords)+max(y_coords))/2):.3f}")
print(f"min z = {min(z_coords):.3f}, max z = {max(z_coords):.3f}, z offset = {((min(z_coords)+max(z_coords))/2):.3f}")
# delta_x = []
# delta_y = []
# delta_z = []
# for i in range(int(360/1.8)-1):
#     delta_x.append(x_coords[i+1] - x_coords[i])
#     delta_y.append(y_coords[i+1] - y_coords[i])
#     delta_z.append(z_coords[i+1] - z_coords[i])

plt.plot(range(200), x_coords, 'r', label="x")
plt.plot(range(200), y_coords, 'g', label="y")
plt.plot(range(200), z_coords, 'b', label="z")
plt.legend()
plt.show()


# plt.plot(range(199), delta_x, 'r', label="delta x")
# plt.plot(range(199), delta_y, 'g', label="delta y")
# plt.plot(range(199), delta_z, 'b', label="delta z")
# plt.legend()
# plt.show()

time.sleep(1)


GPIO.cleanup([pwm_pin, dir_pin])



