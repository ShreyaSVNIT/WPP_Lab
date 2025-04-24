import numpy as np

def ctop(cartesian_points):
    #x is all the x points
    #y is all the y points
    x, y = cartesian_points[:, 0], cartesian_points[:, 1]

    #distance from origin
    r = np.sqrt(x**2 + y**2)
    #gives angles in radians
    theta = np.arctan2(y, x)
    return np.stack((r, theta)) #returns the 2d array of [r, theta]

N = int(input())
#this generates n random points with x and y coordinates
cartesian_points = np.random.uniform(-10, 10, (N, 2))
polar_points = ctop(cartesian_points)

print("Cartesian Points:")
print(cartesian_points)
print("\nPolar Coordinates (r, theta in radians):")
print(polar_points)