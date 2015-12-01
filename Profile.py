# my first edit
print "Welcome to the Profile Program\n"
name=raw_input("Input Name: ")
age=int(raw_input("Input Age: "))
motto=raw_input("Your Motto: ")
school=raw_input("Your School: ")
print "My name is %s and I am %d years old. My Motto is: %s and my school is %s" %(name, age, motto, school)
if age>=18:
	print"You are able to vote at your age of %d" %age
	print"And also for marrying the right person"
	# how to add more?????
else:
	print"You are not able to vote at your age of %d" %age

while age<=100:
	age+=10
	print "Your age plus with 10 is %d" %age
else : 
	print"Your age is still the same: %d" %age
	
# how to do for loop??? and do while loop???? array/list, alternative for if else like switch, exception catching.......

a=int(raw_input("Enter Triangle's Height: "))

x=1
y=1	
while x<=a:
	while y<=x:
		print "*" * y
		y+=1
	x+=1
	
fail=0
sum=0
ctr=1

input=int(raw_input("How many grades will you input: "))

while ctr<=input:
	ctr+=1
	grade=int(raw_input("Enter grade: "))

	if grade<75:
		fail+=1
	sum+=grade
average=sum/input
print"The average of %f\n"%average
print"The failure is %d"%fail


# a=int(raw_input("Enter Pyramid's Height: "))
# x=1
# n=1
# y=0
# d=1
# n=1
# while x<=a:
	# while y<(a-x):
		# print" " * y
		# y+=1
	# while d<=x:
		# print "*" * d
		# d+=1
	# while n<x:
		# print "*" * n
		# n+=1
	# x+=1
	
name='John'
if name in ["John", "Rick"]:
    print "Your name is either John or Rick."