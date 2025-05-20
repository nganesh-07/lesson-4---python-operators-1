# calculate grades in 3 classes

econ = int(input("enter points for econ:"))
english = int(input("enter points for english:"))
physics = int(input("enter points for physics:"))

sum = econ + english + physics
print(sum)

percentage = (sum/300)*100
print(percentage)