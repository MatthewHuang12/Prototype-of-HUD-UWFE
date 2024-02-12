Overview//

Welcome to the UWFE Dashboard repository! This project is a graphical interface built using Python and the Tkinter library, designed to monitor and display various parameters of our racecars performance in real-time. It aims to provide a comprehensive and user-friendly platform for visualizing key metrics such as battery charge, temperature readings, speed, and error notifications.

Features//

Real-Time Monitoring: Dynamically displays vehicle metrics, including battery charge state, temperatures (battery, motor, inverter, water), speed, and voltage.
Interactive Control Elements: Features interactive sliders and buttons for simulating changes in vehicle conditions and modes.
Error Visualization: Implements an error notification system that visually alerts users to potential issues through color changes and flashing.
Customizable UI: Offers a customizable user interface designed for clarity and ease of use, adaptable to different monitoring needs.
Mode Simulation: Allows users to switch between different operational modes (e.g., RACE, SLOW, ERROR) to simulate vehicle status under various conditions.

Components//

Dashboard Interface: The core graphical user interface that displays all the vehicle metrics and controls.
Temperature Displays: Dedicated sections for displaying the current temperatures of the battery, motor, inverter, and water.
Battery Charge Indicator: A dynamic bar and percentage indicator showing the current state of charge, with color gradients representing charge levels.
Mode Selector: A button that toggles between different vehicle operational modes, affecting the dashboard's display and behavior.
Error Handling: Visual cues and flashing screen features to indicate and handle errors or warnings.

Technologies Used//

Python: Chosen for its readability, simplicity, and the vast array of libraries available for developing graphical interfaces.
Tkinter: Utilized as the standard GUI toolkit for Python, providing the framework for building the dashboard interface.
Canvas Widget: Employed for drawing graphics and other complex interface elements, enabling the creation of custom components like charge bars and temperature indicators.
