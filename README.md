### System bring-up:
1. Following the instructions [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#prepare); write image to the SD card, setup, and boot.
2. Following the instructions [here](https://www.youtube.com/watch?v=IbRmYCpF_ws); download and install Visual Studio.
3. [Tutorial](https://www.youtube.com/watch?v=JGMrDXCT_VM) to program GPIO pins to turn on/off an LED.

### Remote connection to Jetson Orin Nano:
1. Install [NoMachine client](https://www.nomachine.com/product&p=NoMachine%20Enterprise%20Client) on your laptop.
2. Install NoMachine on Nano following the instructions [here](https://kb.nomachine.com/AR02R01074) (also written below):
   
   Download the DEB package for ARMv8: `wget https://www.nomachine.com/free/arm/v8/deb -O nomachine.deb`

   Then install NoMachine with the 'dpkg' command: `sudo dpkg -i nomachine.deb`

   Install Xfce4 desktop environment: `sudo apt install xfce4`  

   Configure NoMachine for the Xfce desktop: `sudo vim /usr/NX/etc/node.cfg`

      > A file will open. Find the line starting with `DefaultDesktopCommand` and change the line to the following: `DefaultDesktopCommand "/usr/bin/startxfce4"`
      
      > Save the changes and close the file.

   Reboot the system: `sudo reboot`

   Once rebooting is done, on the login screen, click on the gear icon and select `xfce4`, then login.

   `xrandr -o left` (to rotate the screen, if you want)


4. Once the installations are completed, on Nano terminal, type `ifconfig`, and check IP address under wlan0: inet **192.168.1.252**

5. On your laptop, open NoMachine and double click on the machine you are remotely connecting to (all the machines that are connected to the local network and that has NoMachine installed will show up automatically).
   

6. Login by entering the username and password (of the user of the server you’re connecting to). (To see the username, on Nano terminal, type `whoami`).


### Remote connection through ethernet:

1. On Nano (local) disconnect from wifi.
2. Connect an ethernet cable between your laptop and Nano.
3. On your laptop (MAC), go to "System Settings" and seach for "Sharing". 
   Click on the "?" icon next to "Internet Sharing". Select the following:
   
   > Share your connection from: Wifi
   
   > To computers using: \*Check all the boxes\*

   Finally, enable internet sharing by toggling the switch. At this point, the internet connection must be established between your MAC and Nano.

4. On Nano terminal, type `ifconfig`, and check IP address under eth0: inet  **192.168.3.2**. When you open NoMachine on your laptop, you will see your Nano device automatically. Double click and connect.

### To allow graphics without HDMI display:

IMPORTANT - For headless system users
If you don't want to connect a monitor to your device and don't need to have xserver running, perform the following steps. You can skip Step 1 if you already installed Xfce.

Step 1 -  Install Xfce4 desktop environment:
`sudo apt install xfce4`

Step 2 - Disable the xserver using:
`sudo systemctl set-default multi-user.target`

(if Xserver was disabled after NoMachine installation, you will need to restart nxserver: `sudo /usr/NX/bin/nxserver --restart`).

If later you want to connect an HDMI monitor, on Nano terminal, type: `sudo systemctl set-default graphical.target` and then `sudo reboot`.

   
