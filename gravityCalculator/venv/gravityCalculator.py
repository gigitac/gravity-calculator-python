import time

def findGravity(bodyDistance, bodyMass):
    gravity = (0.00000000000667 * bodyMass)/(bodyDistance * bodyDistance)
    print("The gravitational acceleration is " + gravity + "  m/s^2")

print("Here's a simple gravity calculator.")
massOfBody = input("So, what's the mass of the gravitating body?")
distanceFromBody = input("So, what's the distance from the gravitating body?")
findGravity(massOfBody, distanceFromBody)