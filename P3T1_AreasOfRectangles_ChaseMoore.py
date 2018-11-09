#P3T1 - Area of a rectangle

#Input the length and width of rectangle 1.
#Input the length and width of rectangle 2.
#Calculate the area of rectangle 1.
#Calculate the area of rectangle 2.


#Calculate the area of rectangle 1.
length1 = input("Enter the length of triangle: ")
width1 = input ("Enter the width of the triangle: ")
area1 = int(length1) * int(width1)
print("Area of rectangle is " + str(area1))

#Calculate the area of rectangle 2.
length2 = input("Enter the length of triangle: ")
width2 = input("Enter the width of the triangle: ")
area2 = int(length2) * int(width2)
print("Area of rectangle 2 is " + str(area2))

#Determine which triangle has the greater area
if area1 > area2:
    print("Rectangle 1 has the greater area.")

elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("The rectangles have the same area.")

    
