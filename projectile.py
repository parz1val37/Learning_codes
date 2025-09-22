import matplotlib.pyplot as plt
import numpy as np
from math import sin, radians, cos, tan
import time

print("\t\t\tProjectile Motion Calculator\n")
speed = float(input("Enter the speed(m/s): "))
angle = radians(float(input("Enter the angle of projection in degrees: ")))

g = 9.8
time_period = (2*speed*sin(angle))/g
max_height = ((speed*sin(angle))**2)/(2*g)
horizontal_range = (speed**2*sin(2*angle))/g

def projectile_motion(speed, angle):
    print(f"\nTotal time of flight is: {round(time_period, 2)}sec")
    print(f"Maximum height reached is: {round(max_height, 2)}m")
    print(f"Horizontal range is: {round(horizontal_range, 2)}m")
    print(f"\nEquation of trajectory is:\ny = {"-" if tan(angle)<0 else ""}x*{abs(round(tan(angle),2))} - 9.8*x²/{round(2*(speed*cos(angle))**2,2)}")
    print("\n\t\t\tPlotting the trajectory...")

projectile_motion(speed, angle)

x = np.linspace(0, horizontal_range, 500)
y = x*tan(angle) - (9.8*x**2)/(2*(speed*cos(angle))**2)

# Plotting trajectory
plt.plot(x, y,'--r', label="PROJECTILE TRAJECTORY")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("PROJECTILE MOTION")
plt.grid(True)
plt.legend()
time.sleep(2)
plt.show()