### Check PWM driver:

<img width="936" alt="image" src="https://github.com/Ezgii/Jetson-Orin-Nano/assets/4748948/bb4c4c8e-4183-41c9-8a55-ba521d491eb9">

### Configure the 40-pin expansion header [[reference]](https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3231/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/hw_setup_jetson_io.html):

1. Run this command:
`sudo /opt/nvidia/jetson-io/jetson-io.py`

2. A UI will open. Select the below pins by pressing the space button, as shown below.

<img width="1060" alt="image" src="https://github.com/Ezgii/Jetson-Orin-Nano/assets/4748948/04aedbb0-507f-45d6-99dc-df93674d51b5">


Back >> Save pin changes >> Save and reboot to reconfigure pins.

<img width="1076" alt="image" src="https://github.com/Ezgii/Jetson-Orin-Nano/assets/4748948/eabd3dfa-223e-4b80-a53c-0329df2e0393">



### Check PWM output on the scope:

Eg: Set freq = 1000Hz, duty cycle = 25% (pin15 is used)

![image](https://github.com/Ezgii/Jetson-Orin-Nano/assets/4748948/26e19b73-5c4b-4561-9cde-cb33c7368e72)
