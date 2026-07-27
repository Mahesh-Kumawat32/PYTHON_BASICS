#if
#if-else
#if-elif-else
#match case
#nested if-else

#1
# n = int(input("Enter a integer number : "))
# if n>0:
#     print(f"{n} is positive")
# elif n==0:
#     print(f"Number is Zero")
# elif n<0:
#     print(f"{n} is Negative")
# else:
#     print(f"You enter a wrong number")

#2
# n = int(input("Enter a integer number : "))
# if n%2==0:
#     print(f"{n} is Even")
# elif n%2!=0:
#     print(f"{n} is Odd")
# else:
#     print(f"You enter something wrong! try again")

#3
# n1 = int(input("Enter first number : "))
# n2 = int(input("Enter second number : "))
# n3 = int(input("Enter third number : "))
# if n1>n2 and n1>n3:
#     print(f"{n1} is greter than {n2} and {n3}")
# elif n2>n1 and n2>n3:
#     print(f"{n2} is greter than {n1} and {n3}")
# else:
#     print(f"{n3} is greter than {n1} and {n2}")

#4
# year = int(input("Enter Year : "))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print(f"{year} is a Leap year")
# else:
#     print(f"{year} is not a Leap year")

#5
# sub1 = float(input("Enter Your Maths Marks : "))
# sub2 = float(input("Enter Your Science Marks : "))
# sub3 = float(input("Enter Your English Marks : "))
# sub4 = float(input("Enter Your Social Science Marks : "))
# sub5 = float(input("Enter Your Computer Marks : "))

# total_marks = (sub1+sub2+sub3+sub4+sub5)
# percenatage = total_marks/5


# if percenatage>=90 and percenatage<100:
#     print(60*"-")
#     print(f"Percentage % = {percenatage}")
#     print(f"Result : Pass")
#     print(f"Grade : A")
#     print(60*"-")
# elif percenatage>=80 and percenatage<90:
#     print(60*"-")
#     print(f"Percentage % = {percenatage}")
#     print(f"Result : Pass")
#     print(f"Grade : B")
#     print(60*"-")
# elif percenatage>=70 and percenatage<80:
#     print(60*"-")
#     print(f"Percentage % = {percenatage}")
#     print(f"Result : Pass")
#     print(f"Grade : C")
#     print(60*"-")
# elif percenatage>=50 and percenatage<70:
#     print(60*"-")
#     print(f"Percentage % = {percenatage}")
#     print(f"Result : Pass")
#     print(f"Grade : D")
#     print(60*"-")
# elif percenatage>=35 and percenatage<50:
#     print(60*"-")
#     print(f"Percentage % = {percenatage}")
#     print(f"Result : Pass")
#     print(f"Grade : F ")
#     print(60*"-")
# elif percenatage<35:
#     print(60*"-")
#     print(f"Percentage % = {percenatage}")
#     print(f"Result : Fail")
#     print(f"Grade : - ")
#     print(60*"-")
# else:
#     print(60*"-")
#     print("You enter something wrong ")
#     print(60*"-")

#6
# units = int(input("Enter Units : "))
# if units>=0 and units<=100:
#     print(60*"-")
#     print(f"UNITS : {units}")
#     print(f"BILL : ₹ {units*5}")
#     print(60*"-")
# elif units>100 and units<=200:
#     print(60*"-")
#     print(f"UNITS : {units}")
#     print(f"BILL : ₹{units*7}")
#     print(60*"-")
# elif units>200 and units<=300:
#     print(60*"-")
#     print(f"UNITS : {units}")
#     print(f"BILL : ₹ {units*9}")
#     print(60*"-")
# elif units>300:
#     print(60*"-")
#     print(f"UNITS : {units}")
#     print(f"BILL : ₹ {units*11}")
#     print(60*"-")
# else:
#     print(60*"-")
#     print(f"YOU ENTER SOMETHING WRONG!")

#7
# balance = int(input("Enter Your Balance : "))
# withdrawl_amt = int(input("Enter Withdrawl amount (like: 100,500,100 | not like: 323/340 etc.): "))
# if withdrawl_amt%100==0 and withdrawl_amt<balance:
#     if (balance-withdrawl_amt)>500:
#         print("Withdrawl Successfully")
#         print(f"Remaining Balance : {balance-withdrawl_amt}")
#     else:
#         print("Insufficeint Balance")
# else:
#     print(f"You cannot Withdrawl {withdrawl_amt} due to less balance or incorret input")
    
#8
# weight = float(input("ENTER YOUR WEIGHT (KG) : "))
# height = float(input("ENTER YOUR HEIGHT (METER) : "))
# bmi = weight/(height**height)
# if bmi<18.5:
#     print("UNDER WEIGHT")
# elif bmi>=18.5 and bmi<24.9:
#     print("NORMAL WEIGHT")
#     print("GOOD 👍")
# elif bmi>=24.9 and bmi<29.9:
#     print("OVER WEIGHT")
# elif bmi>30.0:
#     print("OBESE")
# else:
#     print("YOU ENTER SOMETHING WRONG!")

#9
# username = input("USERNAME : ")
# password = input("PASSWORD : ")
# print("YOUR CREDENTIAL STORED SUCCESSFULLY 👍")
# print("NOW VALIDATE THEM BY RE ENTERING AGAIN : ")
# check_username = input("USERNAME : ")
# check_password = input("PASSWORD : ")
# if username==check_username and check_password==password:
#     print(40*"-")
#     print("YOU ARE LOGGED IN SUCCESSFULLY 😊")
#     print(40*"-")
# else:
#     print(40*"-")
#     print("YOUR CREDENTIAL ARE WRONG!")
#     print(40*"-")

#10
# item = input("ENTER ITEM YOU WANT TO BUY : ")
# price = float(input("PRICE : "))

# if price>0 and price<500:
#     print(40*"-")
#     print(f"ITEM NAME : {item}")
#     print(f"ITEM PRICE : {price}")
#     print(f"FINAL AMOUNT : {price} (NO DISCOUNT)")
#     print(40*"-")
# elif price>=500 and price<1000:
#     print(40*"-")
#     print(f"ITEM NAME : {item}")
#     print(f"ITEM PRICE : {price}")
#     print(f"ITEM DISCOUNT : {price*0.2}")
#     print(f"FINAL AMOUNT : {price-(price*0.2)} (20% DISCOUNT)")
#     print(40*"-")
# elif price>=1000 and price<2000:
#     print(40*"-")
#     print(f"ITEM NAME : {item}")
#     print(f"ITEM PRICE : {price}")
#     print(f"ITEM DISCOUNT : {price*0.3}")
#     print(f"FINAL AMOUNT : {price-(price*0.3)} (30% DISCOUNT)")
#     print(40*"-")
# elif price>=2000 and price<5000:
#     print(40*"-")
#     print(f"ITEM NAME : {item}")
#     print(f"ITEM PRICE : {price}")
#     print(f"ITEM DISCOUNT : {price*0.4}")
#     print(f"FINAL AMOUNT : {price-(price*0.4)} (40% DISCOUNT)")
#     print(40*"-")
# elif price>=5000:
#     print(40*"-")
#     print(f"ITEM NAME : {item}")
#     print(f"ITEM PRICE : {price}")
#     print(f"ITEM DISCOUNT : {price*0.5}")
#     print(f"FINAL AMOUNT : {price-(price*0.5)} (50%) DISCOUNT")
#     print(40*"-")
# else:
#     print(40*"-")
#     print("YOU ENTER SOMETHING WRONG!")
#     print(40*"-")