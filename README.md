### System bring-up:
1. Following the instructions [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#prepare); write image to the SD card, setup, and boot.
2. Following the instructions [here](https://www.youtube.com/watch?v=IbRmYCpF_ws); download and install Visual Studio.
3. [Tutorial](https://www.youtube.com/watch?v=JGMrDXCT_VM) to program GPIO pins to turn on/off an LED.

### Remote connection to Jetson Orin Nano through Wifi:
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

### "Make menuconfig" on Nano [[reference]](https://www.youtube.com/watch?v=ttSy14bQKCE)

Do the following on Nano:
1. Go to [Nvidia Developer website](https://developer.nvidia.com/embedded/jetson-linux) and download "Driver Package (BSP) Sources".
   A zip file named public_sources.tbz2 will be downloaded. Move it into a folder : Desktop/nano_sources.
   
2. On terminal, type:
   
> `cd Desktop/nano_sources`

> `tar -xvf public_sources.tbz2` to unpack it. We only need **kernel_src.tbz2**. Therefore, we remove the rest:

> `mv Linux_for_Tegra/source/public/kernel_src.tbz2 .`

> `rm -Rf Linux_for_Tegra`

> `tar -xvf kernel_src.tbz2` to unpack the kernel sources.

> ` cd kernel/kernel-5.10` to go to the root folder.

> `zcat /proc/config.gz > .config` to copy the existing configuration.

> `sudo apt-get install libncurses5-dev`

> `sudo apt-get install pkg-config`

3. Now we are ready to use the UI!

> `make menuconfig`

The UI will open. Select Device Drivers >> Character devices. It looks like as shown below:

![figure1](https://github.com/Ezgii/Jetson-Orin-Nano/blob/main/UI.jpeg)

Exit the UI, and on the terminal, type:

> `cd drivers/char`

> `vi Kconfig`

Modify the Kconfig file. Save the changes and exit the file. Open the UI again by typing:

> `cd Desktop/nano_sources/kernel/kernel-5.10`

> `make menuconfig`

Select Device Drivers >> Character Devices. It shows my modification now, as shown below:

![figure2](https://github.com/Ezgii/Jetson-Orin-Nano/blob/main/UI_modified.jpeg)



   
