wieght = float(input("enter your wieght : "))
height = float(input("enter your height : "))
bmi = wieght / (height**2) 
print("Bmi is {}".format(round(bmi,2)))
if bmi <=18.4:
    print("underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("fit & healthy")
else:
    print("overwieght ")