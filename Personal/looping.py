#for loop
#while loop
#while True
#for else
#while else

#1
# n = int(input("Enter number (1-100) : "))
# for i in range(1,n+1):
#     print(i)

#2
# n = int(input("Enter number : "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum +i
# print(f"The sum of {n} is {sum}")

#3
# n = int(input("Enter number which multiplication table you want : "))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

#4
# n = int(input("Enter a number : "))
# temp = n
# if n==0:
#     cnt = 1
# else:
#     cnt = 0
#     while n>0:
#         n = n//10   #1234
#         cnt = cnt +1
# print(f"Total digits in {temp} : {cnt}")

#5
# n = int(input("Enter a number : "))
# temp = n
# reverse = 0
# remain = 0
# while temp>0:
#     remain = temp%10    
#     reverse = reverse * 10 + remain   
#     temp = temp//10   
# print(f"The reverse number of {n} is {reverse}")

   
#6
# n = int(input("Enter a number : "))
# temp = n
# reverse = 0
# remain = 0
# while temp>0:
#     remain = temp%10    
#     reverse = reverse * 10 + remain   
#     temp = temp//10   
# if reverse == n:
#     print(f"The number {n} is pelindrome")
# else:
#     print(f"The number {n} is not pelindrome")

#7
# n = int(input("Enter a number : "))
# original = n
# digits = len(str(n))
# if n==0:
#     print(f"{n} is a armstrong number")
# else:
#     sum = 0
#     cnt = 0
#     while n>0:
#         digit = n%10
#         sum = sum + (digit**digits)
#         n = n//10
#     if sum==original:
#         print(f"Number {original} is a Armstrong Number")
#     else:
#         print(f"{original} is not a Armstrong Number")

#8
# import random
# number = random.randint(1,20)
# while True:
#     guess = int(input("guess number between (1-20) : "))
#     if guess==number:
#         print(f"You got this time its {number} corret ✔")
#         break
#     elif guess<number:
#         print(f"its less")
#         continue
#     elif guess>number:
#         print(f"its big")
#         continue
#     else:
#         print("You enter something wrong")
#         continue

    
