#what is python.
# python is interpreted, object oriented high-level programming language.

# frist hello world program in python.
print("hello world")

# type() function use to find the data-type of the variable.
a = 12
b = "myname"
c = 4.5
d = 2 + 5j
print(type(a)) #int datatype
print(type(b)) #string datatype
print(type(c)) #float datatype
print(type(d)) #complex datatype


# using input() function.
p = input("enter the value of A:")
print("A:",p)

# keywords in py (keywords are the reserved words in python. we cannot use as variable name, funcion name and or any indentifier name.)
# example of keywords is int float if etc.

# datatype (dataype are used before of variable. to know which type of value stored in variable)
# datatypes of variable 1.numeric 2.boolean 3.sequence 4.set  5.dictonary
#boolean
data1 = True
print(type(data1))
data2 = False
print(type(data2))

#set
data3 = {"a", "b", "c"}
print(type(data3))

#dictnoray
data4 = {"key": "value"}
print(type(data4))

#sequence
#list
list1 = [1, 2, 3, 4]
print(type(list1))

#tuple
tuple2 = ("laptop", "phone", "bugs")
print(type(tuple2))

#string
string1 = "myname2"
print(type(string1))

#type conversion
# converting a datatype into anothere data type.
#example
n = int(input("enter the number: "))
print("the number is:",n)
print(type(n))

# conditional statements
# if simple statement.
x = int(input("Enter a number: "))
if(x >= 10):
  print("x is greater than or equal to 10")
  print("All done")

# if-else statement.
y = int(input("Enter a number: "))
if(y >= 10):
  print("y is greater than or equal to 10")
else:
  print("y is less than 10")

# if-else-lader statement.
z = int(input("Enter a number: "))
if z >= 70 :
  print("disct")
elif z >= 60 and z <= 70 :
  print("A gread")
elif z >= 55 and z <= 60 :
  print("B gread")
elif z >= 45 and z <= 55 :
  print("C gread")
else :
  print("FAIL")

#nested if statement.
age=int(input("enter your age: "))
if age>=18:
 wai=int(input("enter your wait: "))
 if wai>=50:
  print("you can donate")
 else:
  print("you are underwait")
else:
 print("you are underage")
 
 
 # understanding loops.
 # while loop.
 sum = 0
 n = int(input("enter your loop number: "))
 while n >= 0 :
   sum += n
   n-=1
   print("value of N: ", sum)
   print("bye")
   
   # simple for loop.
   lang = ["html", "css", "java", "python"]
   print(type())
   for i in lang :
     print(i, "and",len())
     
     # nested loop
     for i in range(1,6) :
      for j in range(i) :
        print("*",end= "")
        print()
# looping controle satements in python.
for letter in "python" :
  if letter == "o" :
    break
  print("current value: ", letter)
  print("bye")
  
        
    
      
    
     

  
 
