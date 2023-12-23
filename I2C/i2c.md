### Hardware setup

Establish the following connections:

LSM303 Vin <--> Jetson Orin Nano J12-1 (3.3V)

LSM303 GND <--> Jetson Orin Nano J12-9 

LSM303 SCL <--> Jetson Orin Nano J12-5 

LSM303 SDA <--> Jetson Orin Nano J12-3 

### Install Archiconda and create a new environment

1. Go to https://github.com/Archiconda/build-tools/releases and download Archiconda3-0.2.3-Linux-aarch64.sh on Nano.

2. On Nano terminal, type:

   ezgi@ezgi-desktop:~$ `cd Downloads`

   ezgi@ezgi-desktop:~/Downloads$ `bash Archiconda3-0.2.3-Linux-aarch64.sh`

   ezgi@ezgi-desktop:~/Downloads$ `source ~/.bashrc`

   ezgi@ezgi-desktop:~$ `conda create -n "cmpe244"`

   ezgi@ezgi-desktop:~$ `conda activate cmpe244`

### Install the dependencies

   (cmpe244) ezgi@ezgi-desktop:~$ `conda install pip`

   (cmpe244) ezgi@ezgi-desktop:~$ `/home/ezgi/archiconda3/envs/cmpe244/bin/pip install adafruit-circuitpython-lsm303dlh_mag`

   (cmpe244) ezgi@ezgi-desktop:~$ `/home/ezgi/archiconda3/envs/cmpe244/bin/pip install Jetson.GPIO`
   

### Enable I2C

1. Check if any I2C device is detected:

   (cmpe244) ezgi@ezgi-desktop:~$ `i2cdetect -y -r 7`

   (Bus 7 is selected because we are connected to I2C Bus 7.)

   ![image](https://github.com/Ezgii/Jetson-Orin-Nano/assets/4748948/a9e8c814-1696-47b2-bfe4-d28e02c67885)

   The detected I2C devices:
   
   <img width="1025" alt="image" src="https://github.com/Ezgii/CMPE244-Project/assets/4748948/51115971-33d4-4563-8b44-3b0edc85decb">


   As per the LSM303 datasheet,

   For linear acceleration the default (factory) 7-bit slave address is 0011001b = 0x19.

   For magnetic sensors the default (factory) 7-bit slave address is 0011110xb = 0x1E.


### Run simple code

1. Open Visual Studio.

2. Ctrl+Shift+P (Command palette) -> Python: Select Interpreter

   Select cmpe244 as the interpreter, and run the test code shown [here](https://github.com/Ezgii/CMPE244-Project/blob/main/ezgi_i2c_test.py).

