def calculate_area(length, width):
  return length * width

def calculate_perimeter(length, width):
  return 2 * (length + width)

#Ex Usage
length = 5
width = 10
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print(f"The area of the rectangle is: {area}") 
print(f"The perimeter of the rectangle is: {perimeter}") 
