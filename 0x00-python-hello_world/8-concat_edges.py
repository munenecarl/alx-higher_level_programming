#!usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str.split(", ")[-1].split(" ")[0] + "-" + str.split(" ")[-2] + " " + str.split(" ")[-1])
print(str)
