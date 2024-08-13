#rocket_simulator_python/trajectory_simulation/aerodynamics.py
import math
"""
    Aerodynamics:

    Attributes: Drag Coefficient, surface area, lift coefficient

    Inputs: velocity from kinematics, orientation data from Rocket, air density from Environment

    Outputs: Aerodynamics forces (drag, lift)
"""
class Aerodynamics():
    def __init__(self, dragCoeff, surfaceArea, airDensity):
        #initialize variables
        self.dragCoeff = dragCoeff 
        self.surfaceArea = surfaceArea
        self.airDensity = airDensity
        self.drag = 0
        self.lift = 0
    
    def calculate_drag(self, velocity):
        self.drag = 0.5 * self.airDensity * self.surfaceArea * self.dragCoeff * velocity**2
        return self.drag
    
    def calculate_lift(self, velocity, launch_angle):
        lift_coeff = 1.0
        self.lift = lift_coeff * self.airDensity * self.surfaceArea * velocity**2 * math.sin(math.radians(launch_angle))
        return self.lift
    #setters
    def set_drag_coeff(self, dragCoeff):
        self.dragCoeff = dragCoeff

    def set_surface_area(self, surfaceArea):
        self.surfaceArea = surfaceArea
    
    def set_air_density(self, airDensity):
        self.airDensity = airDensity
    
    #getters
    def get_drag_coeff(self):
        return self.dragCoeff
    
    def get_surface_area(self):
        return self.surfaceArea
    
    def get_air_density(self):
        return self.airDensity
    
#Test Main
if __name__ == "__main__":
    #instance of aerodyanmcis classs
    aero = Aerodynamics(0.5, 10.0, 1.225)

    velocity = 400 #m\s
    launch_angle = 90 #90 degrees

    #calculate and print drag and lift
    drag = aero.calculate_drag(velocity)
    lift = aero.calculate_lift(velocity, launch_angle)

    print("Drag Force: ", drag, "N")
    print("Lift Force: ", lift, "N")

    #print current attributes
    print("Drag Coefficient: ", aero.get_drag_coeff())
    print("Surface Area: ", aero.get_surface_area(), "m^2")
    print("Air Density: ", aero.get_air_density(), "kg/m^3")



        