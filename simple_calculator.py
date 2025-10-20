"""
Filename: simple_calculator.py
Author: <Guardado, Gabriela>
Created: <08/28/2025>
Instructor: Holtslander
"""

print("Hello, welcome to this simple calculator!" "Here we only show the four main types of math. Addition, subtraction, multiplication, and division.")

num1 = input("Please input your first number without any commas\n")
num2 = input("Please input your second number without any commas\n")

num1 = int(num1)
num2 = int(num2)

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

print("Thank you for using this simple calculator!" "Have a nice day! :)")