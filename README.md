### System bring-up:
1. Foolowing the instructions [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#prepare); write image to the SD card, setup, and boot.
2. Following the instructions [here](https://www.youtube.com/watch?v=IbRmYCpF_ws); download and install Visual Studio.
3. [Tutorial](https://www.youtube.com/watch?v=JGMrDXCT_VM) to program GPIO pins to turn on/off an LED.

### Remote connection to Jetson Orin Nano:
1. Install [NoMachine client](https://www.nomachine.com/product&p=NoMachine%20Enterprise%20Client) on your laptop.
2. Install NoMachine on Nano following the instructions [here](https://kb.nomachine.com/AR02R01074) (also written below):
   
   `wget https://www.nomachine.com/free/arm/v8/deb -O nomachine.deb`

   `sudo dpkg -i nomachine.deb`

   `sudo apt install xfce4`  

   `sudo vim /usr/NX/etc/node.cfg`

   A file will open. Find the line starting with `DefaultDesktopCommand` and change the line to the following: `DefaultDesktopCommand "/usr/bin/startxfce4"`
   
   Save the changes and close the file.

   `sudo reboot`

   Once rebooting is done, on the login screen, click on the gear icon and select `xfce4`, then login.

   `xrandr -o left` (to rotate the screen, if you want)


4. Once the installations are completed, on Nano, check IP address:
   
   `ifconfig`
   
   ...
   
   wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
   
        inet **192.168.1.252 ** netmask 255.255.255.0  broadcast 192.168.1.255
   
        inet6 2600:1700:1152:40a0::3b  prefixlen 128  scopeid 0x0<global>
   
        inet6 2600:1700:1152:40a0:7380:231a:5c5:13ce  prefixlen 64  scopeid 0x0<
   
   ...

5. On your laptop, open NoMachine and double click on the machine you are remotely connecting to (all the machines that are connected to the local network and that has NoMachine installed will show up automatically):

   <img width="870" alt="image" src="https://github.com/Ezgii/Jetson-Orin-Nano/assets/4748948/d25ebb8b-9e64-4a04-8060-d60245a903aa">
   
   

7. Login by entering the username and password (of the user of the server you’re connecting to). (To see the username, on Nano terminal, type `whoami`).

   <img width="1419" alt="image" src="https://github.com/Ezgii/Jetson-Orin-Nano/assets/4748948/88c981fa-90fe-4ab3-a654-4c5da878d962">


   
