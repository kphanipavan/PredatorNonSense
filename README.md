# PredatorNonSense
Clone of Acer's Predator Sense™ application for fan control on Linux

# * Important *
- Only the fan controls work.
- Other tabs are buggy and may crash the system.
- Fan control works fine on my 2021 Predator Helios 300, PH315-53-72W3.
- This code is tested on Kubuntu 20.04 LTS, you might encounter some issues used on others, if so consult StackOverflow.
- It is not garunteed to work on your model.
- DO NOT RUN THIS ON A DEVICE OTHER THAN A HELIOS 300. USE AT YOUR OWN RISK.
- YOU ARE WARNED NOT TO USE THIS IF YOU DON'T KNOW WHAT YOU ARE DOING.
- I AM NOT RESPONSIBLE FOR BRICKING YOUR DEVICE.
- Helios 300 users: It is recommended to verify that the EC location and data values are the same for your model, link given below
- https://docs.google.com/document/d/1t4qgRKOp1AOsxOUDFZo9hASgen8Ea04nu9-PCp-KhYQ/edit

# Pre-requisites

- Requires Python 3.6 or above
- Requires PyQt5. [Instructions](https://www.howtoinstall.me/ubuntu/18-04/python3-pyqt5/)
- Make sure ModProbe is available. `which modprobe`
- Verify that your model number matched "PH315-53-72W3" or serial mathces "NH-QCYSI-008"
- If not, use an EC reader program like [RW Everything](http://rweverything.com/) and verify that your readings are identical to mine, provided in [This Document](https://docs.google.com/document/d/1t4qgRKOp1AOsxOUDFZo9hASgen8Ea04nu9-PCp-KhYQ/edit)
- Sudo Permissions, required for making EC writable using modprobe.

# Usage

- Open a new terminal window.
- Clone this repository `cd ~/Desktop && git clone https://github.com/kphanipavan/PredatorNonSense.git`
- Open the cloned repository `cd PredatorNonSense`
- Run the following: `sudo chmod +x PNS.sh && sudo bash ./PNS.sh`
- Provide your account password and wait till the window opens.
- Dont use the "Keyboard RGB" tab, it is a work in progress, may crash.

# Features

- Full control over both CPU and GPU fans.
- Toggle button for Acer's Cool Boost Technology, which increases fan speed by 250RPM.
- One click switch between Auto mode and Max speed mode.
- Manual mode available with individual sliders.
- The turbo light turns on if any one of the fans are set to turbo.
- Sinple Design.

## Note
- Sliders lag when used, change it one step at a time using arrow keys.
- Thanks to [MSI Fan Control by Artharvalele](https://github.com/atharvalele/MSI_Fan_Control) for providing some part of the code.
- Thanks to [Acer](www.acer.com) for [this](https://www.acer.com/ac/en/IN/content/predator-model/NH.QCYSI.008) marvalous laptop.
- Fan curve cannot be changed.
- Turbo Button and the Predator Sense Key doesn't work.
- Open an issue if you encounter one.
