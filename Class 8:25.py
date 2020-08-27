import random
rain_val = random.randint(1, 2)

where_str=input("Put in I for indoors or O for outdoors\n")
if where_str=="I":
    if rain_val==1:
        print("Happy day! You made the right choice!")
    else:
        print("Rats! You could've been outside.")
else:
    if rain_val==1:
        print("Sad! You're soaked!")
    else:
        print("Yay! Happy dance! You made the right choice!")

A = 18800
r = 0.05
n = 48
p = A * (r / 12 / (1 - (1 + r / 12)**(-1 * n)))
print(p)

try:
    age_str = input("Your age: ")
    age_int = int(age_str)
except:
    print("age is out of bounds!")

if age_int <=20:
    loan_app=False
elif age_int <= 40:
    inc_str = input("income: ")
    inc_int = int(inc_str)
    if inc_int > 166500:
        loan_app = True
    else:
        sav_str = input("savings: ")
        sav_int = int(sav_str)
        if sav_int > 657:
            loan_app = True
        else:
            loan_app = False
else:
    sav_str = input("savings: ")
    sav_int = int(sav_str)
    if sav_int >= 433:
        loan_app = True
    else:
        loan_app = False

if loan_app:
    print("Yay! Loan approved")
else:
    print("Nay. Loan denied")