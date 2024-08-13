#rocket_simulator_python/trajectory_simulation/trajectory_ui.py

"""
    User Interface: 
    step 1) utilize all kinematics.cpp values to create a UI 
    that shows the path that the rocket will take
    based on user inputs

    step 2) in the User Interface make sure that it has a rocket
    and then a red line that indicates the launch curve over time based
    on the user's launch angle

    step 3) based on the User's launch angle, determine if the rocket will hit
    either earth or orbit insertion etc...
"""

# rocket_simulator_python/trajectory_simulation/trajectory_ui.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from kinematics import Kinematics
from aerodynamics import Aerodynamics
import matplotlib.pyplot as plt

class TrajectoryUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the layout
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Input fields
        self.velocity_input = QLineEdit()
        self.velocity_input.setValidator(QDoubleValidator(0.0, 999.9, 2))
        self.velocity_input.setPlaceholderText("Initial Velocity (m/s)")
        form_layout.addRow("Initial Velocity:", self.velocity_input)

        self.launch_angle_input = QLineEdit()
        self.launch_angle_input.setValidator(QDoubleValidator(0.0, 90.0, 2))
        self.launch_angle_input.setPlaceholderText("Launch Angle (degrees)")
        form_layout.addRow("Launch Angle:", self.launch_angle_input)

        self.drag_coeff_input = QLineEdit()
        self.drag_coeff_input.setValidator(QDoubleValidator(0.0, 10.0, 2))
        self.drag_coeff_input.setPlaceholderText("Drag Coefficient")
        form_layout.addRow("Drag Coefficient:", self.drag_coeff_input)

        self.surface_area_input = QLineEdit()
        self.surface_area_input.setValidator(QDoubleValidator(0.0, 100.0, 2))
        self.surface_area_input.setPlaceholderText("Surface Area (m^2)")
        form_layout.addRow("Surface Area:", self.surface_area_input)

        self.air_density_input = QLineEdit()
        self.air_density_input.setValidator(QDoubleValidator(0.0, 2.0, 3))
        self.air_density_input.setPlaceholderText("Air Density (kg/m^3)")
        form_layout.addRow("Air Density:", self.air_density_input)

        layout.addLayout(form_layout)

        # Run simulation button
        self.run_button = QPushButton("Run Simulation")
        self.run_button.clicked.connect(self.run_simulation)
        layout.addWidget(self.run_button)

        # Set layout to the main window
        self.setLayout(layout)
        self.setWindowTitle('Rocket Trajectory Simulation')
        self.show()

    def run_simulation(self):
        # Get input values
        velocity = float(self.velocity_input.text())
        launch_angle = float(self.launch_angle_input.text())
        drag_coeff = float(self.drag_coeff_input.text())
        surface_area = float(self.surface_area_input.text())
        air_density = float(self.air_density_input.text())

        # Set initial conditions
        position = [0, 0]
        acceleration = 0
        time = 0

        # Initialize Kinematics and Aerodynamics
        kinematics = Kinematics(velocity, position, launch_angle, acceleration, time)
        aerodynamics = Aerodynamics(drag_coeff, surface_area, air_density)

        # Simulation parameters
        mass = 1000  # Mass of the rocket in kg
        thrust = 15000  # Thrust force in N
        dt = 0.1  # Time step in seconds

        # Variables to store trajectory data
        x_positions = []
        y_positions = []

        # Run the simulation
        while kinematics.position[1] >= 0:
            drag = aerodynamics.calculate_drag(kinematics.velocity)
            lift = aerodynamics.calculate_lift(kinematics.velocity, kinematics.launch_angle)
            gravity = mass * 9.8  # Gravity force in N

            net_force = thrust - drag - gravity
            acceleration = net_force / mass

            kinematics.acceleration = acceleration
            kinematics.update_position()
            kinematics.update_final_velocity()

            # Store the positions
            x_positions.append(kinematics.position[0])
            y_positions.append(kinematics.position[1])

            kinematics.time += dt

        # Plot the trajectory
        self.plot_trajectory(x_positions, y_positions)

    def plot_trajectory(self, x_positions, y_positions):
        plt.figure(figsize=(10, 6))
        plt.plot(x_positions, y_positions, label="Trajectory")
        plt.title("Rocket Trajectory")
        plt.xlabel("Horizontal Distance (m)")
        plt.ylabel("Vertical Height (m)")
        plt.grid(True)
        plt.legend()
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TrajectoryUI()
    sys.exit(app.exec())


