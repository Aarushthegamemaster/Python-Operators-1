english = int(input("Your marks in english is"))
hindi = int(input("Your marks in hindi is"))
math = int(input("Your marks in math is"))
science = int(input("Your marks in science is"))

sum = english+math+science+hindi
percentage = (sum/400)*100
print("Your percentage is",percentage)