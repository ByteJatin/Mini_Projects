import math # Imported Math/Numbers(by random)

print("🔲 -- Area Calculator Menu -- 🔲")
print("1. Triangle 🔺")
print("2. Rectangle ➖")
print("3. Square 🟩")
print("4. Circle 🔵")
print("5. Exit 🙏")

options = input("Please select an option (1-5): ") # Choose your shape.

if options == "1":
    height = float(input("Enter the height of the triangle: "))
    base = float(input("Enter the base of the triangle: "))
    area = 1/2 * base * height # Triangle's Area Formulae
    print("Total Area of Triangle is:", area)

elif options == "2":
    length = float(input("Enter the lenght of the Rectanlge: "))
    breadth = float(input("Enter the breadth of the Rectangle: "))
    area = 2 * length + breadth # Rectangle's Area Formulae
    print("Total Area of the Rectangle is", area)

elif options == "3":
    side = float(input("Enter the side of the Square: "))
    area = side * side # Square's Area Formulae
    print("Total Area of the Square is", area)

elif options == "4":
    radius = float(input("Enter the Radius of the Circle: "))
    area = 3.14 * radius ** radius # Circle's Area Formulae
    print("Total Area of the Circle is", area)

elif options == "5":
    print("Exiting...👋") # Exit, If you don't know how to calculate.

else:
    print("Invalid Options Choice, Please Select from 1 - 5") # FAAAH
