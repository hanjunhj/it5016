"""
Calculate the radius of a circle, given the area
Author: James Bond
"""
import math
area = float(input("Enter the area value:"))  #input area value
radius = math.sqrt(area / math.pi)

print("Radius of circle is", radius)
