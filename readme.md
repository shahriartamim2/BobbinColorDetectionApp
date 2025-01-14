# Arduino Bobbin Color Detection System 

## Features
- Detects colors of ring yarn bobbins using the TCS230 color sensor.
- Simple and user-friendly interface built with Python to interact with the Arduino.

## Hardware Requirements
- Arduino board (e.g., Arduino Uno)
- TCS230 color sensor module
- Breadboard and jumper wires
- A laptop 😁

## Software Requirements
- Arduino IDE

## Setup Instructions
### 1. Arduino Setup
| **TCS230 Pin** | **Arduino Pin** |
|:--------------:|:---------------:|
| VCC            | 5V              |
| GND            | GND             |
| S0             | Digital Pin 4   |
| S1             | Digital Pin 5   |
| S2             | Digital Pin 6   |
| S3             | Digital Pin 7   |
| OUT            | Digital Pin 8   |

- Upload the `ColorDetection.ino` code to the Arduino using the Arduino IDE.

### 2. Run the Application
- Download the bobbinCD.exe application 
- Run the app by double clicking 

### 3. Test the system
- Select a color for bobbin
- Place a bobbin under the color sensor 


## You can see my project source code in ./src directory and suggest improvements 