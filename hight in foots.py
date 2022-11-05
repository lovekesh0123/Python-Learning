#write a short program that asks you for height in centimeters and then converts your height to feet and inches (1 foot = 12 inches, 1 inch = 2.54 cm)
a=int(input("ENTER YOUR HEIGHT in cm="))
b=(a/2.54)
c=b//12
d=b-(c*12)
print(f"your height is {c} foot and {d}inch",)