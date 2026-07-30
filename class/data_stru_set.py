#Set is a built in data structure in python it store unique value and in unorder sequance.
# s = {10,50,20}
# print(s)
# print (type(s))

# A = {"Hello","Hi","Hello"}
# print(A)

#Set Operation
# A[1] = "Hello"
# print(A)

# num = {21,34,54,12}
# print(num)
# num.add(32)
# print(num)

# panda = {"dodo","meet","bhoot"}
# print(panda)
# panda.add("Meow")
# print(panda)

# #update ()in set structure
# name = {"anut","janvi","apple"}
# tech_list = {"apple","google","bhoot"}
# name.update(tech_list)
# print(name)

# #Remove value from set using discard() function
# code = {"c","java","python"}
# print(code)
# code.discard("java")
# print(code)
# code.remove("c") #using remove() function
# print(code)

#Print all set value using for loop 
# code = {"c","c++","python"}
# for i in code :
#     print(i)

# #Print length of set using len() function
# number = {2,8,20,50,60,80}
# print(len(number))

# #Union operator is used to combine the set value.
# sub1 = {"java","js","python"}
# sub2 = {"eng","sci","math"}
# print(sub1|sub2)        # " | " is the union operator symbol
# print(sub1.union(sub2)) #and this is another way to combine value in set using union method

# #intersection method is uded to get common element or value from from the set
# A = {"Bhoot","panda","meow"}
# B = {"meet","janvi","panda"}
# print(A.intersection(B)) #this is how to use intersection method in set
# print(A & B)             #this is how to use intersection operator in set

# #Different between two set
# A = {1,5,3}
# B = {1,2,6}
# print(A-B)
# print(A.difference(B))

#Symmetric difference
# A = {1,2,3,5}
# B = {4,5,6}
# print(A^B)
# print(A.symmetric_difference(B))

#Equal Operator is used to check sets values are equal or not.
#It return boolean values like true or false
# A = {2, 1, 6}
# B = {1, 2, 6}
# print(A==B) #Using Operator ==
#print(A._eq_(B)) #Using "_eq_" Method



#1 Takes five numbers from user, store in set, and print all numbers using loop
numbers = set()
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.add(num)

print("Numbers in the set:")
for n in numbers:
    print(n)


#2 Take a set from user and check if a given number exists in the set
user_set = set(map(int, input("Enter numbers separated by space: ").split()))
check_num = int(input("Enter a number to check: "))

if check_num in user_set:
    print(f"{check_num} exists in the set.")
else:
    print(f"{check_num} does not exist in the set.")


#3 Create two sets: names and subjects, perform union using method and operator
names = {"Alice", "Bob", "Charlie"}
subjects = {"Math", "Science", "History"}

# Using union() method
union_method = names.union(subjects)
print("Union using method:", union_method)

# Using | operator
union_operator = names | subjects
print("Union using operator:", union_operator)


#4 Create a set and remove element using discard method
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print("Set after discarding 'banana':", fruits)


#5 Create three sets and print common values between them
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 2, 7, 8}

common_values = set1 & set2 & set3
print("Common values between three sets:", common_values)