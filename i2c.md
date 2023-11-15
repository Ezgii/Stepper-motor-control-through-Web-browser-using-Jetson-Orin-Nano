### Hardware setup

Establish the following connections:

LSM303 Vin <--> Jetson Orin Nano J12-1 (3.3V)

LSM303 GND <--> Jetson Orin Nano J12-9 

LSM303 SCL <--> Jetson Orin Nano J12-5 

LSM303 SDA <--> Jetson Orin Nano J12-3 


### Enable I2C

1. Configure I2C:

   ezgi@ezgi-desktop:~$ `sudo usermod -a -G i2c $USER`

2. Check id the I2C tool is installed:

   ezgi@ezgi-desktop:~$ `sudo apt-get install i2c-tools`

3. Install python smbus:

   ezgi@ezgi-desktop:~$ `sudo apt-get install python-smbus`

4. Reboot:

   ezgi@ezgi-desktop:~$ `sudo reboot`

5. Check if any I2C device is detected:

   ezgi@ezgi-desktop:~$ `i2cdetect -y 0`
