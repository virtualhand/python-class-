def area(length):
   # """Calculate the surface area of a cube with the given length"""
   return 6 * length ** 2

def volume(length):
   # """Calculate the volume of a cube with the given length"""
    return length ** 3

#if __name__ == '__main__':
    # Ask the user for the length of the cube
#    length = float(input("Enter the length of the cube: "))

    # Calculate the area and volume of the cube using the functions
 #   cube_area = area(length)
  #  cube_volume = volume(length)

    # Print out the results
   # print(f"The surface area of the cube is {cube_area:.2f} square units.")
    #print(f"The volume of the cube is {cube_volume:.2f} cubic units.")

# Get the length of the cube from the user
length = float(input("Enter the length of the cube: "))

# Calculate the area and volume
area = 6 * length ** 2
volume = length ** 3

# Print the results
print("The area of the cube is:", area)
print("The volume of the cube is:", volume)





