import tkinter as tk
from tkinter import simpledialog
import RPi.GPIO as GPIO

# Setup GPIO
GPIO.setmode(GPIO.BCM)
led_pins = {'red': 17, 'green': 27, 'blue': 22}
for pin in led_pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def turn_on_led(color):
    # Turn all LEDs off
    for pin in led_pins.values():
        GPIO.output(pin, GPIO.LOW)
    # Turn the specified LED on
    if color in led_pins:
        GPIO.output(led_pins[color], GPIO.HIGH)

def exit_app():
    GPIO.cleanup()
    window.destroy()

# GUI Setup
window = tk.Tk()
window.title("LED Control Panel")

# Radio Buttons for LED control
led_choice = tk.StringVar(value="none")  # Default value to none when the app starts
for color in led_pins.keys():
    radio_button = tk.Radiobutton(window, text=color.capitalize(), variable=led_choice, value=color,
                                  command=lambda color=color: turn_on_led(color))  # Capture the color variable correctly in lambda
    radio_button.pack(anchor=tk.W)

# Button to enter LED color manually
def prompt_color():
    input_color = simpledialog.askstring("Input", "Enter color (red, green, blue):", parent=window)
    if input_color and input_color.lower() in led_pins:
        turn_on_led(input_color.lower())
        led_choice.set(input_color.lower())  # Update the radio button selection

tk.Button(window, text='Enter Color Manually', command=prompt_color).pack()

# Exit button
exit_button = tk.Button(window, text="Exit", command=exit_app)
exit_button.pack()

window.mainloop()
