
def bmi_calci(height,weigth):
    bmi=float(weigth/(height*height))
    if bmi<18.5:
        print("underweight")
    elif bmi>18.5 and bmi<25:
        print("normal weight")
    elif bmi>25 and bmi<30:
        print("overweight")
    elif bmi>30 and bmi<35:
        print("obese")
    else:
        print("critically obese")

height=float(input("enter your height in m:"))
weight=float(input("enter your weigth in kg:"))
bmi_calci(height,weight)