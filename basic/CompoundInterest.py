principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("enter the principle amount:"))
    if principle <=0:
        print("the principle can't be less than or equal to zero")
    elif principle < 1000:
        print("you are a fucking poor guy :)))")

while rate <= 0:
    rate = float(input("enter the interest rate:"))
    if rate <=0:
        print("interest rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("enter the time in years:"))
    if time <=0:
        print("time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years is:{total:.3f}")