# s1 = 'Mahesh'
# s2 = "hello"
# s3 = '''good'''
# s4 = "i like java"
# s5 = '''This is a Python lecture
# But Today i am doing a Hospital management Project'''
# print(s5)                             #printing a string inside triple quotes which contains multiple line
# print(type(s1))
# print(type(s2))
# print(type(s3))
# print(s1)                             #print complete string
# print(s1[0])                          #print a specific index letter
# print(s1[0:len(s1)])                  #print string using slicing
# print(s2+" "+s1)                      #to concate two strings
# print(len(s1))                        #to find length of any string
# print(s1.upper())                     #to convert string into uppercase
# print(s1.lower())                     #to convert string into lowercase
# print(s1.swapcase())                  #used to swap the case of string like lower letter->upper & upper letter->lower letter
# print(s4.replace("java","Python"))    #used to replace a word with another in string
# for i in s1:
#     print(i)


#PRACTICE QUESTIONS:

#CREATE BASIC FORM THAT TAKES USER DATA(FIRST NAME, LAST NAME, ADDRESS, PHONE NUMBER(MUST INTEGER), EMAIL)
# head = "REGESTRATION FORM"
# print(head.center(100,"-"))
# print("\n")
# first_name = input("FIRST NAME : ")
# last_name = input("LAST NAME : ")
# address = input("ADDRESS : ")
# mb = int(input("PHONE NUMBER : "))
# email = input("EMAIL ADDRESS : ")
# print("\n")
# print(80*"=")
# print(f'''NAME : {first_name} {last_name}
# ADDRESS : {address}
# PHONE NUMBER : {mb}
# EMAIL ADDRESS : {email}''')
# print(80*"=")

#TAKE CITY NAME FROM USER AND FIND LENGTH
# city = input("CITY NAME : ")
# print(len(city))

#TAKES USER INPUT(FIRST NAME AND LAST NAME) AND PRINT FULL NAME USING CONCATENATION
# first_name = input('ENTER FIRST NAME : ')
# last_name = input('ENTER LAST NAME : ')
# print(f"FULL NAME : {first_name} {last_name}")

#TAKE SENTENCE FROM USERS, SENTENCE IS A ADDRESS AND REPLACE OLD ADDRESS WITH NEW ADDRESS
# sentence1 = input('OLD ADDRESS : ')
# print(50*"-")
# print(f"NAME : MAHESH KUMAWAT")
# print(f"ADDRESS : {sentence1}")
# print(50*"-")
# sentence2 = input('NEW ADDRESS : ')
# print(50*"-")
# print("NAME : MAHESH KUMAWAT")
# print(f"ADDRESS : {sentence1.replace(sentence1,sentence2)}")
# print(50*"-")

#TAKES THE FULL NAME FROM USER AND PRINT IT REVERSE FROM
# name = input("Enter Your Full Name : ")
# print(f"Reverse Name : {name[::-1]}")



