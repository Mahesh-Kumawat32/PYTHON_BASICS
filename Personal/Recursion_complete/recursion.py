#SCORE 9/10 AS NORMAL PYTHON SOLUTION
#SCORE 0/10 AS RECURSIVE APPROACH

# #1
# n = int(input("Enter number which factorial you want : "))
# def fact_find(n):
#     fact = 1
#     if n==0 or n==1:
#         return 1
#     else:
#         for i in range(1,n+1):
#             fact = fact * i
#         return fact
# print(f"The factorial of {n} is {fact_find(n)}")
        
# #2
# n = int(input("Enter length of fibonacci series : "))
# def find_fib(n):
#     if n==0 or n==1:
#         return 0
#     else:
#         a,b = 0,1
#         for i in range(1,n+1):
#             print(f"{a} ",end = "")
#             c = a+b
#             a = b
#             b = c
# find_fib(n)

# #3
# n = int(input("Enter a number : "))
# original = n
# def find_digit_sum(n):
#     if n==0:
#         return 0
#     else:
#         sum = 0
#         for i in range(0,len(str(n))):
#             digit = n%10
#             sum = sum + digit
#             n = n//10
#         return sum
# print(f"The sum of {original} is {find_digit_sum(n)}")

# #4
# something = input("Enter Something : ")
# def reverse_string(something):
#     if something.isdigit():
#         print("You enter that contain digits that is not allow!")
#     else:
#         print(f"Reverse string : {something[::-1]}")
# reverse_string(something)

# #5
# something = input("Enter Something : ")
# original = something
# def check_str_pelindrome_or_not(something):
#     if something.isdigit():
#         print("You enter that contain digits that is not allow!")
#     else:
#         reverse_string = something[::-1]
#         if reverse_string == original:
#             print(f"String is pelindrome")
#         else:
#             print("String is not pelindrome")
# check_str_pelindrome_or_not(something)

# #6
# n = int(input("Enter a number : "))
# original = n
# def count_numbers_in_digit(n):
#     if n in range(0,10):
#         return 1
#     else:
#         cnt = 0
#         for i in range(0,len(str(n))):
#             digit = n % 10
#             cnt = cnt +1 
#             n = n//10
#         return cnt
# print(f"Total Digits in {original} : {count_numbers_in_digit(n)}")

# #7
# Base = int(input("Enter Base : "))
# Exponent = int(input("Enter Exponent : "))
# def find_exponent(Base,Exponent):
#     if Base==0:
#         return 0
#     elif Exponent==0:
#         return 1
#     else:
#         return Base**Exponent
# print(f"Result : {find_exponent(Base,Exponent)}")

# #8
# l = [1,23,90,45,151,345,400]
# def find_largest_from_list(l):
#     l = sorted(l)
#     return l[len(l)-1]
# print(f"Largest Element : {find_largest_from_list(l)}")

# 9
# n = int(input("Enter a number in decimal form : "))
# def convert_decimal_to_binary(n):
#     binary_num = bin(n)
#     return binary_num
# print(f"Decimal            Binary")
# print(f"{n}         {convert_decimal_to_binary(n)}")

# #10
# something = input("Enter Something : ")
# def count_vowels(something):
#     cnt = 0
#     for i in range(0,len(something)):
#         if ('a' in something[i] or
#             'i' in something[i] or
#             'e' in something[i] or
#             'u' in something[i] or
#             'o' in something[i] or
#             'A' in something[i] or
#             'E' in something[i] or
#             'O' in something[i] or
#             'U' in something[i] or
#             'I' in something[i] 
#         ):
#             cnt = cnt +1
#         else:
#             continue
#     return cnt
# print(f"Count of Vowels : {count_vowels(something)}")