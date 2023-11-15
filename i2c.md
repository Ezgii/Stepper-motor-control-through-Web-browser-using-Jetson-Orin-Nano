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

   ezgi@ezgi-desktop:~$ `i2cdetect -y -r 7`

   (Bus 7 is selected because we are connected to I2C Bus 7.)


   ![image](https://github.com/Ezgii/Jetson-Orin-Nano/assets/4748948/a9e8c814-1696-47b2-bfe4-d28e02c67885)

   The detected I2C devices:
   
   <img width="838" alt="image" src="https://github.com/Ezgii/Jetson-Orin-Nano/assets/4748948/9e844e52-adaf-4ae3-a755-970d7ca76f77">

   As per the LSM303 datasheet,

   For linear acceleration the default (factory) 7-bit slave address is 0011001b = 0x19.

   For magnetic sensors the default (factory) 7-bit slave address is 0011110xb = 0x1E.



