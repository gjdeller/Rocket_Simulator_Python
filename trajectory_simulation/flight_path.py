#rocket_simulator_python/trajectory_simulation/flight_path.py
import math
from kinematics import Kinematics
from aerodynamics import Aerodynamics

class FlightPath:
    def __init__(self, velocity, position, launch_angle, acceleration, time, dragCoeff, surfaceArea, airDensity):
        self.kinematics = Kinematics(velocity, position, launch_angle, acceleration, time)
        self.aerodynamics = Aerodynamics(dragCoeff, surfaceArea, airDensity)
        self.mass = 1000 #mass of rocket in kg
        self.thrust = 1500 #thrust force in Newtons
        self.dt = 0.1 #time step

    def simulate(self):
        while self.kinematics.position[1] >= 0:
            #update forces
            drag = self.aerodynamics.calculate_drag(self.kinematics.velocity)
            lift = self.aerodynamics.calculate_lift(self.kinematics.velocity, self.kinematics.launch_angle)
            gravity = self.mass * 9.8 #gravitational force

            #Net Force
            net_force = self.thrust - drag - gravity
            acceleration = net_force / self.mass

            self.kinematics.acceleration = acceleration
            self.kinematics.update_position()
            self.kinematics.update_final_velocity()

             # Print results at each time step
            print(f"Time: {self.kinematics.time:.2f} s")
            print(f"Position: {self.kinematics.get_position()} m")
            print(f"Velocity: {self.kinematics.get_final_velocity()} m/s")
            print(f"Drag Force: {drag} N")
            print(f"Lift Force: {lift} N")
            print(f"Acceleration: {acceleration} m/s²")
            print("-----")

            #increment time step
            self.kinematics.time += self.dt

        print("Simulation Complete.")
