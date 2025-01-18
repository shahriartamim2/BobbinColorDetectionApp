import tkinter as tk
from tkinter import Label
import serial
import time

# Initialize serial communication and variables
detectedColor = ""

PORT = 'COM3'
BAUDRATE = 9600
try:
    ser = serial.Serial(PORT, BAUDRATE)
    time.sleep(5)  # Allow time for the connection to establish
    print("Connected to Arduino.")
except serial.SerialException as e:
    print(f"Error: Could not open port {PORT}. {e}")
    ser = None  # Set ser to None if the port cannot be opened

thres = 200

# Function to update the detected color label and match status
def update_gui(second_window, selected_color, selected_color_label, detected_color_label, match_status_label):
    global detectedColor
    
    if ser is None:
        print("Serial port is not available from ser.")
        detected_color_label.config(text="Error: Serial port not available")
        return

    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        parts = data.split()
        if len(parts) >= 3:  # Ensure the expected format
            R = int(parts[0].split(':')[1])
            G = int(parts[1].split(':')[1])
            B = int(parts[2].split(':')[1])
            redPW = R
            greenPW = G
            bluePW = B
            # Detect color based on PWM thresholds
            if redPW < thres and greenPW < thres and bluePW < thres:
                detectedColor = "White"
            elif redPW > thres and greenPW > thres and bluePW > thres:
                detectedColor = "Black"
            elif redPW < thres and greenPW > thres and bluePW > thres:
                detectedColor = "Red"
            elif greenPW < thres and redPW > thres and bluePW > thres:
                detectedColor = "Green"
            elif bluePW < thres and greenPW > thres and redPW > thres:
                detectedColor = "Blue"
            else:
                detectedColor = "No dominant color detected"
                
            selected_color_label.config(text=f"Selected Bobbin Color: {selected_color}")
            # Update the detected color label
            detected_color_label.config(text=f"Detected Bobbin Color: {detectedColor}")
            
            # Check if the detected color matches the selected bobbin color
            if detectedColor == selected_color:
                match_status_label.config(text="Match Status: Bobbin Color Matched", fg="green")
            else:
                match_status_label.config(text="Match Status: Bobbin Color does not match", fg="red")
    else:
        print("Serial port is not available. ok")    
    # Schedule the function to run again after a short delay
    second_window.after(500, lambda: update_gui(second_window, selected_color, selected_color_label, detected_color_label, match_status_label))

# Function to create and display the detection window, accepting the selected color
def create_detection_window(selected_color):
    # Create a new window for the detection process
    second_window = tk.Toplevel()
    second_window.title("Color Detection")
    second_window.geometry("500x350")

    # Create Labels to display the detected color and match status
    detected_color_label = Label(second_window, text="Detected Color: None", font=("Arial", 14))
    detected_color_label.pack(pady=10)
    
    selected_color_label = Label(second_window, text="Selected Color: None", font=("Arial", 14))
    selected_color_label.pack(pady=10) 
    
    match_status_label = Label(second_window, text="Match Status: Not Checked", font=("Arial", 14))
    match_status_label.pack(pady=10)

    # Start the detection process by calling update_gui
    update_gui(second_window, selected_color, selected_color_label, detected_color_label, match_status_label)
