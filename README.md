# waste-sorting-robot-raspberrypi4

The entire robot body was made with used cardboard to recycle materials, and it provided me with the ability to change the shape and adopt new implementations as fast as possible within the given timeframe for this project. So it may not look refined; however, all functionalities work.

<img width="1510" height="1172" alt="image" src="https://github.com/user-attachments/assets/5d41ded8-9e57-4a7f-84eb-f9d3c4f6858c" />


## AIM:

• A robotic system placed in houses that can identify trash items and separate them into 3 categories.

• The system will also be able to interact with humans by means of contactless opening and data
visualization and storage.

• The system is capable of working autonomously when it is powered on and has a manual override
controlled by the user

## OBJECTIVES:
• Research – To research past systems that are similar in aims and functionalities. These can be
systems that can sort trash as well or have a machine vision capable of object identification for it then to be used to separate items into categories

• Design – List all possible components needed for the system and identify why and where they would
be needed. Each component must have a reasoning for its addition in the system.
A design for the body of the robot is also created to understand where each component must go for
the system to work. The body should follow the aim of separating trash and must include the
placements of bins and the camera for machine vision. The system’s main computer will be
Raspberry Pi and all components should be compatible with this main computer.


• Components testing + power testing – Test each included component with the main computer for
the types of data input it receives and the output it must send. Since the pinouts of the Raspberry Pi is limited, the number of components should consider the limitations of the pins available on the RPi. Moreover, since RPi’s GPIO are programmed using Python, all components can be controlled via Python as well. Although RPi can power certain small component that work on 3.3V and 5V, the best possible action is to have the components powered by an external power supply and each component should receive their required power supply.

• Build vision AI for object identification – The RPi has good RAM but is not suitable for long Object Identification. There needs to be a machine learning model suitable for IoT projects that can be run on the RPi without burning the computer but work as intended. It is important to have a model capable of running on the RPi with an object identification or detection functions which can then sort objects into the 3 categories.

• Test with datasets – With a working model, test with datasets that are most likely to come up in the trash sorting robot and document test results

• Build architecture – Construct the different parts of the root according to design and power supply

• Functionality testing – Test each functionality of the robot before assembling all together to ensure that there are minimal errors in the future

• Build main body for the robot – Assemble the functionalities all together

• Complete system testing – Run multiple different scenarios on the system and compare the results with expected outcomes and fix errors where required

## System Hierarchy Diagram
<img width="2438" height="1208" alt="image" src="https://github.com/user-attachments/assets/9de2a8ba-5928-4493-989e-2bcd00777a0d" />

## Pinout table
<img width="1914" height="1058" alt="image" src="https://github.com/user-attachments/assets/7a0bf23c-c5b0-4e1e-a9ea-c37b94b5b162" />


## Final Connection Diagram
<img width="1986" height="1318" alt="image" src="https://github.com/user-attachments/assets/27dc51eb-f27e-487f-a384-5ea3c7129768" />


## System Diagram
<img width="1626" height="1024" alt="System_diagram" src="https://github.com/user-attachments/assets/0277f764-74fd-47d3-8e6a-002da28e1577" />


## Proposed Physical Architecture with Arduino
<img width="1596" height="1064" alt="physical_architecture" src="https://github.com/user-attachments/assets/b494ca10-24db-4654-aba5-e2f41c908c7e" />

## Raspberry Pi

The Operating System installed on the Raspberry Pi 4 is the Debian Bullseye 64-bit, which was flashed into an empty SD card using the Raspberry Pi Imager (v1.7.3) to ensure that it has the latest and original version.
The Imager also gives the ability to change the username and password so that the SSH connection remains secure between the laptop and RPi. The wireless LAN is also configured so that RPi is immediately connected to the network from the moment it is powered on. 

Data Labelling – to train and test the detection model, it needs to have labelled data
Datasets were taken from (https://www.kaggle.com/datasets/sapal6/waste-classification-datav2?resource=download) and labelled with Label Studio. This dataset consists of images separated into 3 categories as well which makes it a suitable dataset for this project.
The labels were done according to the 3 categories: Non-recyclable, Recyclable, and Organic.
The RPi 4 4GB RAM has enough computational resources to run object detection and show camera feed, but only for a brief amount of time.

<img width="1124" height="624" alt="image" src="https://github.com/user-attachments/assets/d85bd67b-82fd-4126-bc0a-16d1c79698db" />

## Images 
<img width="1448" height="1134" alt="image" src="https://github.com/user-attachments/assets/01b98061-de87-4cde-85aa-93509671cdfe" />

<img width="1594" height="1234" alt="image" src="https://github.com/user-attachments/assets/d00e2b6d-ee56-48f5-afa4-80f545c973c8" />

<img width="1320" height="1094" alt="image" src="https://github.com/user-attachments/assets/92869561-d605-4466-a8ea-07d52f3d4f76" />

<img width="1152" height="810" alt="image" src="https://github.com/user-attachments/assets/65cf117f-0b2e-4a62-aefd-90be3951e014" />

<img width="1272" height="924" alt="image" src="https://github.com/user-attachments/assets/ec34d63e-a24d-49cc-8afd-77ddd4b7a166" />

<img width="1440" height="888" alt="image" src="https://github.com/user-attachments/assets/0759e30f-5b1f-4371-9f25-5a761259f963" />

<img width="748" height="922" alt="image" src="https://github.com/user-attachments/assets/11595174-17bc-4f86-975e-2a09118704ee" />

<img width="1538" height="1018" alt="image" src="https://github.com/user-attachments/assets/37487010-769e-49e6-b164-cc051b2bbd54" />





