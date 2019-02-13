#enter weight
weight = input("enter your weight(kg):")
#enter height
height = input("enter your height(m):")

bmi = round (float(weight) / ( float(height)**2 ), 2)

if bmi > 0 :
     # the fattest   
    if bmi >= 35:
        print(f"your BMI is {bmi} and the fattest!")
        #fatter
    elif bmi >= 30 and bmi < 35:
        print(f"your BMI is {bmi} and fatter!")
    #fat
    elif bmi >= 27 and bmi < 30:
        print(f"your BMI is {bmi} and fat!")
    # heavy
    elif bmi >= 24 and bmi < 27:
        print(f"your BMI is {bmi} and heavy!")
    #normal
    elif bmi >= 18.5 and bmi< 24:
        print(f"your BMI is {bmi} and normal!")
    #too light
    else:
        print(f"your BMI is {bmi} and too light!")


else:
    print("please check again!")