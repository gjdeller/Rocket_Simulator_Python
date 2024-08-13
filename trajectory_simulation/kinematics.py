#rocket_simulator_python/trajectory_simulation/kinematics.py
import math

"""
step 1)
    calculate the position
    calculate the velocity
    calculate the acceleration/gravity
    calculate the launch angle
    calculate the launch site position
    time keeper
step 2)
    flight path must utilize all of these vales to determine the flight path
"""



class Kinematics:
    def __init__(self, velocity, position, launch_angle, acceleration, time):
        self.velocity = velocity
        self.position = position #[x,y]
        self.launch_angle = launch_angle
        self.acceleration = acceleration
        self.time = time
        self.final_velocity = 0
        self.max_position = 0
    
    #setter functions
    def set_initial_position(self):
        if(self.time==0):
            self.position[0] = 0
            self.position[1] = 0

    def set_initial_velocity(self):
        self.velocity = 400 #m/s

    def set_launch_angle(self, launch_angle):
        self.launch_angle = launch_angle #degrees

    def set_acceleration(self):
        self.acceleration = -9.8 #m/s^2 (acceleration due to force of gravity)

    def update_position(self):
        if(self.launch_angle == 90):
            self.position[0] = 0
            self.position[1] = 0
        elif(self.launch_angle < 90):
            self.position[0] = (self.velocity * math.cos(math.radians(self.launch_angle))) * self.time
            self.position[1] = ((self.velocity * math.sin(math.radians(self.launch_angle)) * self.time) +
                                0.5 * self.acceleration * self.time**2)
    def update_final_velocity(self):
        if(self.launch_angle == 90):
            x_velo_init = 0
            y_velo_init = self.velocity * math.sin(math.radians(self.launch_angle))
        elif(self.launch_angle < 90):
            x_velo_init = self.velocity * math.cos(math.radians(self.launch_angle))
            y_velo_init = self.velocity * math.sin(math.radians(self.launch_angle))
        
        self.final_velocity = math.sqrt(x_velo_init**2 + y_velo_init**2)
    
    def update_time(self):
        vertical_velocity = self.velocity * math.sin(math.radians(self.launch_angle))
        while vertical_velocity > 0:
            self.time += 1
            vertical_velocity += self.acceleration * 1  # Update vertical velocity each second
            self.update_position()  # Update the position as time increments
        print("Time to reach max height:", self.time, "seconds")


    def update_max_position(self):
        if(self.launch_angle == 90):
            self.max_position = self.position[1] + self.velocity * math.sin(math.radians(self.launch_angle))* self.time + 0.5 * self.acceleration * self.time**2
        elif self.launch_angle < 90:
            # Calculate vertical and horizontal velocities
            vertical_velocity = self.velocity * math.sin(math.radians(self.launch_angle))
            horizontal_velocity = self.velocity * math.cos(math.radians(self.launch_angle))
            
            # Time to reach max height (when vertical_velocity = 0)
            time_to_max_height = -vertical_velocity / self.acceleration
            
            # Max height (y component)
            max_height = self.position[1] + vertical_velocity * time_to_max_height + \
                        0.5 * self.acceleration * time_to_max_height**2
            
            # Distance traveled in the horizontal direction (x component)
            horizontal_distance = horizontal_velocity * time_to_max_height
            
            # Update max position
            self.max_position = (horizontal_distance, max_height)
    
    #initial getters
    def get_position(self):
        return self.position
    
    def get_initial_velocity(self):
        return self.velocity
    
    def get_acceleration(self):
        return self.acceleration
    
    def get_launch_angle(self):
        return self.launch_angle
    
    def get_time(self):
        return self.time
    
    def get_final_velocity(self):
        return self.final_velocity
    
    def get_max_position(self):
        if(self.launch_angle == 90 and self.final_velocity == 0):
            return self.position[1] + self.velocity * math.sin(math.radians(self.launch_angle)) * self.time + 0.5 * self.acceleration * self.time**2
        
        return self.max_position

"""
 # Test main
if __name__ == "__main__":
    # Initial parameters: velocity, position [x, y], launch angle, acceleration, time
    kinematics = Kinematics(0, [0, 0], 76, 0, 0)
    
    # Set initial conditions
    kinematics.set_initial_position()
    kinematics.set_initial_velocity()
    #kinematics.set_launch_angle()
    kinematics.set_acceleration()

    # Print initial conditions
    print("Initial Position:", kinematics.get_position())
    print("Initial Velocity:", kinematics.get_initial_velocity(), "m/s")
    print("Launch Angle:", kinematics.get_launch_angle(), "degrees")
    print("Acceleration:", kinematics.get_acceleration(), "m/s^2")
    
    # Update time and compute final values
    kinematics.update_time()
    kinematics.update_position()
    kinematics.update_final_velocity()
    kinematics.update_max_position()

    # Print updated values
    print("Position after time", kinematics.get_time(), "s:", kinematics.get_position())
    print("Final Velocity:", kinematics.get_final_velocity(), "m/s")
    print("Max Position:", kinematics.get_max_position(), "m")       
"""
