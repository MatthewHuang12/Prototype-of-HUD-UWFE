from threading import Thread

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scale
import time
window = Tk()

window.geometry("800x480")
window.configure(bg = "#262626")
window.title("UWFE Dashboard (LIGHT)")

bt = "0.00"
mt = "0.00"
it = "0.00"
wt = "0.00"
et = "ERROR"

canvas = Canvas(
    window,
    bg = "#262626",
    height = 480,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


canvas.place(x = 0, y = 0)

charge_bar = canvas.create_rectangle(
    1.0,
    2.0,
    801.0,
    58.00000000000006,
    fill="#FF0000",
    outline="")


soc_label = canvas.create_text(
    270.0,
    91.0,
    anchor="nw",
    text="SOC:",
    fill="#FFFFFF",
    font=("Lato Regular", 30 * -1)
)

soc_text = canvas.create_text(
    345.0,
    53.0,
    anchor="nw",
    text="100%",
    fill="#FFFFFF",
    font=("Lato Bold", 80 * -1)
)

# if you want to change this color gradient, ask chatgpt how to change it to the colors you want, and paste in the function
def calculate_charge_color(charge):
    # Calculate a gradient from yellow to red based on charge percentage
    r = 255
    g = int(255 * (1 - charge / 100))
    b = 0
    # Convert to hexadecimal color code
    color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return color

def update_battery_charge(value):
    # Convert value to an integer
    value = int(value)

    # Update the text
    canvas.itemconfig(soc_text, text=f"{value}%")

    # Calculate the color based on the charge percentage
    charge_color = calculate_charge_color(value)

    # Update the charge bar color
    canvas.itemconfig(charge_bar, fill=charge_color)

    # Update the bar at the top
    canvas.coords(charge_bar, 1.0, 2.0, 1.0 + (value / 100) * 800, 58.0)


battery_charge_slider = Scale(
    window,
    from_=0,
    to=100,
    orient="horizontal",
    length=200,  # Adjust the length as needed
    sliderlength=20,
    showvalue=0,
    command=update_battery_charge
)
battery_charge_slider.place(x=370, y=300)  # Adjust the position as needed

# Initial configuration of the battery charge
update_battery_charge(battery_charge_slider.get())

# top rectangle for battery temp
temp_bg1 = canvas.create_rectangle(
    0.0,
    58.0,
    196.0,
    150.0,
    fill="#FFBE01",
    outline="")

# bottom rectnagle for water temp
temp_bg2 = canvas.create_rectangle(
    0.0,
    323.0,
    196.0,
    415.0,
    fill="#FFE22E",
    outline="")

# third rectangle, inverter temp
temp_bg3 = canvas.create_rectangle(
    0.0,
    234.0,
    196.0,
    326.0,
    fill="#FFD237",
    outline="")

#second rectangle, motor temp
temp_bg4 = canvas.create_rectangle(
    0.0,
    147.0,
    196.0,
    239.0,
    fill="#FFC31F",
    outline="")

battery_temp_label = canvas.create_text(
    4.0,
    62.0,
    anchor="nw",
    text="Battery Temp:",
    fill="#FFFFFF",
    font=("Lato Regular", 15 * -1)
)

motor_temp_label = canvas.create_text(
    4.0,
    150.0,
    anchor="nw",
    text="Motor Temp:",
    fill="#FFFFFF",
    font=("Lato Regular", 15 * -1)
)

inverter_temp_label = canvas.create_text(
    4.0,
    239.0,
    anchor="nw",
    text="Inverter Temp:",
    fill="#FFFFFF",
    font=("Lato Regular", 15 * -1)
)

water_temp_label = canvas.create_text(
    4.0,
    327.0,
    anchor="nw",
    text="Water Temp:",
    fill="#FFFFFF",
    font=("Lato Regular", 15 * -1)
)

battery_temp_text = canvas.create_text(
    6.0,
    76.0,
    anchor="nw",
    text=bt,
    fill="#FFFFFF",
    font=("Lato Bold", 60 * -1)
)

motor_temp_text = canvas.create_text(
    7.0,
    163.0,
    anchor="nw",
    text=mt,
    fill="#FFFFFF",
    font=("Lato Bold", 60 * -1)
)

inverter_temp_text = canvas.create_text(
    4.0,
    253.0,
    anchor="nw",
    text=it,
    fill="#FFFFFF",
    font=("Lato Bold", 60 * -1)
)

water_temp_text = canvas.create_text(
    4.0,
    340.0,
    anchor="nw",
    text=wt,
    fill="#FFFFFF",
    font=("Lato Bold", 60 * -1)
)

deployment_label = canvas.create_text(
    235.0,
    139.0,
    anchor="nw",
    text="Deployment \n Last Lap:",
    fill="#FFFFFF",
    font=("Lato Bold", 20 * -1)
)

deployment_text = canvas.create_text(
    384.0,
    134.0,
    anchor="nw",
    text="4.8%",
    fill="#FFFFFF",
    font=("Lato Regular", 50 * -1)
)

speed_label = canvas.create_text(
    237.0,
    202.0,
    anchor="nw",
    text="Speed:",
    fill="#FFFFFF",
    font=("Lato Bold", 20 * -1)
)

speed_text = canvas.create_text(
    393.0,
    179.0,
    anchor="nw",
    text="34",
    fill="#FFFFFF",
    font=("Lato Regular", 50 * -1)
)

border_rectangle1 = canvas.create_rectangle(
    603.0,
    58.0,
    799.0,
    128.0,
    fill="#6B6B6B",
    outline="#FFFFFF")

border_rectangle2 = canvas.create_rectangle(
    603.0,
    126.0,
    799.0,
    196.0,
    fill="#6B6B6B",
    outline="#FFFFFF")

border_rectangle3 = canvas.create_rectangle(
    603.0,
    193.0,
    799.0,
    263.0,
    fill="#6B6B6B",
    outline="#FFFFFF")

border_rectangle4 = canvas.create_rectangle(
    603.0,
    261.0,
    799.0,
    331.0,
    fill="#6B6B6B",
    outline="#FFFFFF")

vbatt_label = canvas.create_text(
    610.0,
    63.0,
    anchor="nw",
    text="V-Batt:",
    fill="#FFFFFF",
    font=("Lato Regular", 15 * -1)
)


mode_label = canvas.create_text(
    610.0,
    131.0,
    anchor="nw",
    text="Mode:",
    fill="#FFFFFF",
    font=("Lato Regular", 15 * -1)
)

lap_label = canvas.create_text(
    610.0,
    197.0,
    anchor="nw",
    text="Current Lap:",
    fill="#FFFFFF",
    font=("Lato Regular", 15 * -1)
)

lap_label2 = canvas.create_text(
    610.0,
    265.0,
    anchor="nw",
    text="Last Lap",
    fill="#FFFFFF",
    font=("Lato Regular", 15 * -1)
)

vbatt_text = canvas.create_text(
    651.0,
    77.0,
    anchor="nw",
    text="300V",
    fill="#FFFFFF",
    font=("Lato Bold", 40 * -1)
)

error_box_height = 50  # Height of the error box
error_box = canvas.create_rectangle(
    0,  # x1: Start from the left edge
    480 - error_box_height,  # y1: Position y1 just above the bottom edge by the height of the error box
    800,  # x2: Span the entire width of the window
    480,  # y2: Bottom edge of the window
    fill="blue", 
    outline="",
    state="hidden"  # Initially hidden
)

# Position the error text within the error box, aligned to the left
error_text_padding = 10  # Padding from the left edge of the error box
error_text = canvas.create_text(
    error_text_padding,  # x: Start just inside the left edge of the box
    480 - error_box_height / 2,  # y: Vertically center the text in the error box
    anchor="w",  # Anchor the text at the west (left) to align it inside the box
    text="ERROR", 
    fill="white", 
    font=("Lato Bold", 20), 
    state="hidden"  # Initially hidden
)

def show_error_box(show):
    """Show or hide the error box."""
    if show:
        canvas.itemconfig(error_box, state="normal")
        canvas.itemconfig(error_text, state="normal")
    else:
        canvas.itemconfig(error_box, state="hidden")
        canvas.itemconfig(error_text, state="hidden")

def flash_screen():
    """Toggle the canvas background to simulate flashing for ERROR mode."""
    if canvas.itemcget(mode_text, "text") == "ERROR":
        current_color = canvas['bg']
        new_color = "#FF0000" if current_color != "#FF0000" else "#262626"
        canvas.configure(bg=new_color)
        window.after(500, flash_screen)
   

    else:
        # Reset the canvas background if not in ERROR mode
        canvas.configure(bg="#262626")


def changeMode():
    """Cycle through the modes RACE -> SLOW -> ERROR and trigger actions accordingly."""
    current_mode = canvas.itemcget(mode_text, "text")
    if current_mode == "RACE":
        canvas.itemconfig(mode_text, text="SLOW")
        show_error_box(False)  # Hide the error box
    elif current_mode == "SLOW":
        canvas.itemconfig(mode_text, text="ERROR")
        flash_screen()  # Start flashing screen for ERROR mode
        show_error_box(True)  # Show the error box
    elif current_mode == "ERROR":
        canvas.itemconfig(mode_text, text="RACE")
        show_error_box(False)  # Hide the error box
        # No need to call flash_screen() to stop as it checks the mode before flashing




mode_button = Button(
    window,
    text="Mode",
    font=("Lato Regular", 15),
    bg="#4CAF50",
    fg="black",
    command=changeMode
)

# Position the button
mode_button.place(x=370, y=320)
    

mode_text = canvas.create_text(
    620.0,
    144.0,
    anchor="nw",
    text="RACE",
    fill="#FFFFFF",
    font=("Lato Bold", 40 * -1)
)

current_lap_text = canvas.create_text(
    621.0,
    212.0,
    anchor="nw",
    text="00:00:00",
    fill="#FFFFFF",
    font=("Lato Bold", 40 * -1)
)

last_lap_text = canvas.create_text(
    621.0,
    278.0,
    anchor="nw",
    text="00:00:00",
    fill="#FFFFFF",
    font=("Lato Bold", 40 * -1)
)

def dash():
    # loop infinitely while program is running, ask for input every 30 sec
    loop = 0

    while loop == 0:
        # get input for battery temp, motor temp, inverter temp, water temp from cl
        bt = input("Battery Temp: ")
        mt = input("Motor Temp: ")
        it = input("Inverter Temp: ")
        wt = input("Water Temp: ")
        et = input("Error: ")

        # update batery temp, motor temp, inverter temp, water temp

        canvas.itemconfigure(battery_temp_text, text=bt)
        canvas.itemconfigure(motor_temp_text, text=mt)
        canvas.itemconfigure(inverter_temp_text, text=it)
        canvas.itemconfigure(water_temp_text, text=wt)
        canvas.itemconfigure(error_text, text=et)
        
    window.resizable(False, False)
    window.mainloop()
    
dash()
