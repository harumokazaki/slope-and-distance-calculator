import math

points_1 = (input('Enter your first points: '))
points_2 = (input('Enter your second points: '))
set_one = [int(first_points) for first_points in points_1.split(', ')]
x1 = set_one[0]
y1 = set_one[1]

set_two = [int(second_points) for second_points in points_2.split(', ')]
x2 = set_two[0]
y2 = set_two[1]

slope = (y2 - y1) / (x2 - x1)
distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
distance = math.sqrt(distance)
print(slope)
print(distance)
