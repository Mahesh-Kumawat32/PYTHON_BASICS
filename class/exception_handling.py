# a = 10
# m = 0 
# print(a/m)  #zero division error
# try:
#     num = a/m
#     print(num)
# except:
#     print("error occurs")

# try:
#     a = int(input("Enter number : "))
#     print(100/a)
# except ZeroDivisionError:
#     print("Number is not divided by 0")

# try:
#     a = input('Enter something in english character : ')
#     print(a)
# except ValueError:
#     print("Please enter english charcters only")

# try:
#     file = open("Python_notes.txt","r")
#     data=file.read()
#     print(data)
# except FileNotFoundError:
#     print("File not found")

# try:
#     a = int(input("Enter a number : "))
#     print(a)
# except ValueError:
#     print("Please enter a valid integer number")
# finally:
#     print("Program ended")
    

#PRACTICE QUESTIONS
#TAKES TWO NUMBER FROM USERS AND DIVIDE THEM AND HANDLE DIVISION BY 0 EXCEPTION
try:
    a = int(input("1st number : "))
    b = int(input("2nd number : "))
    print(a/b)
except ZeroDivisionError:
    print("number does not divide by zero")
finally:
    print("Program ended")
    
#TAKE AGE FROM USER USE HANDLE VALUE ERROR IF USER ENTER TEXT INSTEAD OF THE NUMBER
try:
    age = int(input("Enter your age : "))
except ValueError:
    print("Enter a valid age contains integer number")
finally:
    print("Program ended")

#CREATE A CALCULATOR PROGRAM AND PERFORM +,-,/,* AND HANDLE ZERO DIVISION

#TAKE MARKS FROM USERS AND COVERT THEM TO INTEGER AND HANDLE VALUE ERROR
try:
    marks = float(input('Enter your marks : '))
    marks = int(marks)
    print(f"Your marks is {marks}")

except:
    print("Enter a valid marks contains decimal or integer numbers")
finally:
    print("progran ended")


#TAKE A NUMBER FROM USER AND DIVIDE BY 100 AND HANDLE VALUE ERROR AND DIVISION ZERO ERROR
try:
    n = int(input("Enter a number : "))
    print(100/n)
except ValueError:
    