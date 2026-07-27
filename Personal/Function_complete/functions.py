#1
# def helloworld():
#     print("Hello World")
# helloworld()

#2
# def greet(name):
#     print(name)
# greet("Mahesh")

#3
# def greet(name):
#     print("Hello ",name)
# greet("Mahesh")

#4
# def sum(a,b):
#     print(f"The sum of {a} and {b} is {a+b}")
# sum(10,20)

#5
# a = int(input("Enter a number which square you want : "))
# def square(n):
#     print(f"The square of {n} is {n**2}")
# square(a)

#6
# n = int(input("Enter a number which cube you want : "))
# def cube(n):
#     print(f"The cube of {n} is {n*n*n}")
# cube(n)

#7
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# def large_of_two(a,b):
#     if a>b:
#         print(f'The number {a} is greater than {b}')
#     else:
#         print(f'The number {b} is greater than {a}')
# large_of_two(a,b)

#8
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# def small_of_two(a,b):
#     if a<b:
#         print(f'The number {a} is less than {b}')
#     else:
#         print(f'The number {b} is less than {a}')
# small_of_two(a,b)

#9
# l = float(input("Enter length of rectangle : "))
# b = float(input("Enter width of rectangle : "))
# def rectangle_area(l,b):
#     print(f"The area of rectangle which length is {l} and width is {b} is : {l*b}")
# rectangle_area(l,b)

#10
# l = float(input("Enter length of rectangle : "))
# b = float(input("Enter width of rectangle : "))
# def rectangle_perimeter(l,b):
#     print(f"The perimeter of rectangle which length is {l} and width is {b} is : {2*(l+b)}")
# rectangle_perimeter(l,b)

#11
# n = int(input("Enter a number : "))
# def evenodd(n):
#     if n%2==0:
#         print(f"The number {n} is even")
#     else:
#         print(f"The number {n} is odd")
# evenodd(n)

#12
# n = int(input("Enter a number : "))
# def absolute_value(n):
#     if n>0:
#         print(f"You enter {n}")
#     elif n<0:
#         print(f"You enter {-1*(n)}")
#     elif n==0:
#         print(f"You enter zero")
#     else:
#         print('You enter a wrong number')
# absolute_value(n)

#13
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# c = int(input("enter third one : "))
# def avg_three(a,b,c):
#     avg = 0
#     avg = (a+b+c)/3
#     print(f"The average of {a},{b} and {c} is {avg}")
# avg_three(a,b,c)

#14
# a = int(input("Enter first value (must integer): "))
# b = int(input("Enter second value (must integer): "))
# def swap_two_numbers(a,b):
#     temp = a
#     a = b
#     b = temp
#     print(f"The swaped number are a = {a} and b = {b}")
# swap_two_numbers(a,b)

#15
# n = int(input("Enter a number : "))
# def find_last_digit(n):
#     last_digit = n%10
#     print(f"The last digit of the number {n} is {last_digit}")
# find_last_digit(n)

#16
# n = int(input("Enter the number which factorial you want : "))
# def fact(n):
#     facto = 1
#     for i in range(1,n+1):
#         facto = facto*i
#     print(f"The value of factorial of {n} is {facto}")
# fact(n)

#17
# n = int(input("Enter the number : "))
# def sum_of_n_num(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#     print(f"The sum of first {n} number is {sum}")
# sum_of_n_num(n)

#18
# n = int(input("Enter the number which mulitplication table you want : "))
# def multiplication(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")
# multiplication(n)

#extra sum of 1-100 even number and same for odd number with minor changes
# n = int(input("Enter the number : "))
# def sum_of_n_num(n):
#     sum = 0
#     for i in range(1,n+1):
#         if i%2==0:
#             sum = sum + i
#         else:
#             continue
#     print(f"The sum of first {n} number is {sum}")
# sum_of_n_num(n)

#19
# n = int(input("Enter a number upto to which you want even numbers : "))
# def evennum(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i)
#         else:
#             continue
# evennum(n)

#20
# n = int(input("Enter a number upto to which you want even numbers : "))
# def oddnum(n):
#     for i in range(1,n+1):
#         if i%2!=0:
#             print(i)
#         else:
#             continue
# oddnum(n)

#21
# n = (input("Enter a number : "))
# def return_num_total(n):
#     total_digit = len(n)
#     print(f"The total digit in number {n} is {total_digit}")
# return_num_total(n)

#22
# n = int(input("Enter a number : "))
# temp = n
# def reverse_num(temp):
#     reverse = 0
#     remainder = 0
#     while temp>0:
#         remainder = temp %10
#         reverse = reverse * 10 + remainder
#         temp = temp // 10
#     print(f"The Reverse number of {n} is {reverse}")
# reverse_num(temp)

#23
# n = int(input("Enter a number : "))
# temp = n
# def reverse_num(temp):
#     reverse = 0
#     remainder = 0
#     while temp>0:
#         remainder = temp %10
#         reverse = reverse * 10 + remainder
#         temp = temp // 10
#     if reverse==n:
#         print(f"{n} is a pelindrome number")
#     else:
#         print(f"{n} is not pelindrome")
# reverse_num(temp)

#24
# ARMSTRONG NUMBER : An Armstrong number (also called a Narcissistic number) is a number that is equal to the sum of its own digits, where each digit is raised to the power of the total number of digits in the number.
# n = int(input("Enter a number : "))
# def armstrong_or_not(n):
#     global temp
#     temp = n
#     digits = len(str(n))
#     total = 0
#     while n>0:
#         digit = n%10
#         total = total+(digit**digits)
#         n = n//10
#     return temp == total
# if armstrong_or_not(n):
#     print(f"{temp} is a armstrong number")
# else:
#     print(f"{temp} is not a armstrong number")

#25
# A prime number is a natural number greater than 1 that has exactly two factors:
    # means only divisible by 1, or itself
# n = int(input("Enter a number : "))
# def prime_or_not(n):
#     global cnt
#     cnt = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             cnt = cnt +1
#         else:
#             continue
#     return cnt
# if prime_or_not(n)==2:
#     print(f"{n} is a prime number ")
# else:
#     print(f"{n} is not a prime number")

#=======================================================
#ANOTHER SET
#=======================================================
#1
# l = float(input("Enter Length : "))
# b = float(input("Enter Width : "))
# def calculate_area(l,b):
#     print(f"The area of rectangle which length is {l} and width is {b} is : {l*b}")
# calculate_area(l,b)
    
#2
# def evenodd(n):
#     if n%2==0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")
# n = int(input("Enter a number : "))
# evenodd(n)

#3
# def max_or_min(a,b,c):
#     if a>b and a>c:
#         print(f"{a} is maximum")
#     elif b>a and b>c:
#         print(f"{b} is maximum")
#     else:
#         print(f"{c} is maximum")
# a = int(input("Enter a number : "))
# b = int(input("Enter a number : "))
# c = int(input("Enter a number : "))
# max_or_min(a,b,c)

#4
# def calcius_to_feranhide(c):
#     far = (c*(9/5))+32 
#     return far
# c = float(input("Enter temprature in celcius : "))
# print(f"""Calcius = {c}\nFahrenheit = {calcius_to_feranhide(c)}""")

#5
# something = input("Enter a word : ")
# def find_vowel(something):
#     cnt = 0
#     for i in something:
#         if i=='a' or i=="e" or i=='i' or i == 'o' or i =='u' or i=='A' or i=="E" or i=='I' or i == 'O' or i =='U':
#             cnt = cnt +1
#         else:
#             continue
#     return cnt
# print(f"The vowel in the word {something} are total : {find_vowel(something)}")

#6
# n = int(input("Enter a number : "))
# def find_pelindrome_or_not(n):
#     temp = n
#     remain = 0
#     reverse = 0
#     while temp>0:
#         remain = temp %10
#         reverse = reverse * 10 + remain
#         temp = temp //10
#     if reverse==n:
#         print(f"The number {n} is a pelindrome number because {n} = {reverse}")
#     else:
#         print(f"{n} is not a pelindrome number because {n} != {reverse}")
# find_pelindrome_or_not(n)

#7
# def find_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     print(f"The factorial of the number {n} is {fact}")
# n = int(input("Enter a number which factorial you want : "))
# find_fact(n)

#8
# n = int(input("Enter a number to check it is prime or not : "))
# def find_prime_or_not(n):
#     cnt = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             cnt += 1
#         else:
#             continue
#     if cnt ==2:
#         print(f"The number {n} is a prime number")
#     else:
#         print(f"{n} is not a prime number")
# find_prime_or_not(n)

#9
# method -1: using type conversion list --->set-->list
# l = []
# while True:
#     n = int(input("Enter element of list : "))
#     l.append(n)
#     choice = input("You want to add more element to list (yes/no) : ")
#     if choice =="Yes" or choice =="yes":
#         continue
#     elif choice =="No" or choice == "no":
#         break
# def find_unique_from_list(l):
#     l = set(l)
#     l.union()
#     l = list(l)
#     print(f"After removing duplicate elements list is {l}")
# print(f"\n\n\nBefore removing duplicate elements list is {l}")
# find_unique_from_list(l)


#method -2: using list itself
# l = []
# while True:
#     n = int(input("Enter element of list : "))
#     l.append(n)
#     choice = input("You want to add more element to list (yes/no) : ")
#     if choice =="Yes" or choice =="yes":
#         continue
#     elif choice =="No" or choice == "no":
#         break
# def find_unique_from_list(l):
#     cnt = 0
#     for i in range(0,len(l)):
#         cnt = l.count(i)
#         if cnt==1:
#             continue
#         else:
#             while l.count(i)>1:
#                 l.remove(i)
#     print(sorted(l))
# find_unique_from_list(l)


#10
# marks = []
# while True:
#     n = int(input("Enter marks : "))
#     marks.append(n)
#     choice = input("You want to add more student marks to list (yes/no) : ")
#     if choice =="Yes" or choice =="yes":
#         continue
#     elif choice =="No" or choice == "no":
#         break
# def find_avg_marks(marks):
#     sum = 0
#     for i in range(0,len(marks)):
#         sum = sum + marks[i]
#     avg_result = sum/len(marks)
#     return avg_result
# print(f"The Average Result of institute is {find_avg_marks(marks)}")

#11
# l = [1,2,3,4,1,5,6,2,4]
# def find_second_largest(l):
#     l = set(l)
#     l.union()
#     l = list(l)
#     sorted(l)
#     print(l)
#     print(l[len(l)-2])
# find_second_largest(l)

#12
# sentence = input("Enter a sentence : ")
# s=sentence.lower()
# data = {}
# def word_frequency(s):
#     l = s.split()
#     cnt = 0
#     for i in range(0,len(l)):
#         cnt = l.count(l[i])
#         data[l[i]] = cnt
#     print(data)
# word_frequency(s)


#13

#14

#15
# cst_name = input("Enter Customer Name : ")
# dt = "22-07-2026"
# addrs = input("Enter Customer Address : ")
# bill_data = {}
# def bill(cst_name, dt, addrs):
#     while True:
#         n = input("Enter item name : ")
#         price = float(input("Enter item price : "))
#         total_peice = int(input("Enter items peice : "))
#         bill_data[n] = (price*total_peice+(price*total_peice*0.18))
#         choice = input("You want to add more items to bill(yes,no) : ")
#         if choice == "yes":
#             continue
#         else:
#             break
#     greet = "BILL"
#     print(greet.center(50,"="))
#     print(f"Customer Name : {cst_name}")
#     print(f"Customer Address : {addrs}")
#     print(f"Date : {dt}")
#     for a,b in bill_data.items():
#         print(f"{a} : {b}")
#     total_bill = 0
#     for i in bill_data.values():
#          total_bill= total_bill + i
#     print(f"Total Amount : {total_bill}")
#     end="="
#     print(end.center(50,"="))
# bill(cst_name, dt, addrs)

#16
# heading = "GET RESULT"
# print("\n",heading.center(100,"*"))
# student_name = input("Enter Your Name : ")
# student_roll_no = int(input("Enter Your Roll No : "))
# result = float(input("Enter Your Marks : "))
# def get_result(student_name,student_roll_no, result):
#     result_head = "MARKSHEET"
#     print(result_head.center(30,"="))
#     if result>=90 and result<100:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : A""")
#     elif result>=80 and result<90:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : B""")
#     elif result>=70 and result<80:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : C""")
#     elif result>=60 and result<70:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : D""")
#     elif result>=40 and result<60:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : F""")
#     elif result<40:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Fail\nGrade : __""")
#     else:
#         print("You Entered Something Wrong")
#     print(f"\t\t\nTHANK YOU")
# get_result(student_name,student_roll_no, result)
# ending = "*"
# print(ending.center(100,"*"))

#17
# cst_names = {
#     "12345678" : {"Name" : "MAHESH KUMAWAT",    "Age":  19, "Current Balance":10000},
#     "23456789" : {"Name" : "CHAMPALAL KUMAWAT", "Age" : 30, "Current Balance":100000},
#     "34567890" : {"Name" : "SURESH KUMAWAT",    "Age" : 22, "Current Balance":30000},
#     "45678901" : {"Name" : "KHUSH KUMAWAT",     "Age" : 20, "Current Balance":50000},
#     "56789012" : {"Name" : "NARAYAN KUMAWAT",   "Age" : 28, "Current Balance":70000}
# }
# head = "SBI ATM"
# print(head.center(100,"="))
# language = input("SELECT LANGUAGE\nFOR ENGLISH PRESS : E\nFOR HINDI PRESS : H\n:==> ")
# choice = input("SELECT CHOICE\nFOR WITHDRAWL AMOUNT PRESS : W\nFOR CHECK AMOUNT PRESS : C\n:==>> ")
# def atmWithdrawl(choice):
#     main_format = "="
#     while True:
#         if choice =="W":
#             ac = input("ENTER YOUR 8 DIGIT AC/NO : ")
#             if ac in cst_names:
#                 withdrawl_amt  = int(input("ENTER AMOUNT WANT TO WITHDRWAL : "))
#                 if cst_names[ac]["Current Balance"]>withdrawl_amt:
#                     print(f"✔ YOU CAN WITHDRAWL : {withdrawl_amt}")
#                     confirm_withdrawl = input("FOR CONFIRM WITHDRAWL PRESS (D) : ")
#                     if confirm_withdrawl=="D":
#                         print("\n")
#                         print(main_format.center(100,"="))
#                         print(f"NAME : {cst_names[ac]["Name"]}")
#                         print(f"AGE : {cst_names[ac]["Age"]}")
#                         print(f"AC/NO : {ac}")
#                         print(f"WITHDRAWL AMOUNT : {withdrawl_amt}")
#                         print(f"CURRENT BALANCE : {(cst_names[ac]["Current Balance"] - withdrawl_amt)}")
#                         print(f"PREVIOUS BALANCE : {cst_names[ac]["Current Balance"]}")
#                         print(main_format.center(100,"="))
#                 else:
#                     print("\n")
#                     print(main_format.center(100,"="))
#                     print(f"😔YOU CANNOT WITHDRAWL {withdrawl_amt} BECAUSE YOUR BALANCE IS {cst_names[ac]["Current Balance"]}")
#                     print("PLEASE TRY AGAIN 🙂")
#                     print(main_format.center(100,"="))
#             else:
#                 print(f"CHECK YOUR ACCOUNT NUMBER AGAIN!")
#         elif choice =="C":
#             ac = input("ENTER YOUR 8 DIGIT AC/NO : ")
#             for a,b in cst_names[ac].items():
#                 print(f"{a} : {b}")
#             print(f"AC/NO : {ac}")
#         else:
#             print("YOU ENTER SOMETHING WRONG! PLEASE ENTER THE CORRECT INPUT😡")
#         permission = input("YOU WANT TO CONTINUE AGAIN (YES/NO)🤨: ")
#         if permission=="YES" :
#             continue
#         else:
#             break
# atmWithdrawl(choice)
# end = "="
# print(end.center(100,"="))

#18
# ALREADY DONE IN CLG PC

#19------------->>NOT MYSELF USING CHATGPT
# def email_validator(email):
#     if " " in email:
#         return False

#     if email.count("@")!=1:
#         return False

#     for ch in email:
#         if ch.isdigit():
#             break
#     else:
#         return False

#     username, domain = email.split("@")
#     if username =="" and username.islower()!=True:
#         return False
#     if domain=="":
#         return False
#     if not (
#         domain.endswith("gmail.com") or
#         domain.endswith(".org") or
#         domain.endswith(".net")
#     ):
#             return False 
#     return True

# while True:
#     permission = None
#     email = input("Enter Email : ")
#     if email_validator(email):
#         print(f"✔ Valid Email {email}")
#     else:
#         print(f"X Invalid Email {email}")
#         permission = input("Enter Email Again (YES/NO): ").upper()
#     if permission!="YES":
#         break


#20
# books = [
#     {'id':1,  'title':'Python Begineer',            'author' : 'Mahesh Kumawat',    'Price':400},
#     {'id':2,  'title':'Rich Dead Poor Dead',        'author' : 'John',              'Price':2000},
#     {'id':3,  'title':'Wings of Fire',              'author' : 'APJ Abdul Kalam',   'Price':500},
#     {'id':4,  'title':'Python Intermediate',        'author' : 'Mahesh Kumawat',    'Price':500},
#     {'id':5,  'title':'Python Advance',             'author' : 'Mahesh Kumawat',    'Price':800},
#     {'id':6,  'title':'Psychology of Money',        'author' : 'Morgan Housel',     'Price':1000},
#     {'id':7,  'title':'The Pragmatic Programmer',   'author' : 'David Thomas',      'Price':300},
#     {'id':8,  'title':'Git & Github',               'author' : 'Harry Das',         'Price':600},
#     {'id':9,  'title':'Html & Css',                 'author' : 'Shradha Khapra',    'Price':550},
#     {'id':10, 'title':'Clean Code',                 'author' : 'Robert C. Martin',  'Price':499}
# ]
# def search_books(books,Title):
#     cnt = 0
#     for i in range(0,len(books)):
#         if Title.title()==books[i]['title']:
#             cnt = cnt +1
#         else:
#             continue
            
#     if cnt ==1:
#         print("\n")
#         greet1 = "="
#         print(greet1.center(50,"*"))
#         print(f"{Title.title()} is Available ✔")
#         print(greet1.center(50,"="))
#         print(f"Book Title : {books[i]['title']}")
#         print(f"Book Author : {books[i]['author']}")
#         print(f"Book Price : {books[i]['Price']}")
#         print(greet1.center(50,"="))

#     else:
#         greet2 = "="
#         print(greet2.center(50,"="))
#         print(f"{Title.title()} is not found")
#         print(greet2.center(50,"="))
# while True:
#     Title = input("Enter Title of Book You Want : ")
#     search_books(books,Title)
#     permission = input("You want to search more books(YES/NO) : ").upper()
#     if permission == "YES":
#         continue
#     else:
#         break


        