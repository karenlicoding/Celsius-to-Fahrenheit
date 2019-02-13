#enter country
country = input("where do you come from? 1.Taiwan 2.U.S.A. :")
country = int(country)
if country == 1 or country == 2:

    #enter age
    age = input("enter your age:")
    age = int(age)
    #result
    if country == 1 and age >= 18:
        print("In taiwan, you can drive!")
    elif country == 2 and age >= 16:
        print("In U.S.A., you can drive!")
    else:
        print("Sorry, you are too young!")
else:
    print("your enter is error, please again!")

