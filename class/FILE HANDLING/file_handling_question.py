#WRITE YOUR NAME INTO A FILE NAMED name.txt 
with open("name.txt","w") as f1:
    f1.write("MAHESH KUMAWAT\n")

#WRITE FIVE STUDENT NAME INTO A FILE CALLED student.txt
with open("student.txt","w") as f2:
    f2.write("MAHESH KUMAWAT\n")
    f2.write("KARAMUR BHARATI\n")
    f2.write("TIWARI SATYAM\n")
    f2.write("BAGHEL ATENDRA\n")
   
#TAKES USER INPUT AND SAVE INTO msg.txt
message = input('Enter some msg : ')
with open("msg.txt","a") as f3:
    f3.write(message+"\n")

#WRITE NUMBERS FROM 1-10 CALLED number.txt
with open("numbers.txt","a") as f4:
    f4.write("1,2,3,4,5,6,7,8,9,10\n")

#CREATE FILE NAME AS A bio.txt NAME, AGE, CITY, ADDRESS OR EMAIL WITH USER INPUT
name = input('Enter your name : ')
age = int(input("Enter your age : "))
city = input("Enter your city : ")
address = input("Address : ")
email = input('enter email : ')
with open("bio.txt","a") as f5:
    f5.write(name+"\n")
    f5.write(str(age)+"\n")
    f5.write(city+"\n")
    f5.write(address+"\n")
    f5.write(email+"\n")

# READ ALL FILES
with open("name.txt","r") as f1:
    print(40*"-")
    data1 = f1.read()
    print(data1)
    
with open("student.txt","r") as f2:
    print(40*"-")
    data2 = f2.read()
    print(data2)
   
with open("msg.txt","r") as f3:
    print(40*"-")
    data3 = f3.read()
    print(data3)
    
with open("numbers.txt","r") as f4:
    print(40*"-")
    data4 = f4.read()
    print(data4)
    
with open("bio.txt","r") as f5:
    print(40*"-")
    data5 = f5.read()
    print(data5)
    print(40*"-")