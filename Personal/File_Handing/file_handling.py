#1
# with open("student.txt","a") as f:
#     f.write("Mahesh\nAhemdabad\n19")

#2
# with open("student.txt","r") as f:
#     print(f.read())

#3
# with open("student.txt","r") as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())

#4
# cnt = 0
# with open("student.txt","r") as f:
#     data = True
#     while data:
#         data = f.readline()
#         if data !="":
#             cnt = cnt +1
# print(cnt)

#5
# sumChar = 0
# with open("student.txt",'r') as f:
#     data = f.read()
# l = data.split()
# for i in range(len(l)):
#     sumChar = sumChar + len(l[i])
# print(f"Total Characters : {sumChar}")

#6
# cnt = 0
# digit = 0
# with open("student.txt",'r') as f:
#     data = f.read()
# l = data.split()
# for i in range(len(l)):
#     if l[i].isalpha():
#         cnt  = cnt +1
#     elif l[i].isnumeric():
#         digit = digit +1
# print(f"Words : {cnt}")
# print(f"Numbers : {digit}")

#7
# with open("student.txt","a") as f:
#     f.write("\nPython is My Favorite line")

#8
# with open("student.txt","r") as f:
#     print(f.readline())

#9***
# cnt = 0
# with open("student.txt","r") as f:
#     data = True
#     while data:
#         data = f.readline()
#         if data !="":
#             cnt = cnt +1
# n = cnt
# count = 0
# with open("student.txt", "r") as f:
#     while count< n:
#         line = f.readline()
#         count += 1
# print(line)


#10
# f = open("student.txt","r")
# data = f.read()
# print(data.upper())

#11
# word = input("Enter word : ")
# f = open("student.txt","r")
# data = f.read()
# if word in data:
#     print(f"{word} in file")
# else:
#     print(f"{word} not exists in file")

#12
# cnt = 0
# word = input("Enter word : ")
# f = open("student.txt","r")
# data = f.read()
# cnt =data.count(word)
# print(f"{word} appears {cnt} time")

#13
# f = open("student.txt","r")
# data = f.read()
# with open("backup.txt","a") as f1:
#     f1.write(data)

#14
# with open("student.txt",'r') as f:
#     data = f.read()
# new_data = data.replace("Mahesh","Ramesh")
# with open("student.txt",'w') as f1:
#     f1.write(new_data)

#15***
# cnt = 0
# with open("student.txt", "r") as f:
#     data = f.readline()
#     while data:
#         cnt += 1
#         print(f"{cnt}. {data}", end="")
#         data = f.readline()
    
#16
# with open("student.txt","a") as f:
#     for i in range(1,4):
#         username = input(f"Student {i} name : ")
#         age = input(f"Student {i} age : ")
#         city = input(f"Student {i} city : ")
#         f.write(f"{username} {age} {city}\n")

#17
# with open("student.txt","r") as f:
#     data = f.read()
# print(data)

#18
# name = input("Name : ")
# with open("student.txt","r") as f:
#     while True:
#         line = f.readline()

#         if line =="":
#             print("Name not found")
#             break

#         if name in line:
#             print(line)
#             break

#19***
# cnt = 0

# with open("student.txt", "r") as f:
#     while True:
#         line = f.readline()

#         if line == "":
#             break

#         if line.strip() == "":
#             cnt += 1

# print(cnt)

#20
# open_file = input("TO OPEN FILE AND READ (PRESS) 'OR' : ").upper()
# def seefile(open_file):
#     if open_file == "OR":
#         with open("notes.txt","r") as f:
#             data = f.read()
#             print(data)
# seefile(open_file)

# close_file = input("TO CLOSE FILE (PRESS) 'C' : ").upper()
# def closefile(close_file):
#     if close_file=="C":
#         with open("notes.txt","w") as f:
#             print(f.write("\n"))
# closefile(close_file)
