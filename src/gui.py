import tkinter as tk
import detection

# Define selectedColor within this file
selectedColor = ''

def open_detection_window(color):
    detection.create_detection_window(color)

# Function to update the label and selectedColor variable when a color button is clicked
def update_label(color):
    global selectedColor
    selectedColor = color  # Update the selectedColor variable
    label.config(text=f"Selected Color: {color}")

# Function to proceed with the selected color without exporting
def proceed_with_color():
    global selectedColor
    if selectedColor:
        label.config(text=f"Bobbin Color set to: {selectedColor}")
        label.config(text="Opening Detection Window")
        open_detection_window(selectedColor)  # Pass the selectedColor to the detection window
    else:
        print("No color selected.")

# Create the main window
root = tk.Tk()
root.title("Color Selection Window")
root.geometry("1066x668")


# Create a label widget
label = tk.Label(root, text="Select a Color", font=("Arial", 14))
label.pack(pady=20)

# Create color buttons
colors = ['Red', 'Green', 'Blue', 'Black', 'White']
for color in colors:
    button = tk.Button(
        root, 
        text=color, 
        command=lambda c=color: update_label(c), 
        width=10, 
        bg=color.lower(),  # Set the button background color
        fg="white" if color in ['Black', 'Blue'] else "black"  # Set text color for better contrast
    )
    button.pack(pady=5)

# Create a "Proceed" button to proceed with the selected color
proceed_button = tk.Button(root, text="Proceed with Color", command=proceed_with_color, font=("Arial", 14))
proceed_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
