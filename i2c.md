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
